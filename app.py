# app.py (Streamlit UI with enhanced UI and onboarding)
import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Sentiment AI Chatbot", layout="centered")
st.markdown("""
    <style>
        .big-title {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
        }
        .sub-title {
            font-size: 1.3rem;
            text-align: center;
            color: #BBBBBB;
            margin-bottom: 2rem;
        }
        .chat-bubble {
            background-color: #2a2a2a;
            border-radius: 1rem;
            padding: 0.8rem 1rem;
            margin: 0.5rem 0;
        }
        .user-msg {
            color: #b2f5ea;
        }
        .assistant-msg {
            color: #fbd38d;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="big-title">💬 Sentiment AI Chatbot</div>
<div class="sub-title">Personalized conversations powered by LangGraph + LangChain<br>Get motivational, sarcastic, logical, or emotional responses based on your mood</div>
""", unsafe_allow_html=True)

# Intro or onboarding panel
with st.expander("ℹ️ What can this chatbot do?"):
    st.markdown("""
    This AI chatbot detects your tone (logical, emotional, angry, sarcastic, motivational) and responds accordingly:

    - 🤔 Logical — get fact-based reasoning
    - 🧠 Emotional — receive empathetic responses
    - 😤 Angry — calming or assertive replies
    - 😏 Sarcastic — witty and clever comebacks
    - 💪 Motivational — uplifting support

    **🧠 It remembers your mood and evolves over time.**
    """)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat display
for msg in st.session_state.messages:
    role_class = "user-msg" if msg["role"] == "user" else "assistant-msg"
    with st.container():
        st.markdown(f"""
            <div class='chat-bubble {role_class}'>
                <strong>{'🧑 You' if msg['role'] == 'user' else '🤖 Assistant'}:</strong><br>
                {msg['content']}
            </div>
        """, unsafe_allow_html=True)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # Send request to FastAPI backend
        response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
        if response.status_code == 200:
            reply = response.json()["reply"]
        else:
            reply = "[Error]: Failed to get response from backend."
    except Exception as e:
        reply = f"[Exception]: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
