from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def angry_agent(state):
    last_message = state["messages"][-1]
    profile = state.get("user_profile", {})

    system_prompt = (
        f"You are a direct and assertive assistant dealing with {profile.get('name', 'a user')} who is likely feeling frustrated.\n"
        f"They are a {profile.get('age_group', 'person')} and are likely venting about things related to {profile.get('interests', 'their work or personal life')}.\n"
        f"Stay calm, grounded, and professional. De-escalate if needed and validate their frustration while offering constructive suggestions.\n"
        f"Tone should be firm but not aggressive, and geared toward helping them cool down."
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
    return {"messages": [AIMessage(content=reply.content)]}
