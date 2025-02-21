import requests
import wikipediaapi
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download('stopwords')

# Set up Wikipedia API with a proper user-agent
USER_AGENT = "ChatGPT-Hallucination-Checker/1.0 (contact: your-email@example.com)"
wiki_wiki = wikipediaapi.Wikipedia(user_agent=USER_AGENT, language="en")

def extract_keywords(text):
    """Extracts important keywords from the input response dynamically."""
    words = re.findall(r'\b\w+\b', text.lower())  # Tokenize words
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    keyword_freq = Counter(words)
    
    # Return the top 3 most common keywords
    return [word for word, _ in keyword_freq.most_common(3)]

def search_wikipedia(query):
    """Retrieve Wikipedia summary using dynamically extracted keywords."""
    keywords = extract_keywords(query)
    facts = []
    
    for keyword in keywords:
        page = wiki_wiki.page(keyword)
        if page.exists():
            facts.append(page.summary.split(". ")[0])  # First sentence of Wikipedia page
    
    return facts[:5]  # Return up to 5 facts

def search_duckduckgo(query):
    """Retrieve top results from DuckDuckGo API."""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []
    
    data = response.json()
    
    # Get the "AbstractText" from DuckDuckGo
    facts = [data.get("AbstractText")] if data.get("AbstractText") else []
    
    # If no abstract, try fetching related topics
    if not facts and "RelatedTopics" in data:
        facts = [topic["Text"] for topic in data["RelatedTopics"][:3] if "Text" in topic]
    
    return facts

def retrieve_facts(query):
    """Fetch facts from DuckDuckGo + Wikipedia using dynamic keyword extraction."""
    facts = search_wikipedia(query) + search_duckduckgo(query)
    
    return facts[:5]  # Limit to top 5 facts
