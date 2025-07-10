import streamlit as st
import uuid
import requests

st.set_page_config(page_title="Sentiment-Aware AI Chatbot", page_icon="💬")
st.title(":speech_balloon: Sentiment-Aware AI Chatbot")

# Generate unique session ID once per session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Initialize chat history if not already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display the welcome message
with st.expander("ℹ️ What can this chatbot do?"):
    st.markdown("""
    This intelligent chatbot understands your mood and responds accordingly! 

    **Examples you can try:**
    - "I'm feeling down."
    - "Cheer me up."
    - "Explain what AI is."
    - "Tell me a joke."
    
    Your responses are personalized and your mood is remembered across the session.
    """)

# Display past chat messages
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Get user input
user_input = st.chat_input("Type your message...")
if user_input:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send message to FastAPI backend
    try:
        response = requests.post("http://localhost:8000/chat", json={
            "session_id": st.session_state.session_id,
            "message": user_input
        })

        if response.status_code == 200:
            ai_reply = response.json().get("reply", "")
            st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
            with st.chat_message("assistant"):
                st.markdown(ai_reply)
        else:
            st.error("Server error: Unable to get a response from the backend.")

    except Exception as e:
        st.error(f"Exception occurred: {e}")

# Optional Debug Section
with st.expander("🔐 Session Info"):
    st.write("**Session ID:**", st.session_state.session_id)
    st.write("**Total Messages:**", len(st.session_state.chat_history))

# Reset Button
if st.button("🔄 Reset Chat"):
    st.session_state.chat_history = []
    st.rerun()