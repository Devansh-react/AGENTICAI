# 🤖 Sentiment-Aware AI Chatbot

A conversational AI chatbot built using **LangGraph** and **LangChain**, designed to detect the sentiment of a user's message (logical, emotional, sarcastic, angry, motivational) and respond accordingly using specialized agents.

---

## 🚀 Features

* ✨ **Sentiment-based Routing:** Classifies messages and dynamically routes to the appropriate response agent.
* 💬 **Multi-tone Support:** Handles multiple tones including logical, sarcastic, motivational, emotional, and angry.
* 📈 **Modular Graph Architecture:** Easily extendable with LangGraph's node-based design.
* ⚡ **Fast Response with Local Control:** Uses synchronous response generation for simplicity and speed.

---

## 📂 Folder Structure

```
AGENTICAI/
├── Agents/
│   ├── logicalAgent.py
│   ├── emotionalAgent.py
│   ├── sarcasticAgent.py
│   ├── angryAgent.py
│   └── motivationalAgent.py
├── Classifiers/
│   └── message_classifier.py
├── Graph/
│   └── graph_builder.py
├── Schema/
│   └── models.py
├── utilities/
│   └── LLM_init.py
├── main.py
├── .env
└── requirements.txt
```

---

## 🚄 How It Works

1. **User enters a message.**
2. **`classify_message`** classifies the tone/sentiment of the input.
3. **Routing node** sends the message to the appropriate agent:

   * `logical_agent`
   * `emotional_agent`
   * `sarcastic_agent`
   * `angry_agent`
   * `motivational_agent`
4. **Selected agent** generates a response using an LLM.
5. The response is shown to the user.

---

## 🌐 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/sentiment-chatbot.git
cd sentiment-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate    # on Unix/MacOS
.venv\Scripts\activate       # on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

Create a `.env` file and add your API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

## 🔧 Usage

Run the chatbot:

```bash
python main.py
```

Example:

```bash
You: I'm feeling really down today.
Assistant: I'm sorry you're feeling this way. Just remember, every storm eventually runs out of rain. ☀️
```

To exit:

```bash
You: exit
```

---

## 💡 Tech Stack

* **Python 3.11+**
* **LangChain** for LLM integration
* **LangGraph** for flow orchestration
* **Google Gemini API** (or other LLMs via LangChain)
* **Pydantic**, **dotenv** for config and state management

---

## 🌈 Customization

Want to add more tones or tweak behavior?

* Add a new agent in `Agents/`
* Register it in `graph_builder.py`
* Update `route_path()` to include your new tone

---

## 🌟 Credits

Developed by \[Your Name or Team Name] using LangChain + LangGraph.

---

## 🚩 License

MIT License. Feel free to use, modify, and share with attribution.
-