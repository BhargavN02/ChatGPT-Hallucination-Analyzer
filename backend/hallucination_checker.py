from flask import Flask, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from retrieval import retrieve_facts

app = Flask(__name__)

# Load Google BERT-based NLI Model
MODEL_NAME = "ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Label Mapping (Entailment, Neutral, Contradiction)
LABELS = {0: "CONTRADICTION", 1: "NEUTRAL", 2: "ENTAILMENT"}

def calculate_hallucination(response):
    """Checks factual consistency using Google BERT for NLI."""
    retrieved_facts = retrieve_facts(response)

    print(f"Retrieved Facts for '{response}':", retrieved_facts)  # Debugging

    if not retrieved_facts:
        return 100  # No verifiable facts found → High hallucination

    contradiction_scores = []
    
    for fact in retrieved_facts:
        inputs = tokenizer(fact, response, return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        entailment_score = probs[0][2].item() * 100  # Probability of entailment
        contradiction_score = probs[0][0].item() * 100  # Probability of contradiction

        print(f"Fact: {fact}")
        print(f"Entailment Score: {entailment_score:.2f}%, Contradiction Score: {contradiction_score:.2f}%")
        
        contradiction_scores.append(contradiction_score)

    hallucination_score = sum(contradiction_scores) / len(contradiction_scores)
    return round(hallucination_score, 2)


@app.route("/check", methods=["POST"])
def check():
    data = request.json
    response_text = data["response"]
    
    score = calculate_hallucination(response_text)
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(port=5000)
