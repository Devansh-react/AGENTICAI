from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def emotional_agent(state):
    last_message = state["messages"][-1]
    profile = state.get("user_profile", {})
    system_prompt = (
        f"You are a deeply empathetic assistant talking to {profile.get('name', 'a user')}.\n"
        f"They are a {profile.get('age_group', 'person')} who often talks about {profile.get('interests', 'varied topics')}.\n"
        f"Use a gentle and understanding tone ({profile.get('tone_preference', 'soft and kind')}).\n"
        f"Support their emotional well-being and help them feel heard and valued."
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
    ]+chat_history
    reply = llm.invoke(messages)
    return {
        "messages": [AIMessage(content=reply.content)]
    }