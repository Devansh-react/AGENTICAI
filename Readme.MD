# 🧠 AGENTICAI: Humanlike Emotion-Sensitive Chatbot with LangGraph + LangChain

## 📌 Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Folder Structure](#folder-structure)
5. [Installation Guide](#installation-guide)
6. [Environment Configuration](#environment-configuration)
7. [Core Concepts](#core-concepts)
8. [LangGraph Architecture](#langgraph-architecture)
9. [Agent Descriptions](#agent-descriptions)
10. [Message Routing](#message-routing)
11. [PostgreSQL Chat History](#postgresql-chat-history)
12. [Error Handling & Debugging](#error-handling--debugging)
13. [Future Enhancements](#future-enhancements)

---

## 📖 Project Overview

AGENTICAI is a LangGraph-based chatbot that mimics human-like emotional intelligence. It routes messages to appropriate agents (emotional, logical, sarcastic, etc.) based on context, sentiment, and user profile using LangChain and LangGraph.

---

## 🛠 Tech Stack

* **Python 3.11+**
* **LangGraph**
* **LangChain**
* **FastAPI**
* **Google Generative AI / Gemini**
* **PostgreSQL**
* **Pydantic v2**
* **Dotenv**
* **Uvicorn**

---

## ✨ Features

* Emotionally intelligent conversations
* Context-aware message routing
* Human-like tone generation
* Sentiment-based response agents
* Persistent PostgreSQL chat history

---

## 📁 Folder Structure

```
AGENTICAI/
│
├── Agents/
│   ├── emotionalAgent.py
│   ├── logicalAgent.py
│   ├── sarcasticAgent.py
│   ├── angryAgent.py
│   ├── motivationalAgent.py
│   └── humanLike.py
│
├── Classifiers/
│   └── message_classifier.py
│
├── Schema/
│   └── models.py
│
├── utilities/
│   └── LLM_init.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation Guide

```bash
git clone https://github.com/yourusername/AGENTICAI.git
cd AGENTICAI
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration (`.env`)

```env
GOOGLE_API_KEY=your_google_genai_api_key
DATABASE_URL=postgresql://username:password@localhost:5432/chatbot_db
```

---

## 🧬 Core Concepts

* **LangGraph** builds finite-state machine logic on top of LangChain.
* **State** is passed between nodes, evolving across graph transitions.
* **TypedDict/Pydantic** enforces strong typing of state (`State` model).
* Each **Agent** is a callable function (like `humanlike`, `emotional_agent`) returning new messages.
* **Routing Node** uses `message_classifier` to determine agent type.

---

## 🧐 LangGraph Architecture

```python
graph = StateGraph(State)
graph.add_node("humanlike", humanlike)
graph.add_node("logical", logical_agent)
graph.add_node("emotional", emotional_agent)
graph.add_node("sarcastic", sarcastic_agent)
graph.add_node("motivational", motivational_agent)
graph.add_node("angry", angry_agent)

graph.add_conditional_edges("router", route, {
  "humanlike": "humanlike",
  "emotional": "emotional",
  "logical": "logical",
  ...
})
graph.set_entry_point("router")
graph.set_finish_point("humanlike")
bot_graph = graph.compile()
```

---

## 🧑‍💼 Agent Descriptions

| Agent          | Behavior                                                    |
| -------------- | ----------------------------------------------------------- |
| `humanlike`    | Warm, empathetic, human tone, uses humor/motivation/support |
| `emotional`    | Matches user emotional tone and responds sensitively        |
| `logical`      | Analytical, gives factual, structured replies               |
| `sarcastic`    | Uses witty, dry humor in appropriate situations             |
| `angry`        | Mimics angry tone while avoiding escalation                 |
| `motivational` | Encourages and inspires the user                            |

---

## 🔀 Message Routing

### `message_classifier.py`

* Uses LLM to classify intent/emotion of the latest message.
* Output: `"humanlike"`, `"emotional"`, `"logical"`, etc.

### `route(state: State)`:

```python
def route(state: State):
    classification = classify_message(state)
    return {"type": classification}
```

---

## 📂 PostgreSQL Chat History

### `.env`

```env
DATABASE_URL=postgresql://user:pass@localhost:5432/chatbot_db
```

### `get_history(session_id)`

```python
PostgresChatMessageHistory(
    connection_string=os.getenv("DATABASE_URL"),
    session_id=session_id,
    table_name="chat_messages"
)
```

---

## 🛠 Error Handling & Debugging

* Common error: `ValidationError: content.str` → caused by using `HumanMessage` objects instead of plain strings when calling `.invoke()`.
* Fix: Convert `HumanMessage` and `AIMessage` to raw string in message history before invoking `llm`.

---

## 🚀 Future Enhancements

* Add voice support using ElevenLabs or TTS APIs.
* Fine-tune Gemini prompts for each agent.
* Add emotion-specific avatars in UI (if frontend added).
* Implement fallback/error recovery in LangGraph routes.
* Add user personalization using long-term memory (e.g., Redis, Pinecone).

---
