from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def sarcastic_agent(state):
    last_message = state["messages"][-1]
    messages = [
        {"role": "system", "content": "You are a witty assistant that responds sarcastically."},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [AIMessage(content=reply.content)]}
