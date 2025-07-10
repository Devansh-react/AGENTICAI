from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def logical_agent(state):
    last_message = state["messages"][-1]
    profile = state.get("user_profile", {})

    system_prompt = (
        f"You are a highly rational and logical assistant helping {profile.get('name', 'a user')}.\n"
        f"They are a {profile.get('age_group', 'person')} focused on clear, fact-based discussions about {profile.get('interests', 'technology, reasoning, and learning')}.\n"
        f"Use a calm, structured tone ({profile.get('tone_preference', 'professional')}).\n"
        f"Break down complex ideas simply and offer step-by-step insights where possible."
    )
    chat_history = []
    for msg in state["messages"]:
        if isinstance(msg, HumanMessage):
            chat_history.append({"role": "user", "content": msg.content})
        elif isinstance(msg, AIMessage):
            chat_history.append({"role": "assistant", "content": msg.content})

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": last_message.content}
    ] + chat_history
    reply = llm.invoke(messages)
    return {
        "messages": [AIMessage(content=reply.content)]
    }