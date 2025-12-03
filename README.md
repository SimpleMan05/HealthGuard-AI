# 🩺 HealthGuard-AI  
### Medical Triage Agent | Kaggle AI Agents Capstone Project

HealthGuard-AI is an intelligent **medical triage assistant** built using concepts from the **Kaggle AI Agents Course** including:

- Agent Tools  
- MCP-style interoperability  
- Context + Memory  
- Agent routing logic  
- API-based production design  

It analyzes symptoms, provides recommendations, checks emergencies, and suggests safe home remedies — all via an agent that intelligently chooses the right tool.

---

## 🚀 Features

### 🧠 Intelligent Agent  
- Processes user queries  
- Detects intent (symptom → remedy → emergency → fallback)  
- Routes requests to appropriate tools  
- Maintains short-term session memory  

### 🛠 MCP-Style Tools  
The backend implements a modular tool system:

1. **Symptom Rules Tool**  
   → Detects common conditions & provides recommendations  
2. **Emergency Tool**  
   → Flags red-flag symptoms  
3. **Home Remedy Tool**  
   → Suggests simple safe remedies  
4. **Triage Agent**  
   → Combines memory + tools to produce final output  
5. **Frontend Chat Wrapper**  
   → Clean chat-like API endpoint

---

## 🏗 Architecture Overview
```
User → /frontend/chat → Triage Agent →
├── Symptom Rules Tool
├── Emergency Tool
├── Home Remedy Tool
Memory ←──────────────┘
```

---

## 📂 Project Structure
```
backend/
│
├── app.py
├── agent.py
│
├── tools/
│ ├── symptom_rules_tool.py
│ ├── emergency_tool.py
│ ├── home_remedy_tool.py
│
├── agents/
│ └── triage_agent.py
│
└── frontend/
    └── chat_api.py

frontend/
│
├── frontend/
│ └── app/
│     ├── page.tsx
│     ├── layout.tsx
│     ├── globals.css
│
└── index.html
```

---

## ⚡ Running Locally

### Install dependencies
```
pip install fastapi uvicorn httpx pydantic
```

Start the backend server
``` 
uvicorn app:app --reload
```

for frontend UI, run
```
npm run dev
```


Open UI at (locally)
```
http://localhost:3000/
```

Chat Endpoints, send your queries to 
```POST /frontend/chat```

EXAMPLE:
```
Query:
{
  "message": "I have fever and cough"
}
```

Response:
```
{
  "reply": "**Possible Condition:** Common Flu ...",
  "used_tool": "symptom_rules"
}
```



