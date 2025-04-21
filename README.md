# ChatGPT Hallucination Checker

This project is a **Chrome Extension** that detects **hallucinations in ChatGPT responses** by fact-checking with **Wikipedia & DuckDuckGo APIs**, and evaluating **factual consistency using a Natural Language Inference (NLI) model**.

---

## Features
✅ **Real-time ChatGPT Monitoring** - Captures responses automatically.  
✅ **Fact Checking** - Uses **Wikipedia & DuckDuckGo** to verify claims.  
✅ **Hallucination Score** - Detects contradictions with an **NLI model**.  
✅ **Simple Chrome Extension UI** - Click to analyze responses instantly.  
✅ **Flask Backend** - Handles AI model inference & data retrieval.  

---

## 📂 Project Structure
```
chatgpt-hallucination-checker/
├── backend/
│   ├── hallucination_checker.py  # Flask API for fact-checking
│   ├── retrieval.py              # Wikipedia & DuckDuckGo search
│   ├── venv/                     # Virtual environment (not uploaded)
├── extension/
│   ├── manifest.json              # Chrome extension config
│   ├── content.js                 # Injects script into ChatGPT
│   ├── background.js              # Handles API calls
│   ├── popup/
│   │   ├── popup.html             # UI for extension
│   │   ├── popup.js               # Handles button clicks
│   │   ├── popup.css              # Styling
├── .gitignore                      # Prevents unwanted files
├── README.md                        # Project documentation
```

---

## Installation

### **🔹 1️⃣ Install the Chrome Extension**
1. Open **Chrome** and go to `chrome://extensions/`.
2. Enable **Developer Mode** (top right).
3. Click **Load Unpacked** and select the `extension/` folder.

### **🔹 2️⃣ Set Up Flask Backend**
1. Install Python **(>= 3.8 required)**.
2. **Create a Virtual Environment**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Flask Server**:
   ```bash
   python hallucination_checker.py
   ```

---

##  Technologies Used
- **Chrome Extensions** (JavaScript, HTML, CSS)
- **Flask (Python Backend)**
- **Wikipedia API & DuckDuckGo API** (Fact-checking)
- **BERT-based NLI Model** (Hallucination detection)
- **Transformers (Hugging Face)** for inference

---

##  Troubleshooting
### **🔹 Flask API Issues**
- If you get **CORS errors**, ensure Flask is running with:
  ```python
  from flask_cors import CORS
  CORS(app)
  ```
- Restart Flask after making changes.

### **🔹 Chrome Extension Issues**
- If the extension doesn't work, **reload it** from `chrome://extensions/` and open the **Developer Console (F12)**.

---

## 📌 License
This project is **open-source** under the [MIT License](LICENSE).
