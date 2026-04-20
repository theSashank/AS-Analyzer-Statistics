# AS — Analyzer Statistics

An AI-powered dataset generator that takes a user prompt and generates 
realistic structured datasets downloadable in multiple formats.

## 🚀 Features
- Natural language prompt → instant dataset
- Download in CSV, JSON, XLSX, SQL, TXT
- Fully local AI (Ollama + LLaMA 3) — no API costs
- Clean table preview in browser

## 🛠 Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python + Flask
- **AI:** Ollama (LLaMA 3) — runs locally
- **Data Export:** Pandas, OpenPyXL

## 📁 Project Structure
```
AS/
├── app.py              # Flask backend
├── agent.py            # Agent + LLM interaction
├── exporter.py         # File export logic
├── templates/
│   └── index.html      # Frontend UI
├── outputs/            # Generated dataset files
└── requirements.txt
```

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install flask requests pandas openpyxl
```

### 2. Start Ollama
Open Ollama app (runs on `http://localhost:11434`)

### 3. Pull LLaMA 3 model
```bash
ollama pull llama3
```

### 4. Run the app
```bash
python app.py
```

### 5. Open browser
```
http://127.0.0.1:5000
```

## 📌 Current Status
- [x] Phase 1 — Planning
- [x] Phase 2 — Requirements
- [x] Phase 3 — System Design
- [x] Phase 4 — Basic Implementation
- [ ] Phase 5 — Encoder + Decoder
- [ ] Phase 6 — Memory / Change Loop
- [ ] Phase 7 — Testing
- [ ] Phase 8 — Deployment

## 🔮 Upcoming
- Encoder — structures user prompt into precise instructions
- Decoder — validates and cleans LLM output
- Memory loop — refine dataset without regenerating
- Row count control
- Public deployment (Streamlit / Render)

## 👤 Author
Sashank — BSc CS + MCA