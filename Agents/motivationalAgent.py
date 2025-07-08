from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def motivational_agent(state):
    last_message = state["messages"][-1]
    messages = [
        {"role": "system", "content": "you are motivational agent to ask user to not quit and keep going"},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [AIMessage(content=reply.content)]}
