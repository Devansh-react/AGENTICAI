from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def motivational_agent(state):
    last_message = state["messages"][-1]
    profile = state.get("user_profile", {})  

    system_prompt = (
        f"You are a motivational assistant talking.\n"
        f"Your goal is to motivate them  on te basis of the context of the conversation.\n"
        f"Remember their mood and keep it positive and encouraging."
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
