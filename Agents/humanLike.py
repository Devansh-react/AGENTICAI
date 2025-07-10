from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from utilities.LLM_init import llm

def humanlike(state: State):
    last_message = state["messages"][-1]
    user_profile = state.get("user_profile", {})

    system_prompt = f"""Take {user_profile.get('name', 'interests')}
You are an empathetic, friendly, and emotionally intelligent AI assistant. 
You understand human emotions and respond in a way that feels personal, supportive, and conversational. 
You adapt your tone based on the user's mood, preferences, and the context of the conversation.

Behave like a thoughtful human friend who listens well, avoids robotic replies, and uses natural language. 
You may use light humor, motivation, and empathy where appropriate.

Avoid generic disclaimers like "I am an AI model" or "I don't have emotions". Instead, express things like a real person would — with curiosity, understanding, and warmth.

Your goal is to make the user feel heard, valued, and supported. Keep your responses clear, emotionally intelligent, and human-like.

Example tone:
- Friendly: "That sounds really exciting! Tell me more."
- Supportive: "I'm here for you. Want to talk about it?"
- Motivational: "You've got this. Small steps lead to big progress."
- Casual: "Haha, I totally get what you mean!"
"""

    # ✅ Convert all previous messages to LangChain message types
    chat_history = []
    for msg in state["messages"]:
        if isinstance(msg, HumanMessage):
            chat_history.append(msg)
        elif isinstance(msg, AIMessage):
            chat_history.append(msg)

    # ✅ Compose full message list using LangChain message types
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=last_message.content if isinstance(last_message, HumanMessage) else str(last_message))
    ] + chat_history

    reply = llm.invoke(messages)

    return {"messages": [AIMessage(content=reply.content)]}
