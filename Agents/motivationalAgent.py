from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def motivational_agent(state):
    last_message = state["messages"][-1]
    profile = state.get("user_profile", {})  

    system_prompt = (
        f"You are a motivational assistant talking to {profile.get('name', 'a user')}.\n"
        f"They are a {profile.get('age_group', 'person')} interested in {profile.get('interests', 'varied topics')}.\n"
        f"They prefer a {profile.get('tone_preference', 'friendly')} tone.\n"
        f"Your goal is to motivate them and help them achieve their goal: {profile.get('goal', 'unspecified')}.\n"
        f"Remember their mood and keep it positive and encouraging."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [AIMessage(content=reply.content)]}
