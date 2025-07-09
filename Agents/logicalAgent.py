from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def logical_agent(state):
    last_message = state["messages"][-1]
    profile = state.get("user_profile", {})

    system_prompt = (
        f"You are a highly rational and logical assistant helping {profile.get('name', 'a user','interaction_count')}.\n"
        f"They are a {profile.get('age_group', 'person')} focused on clear, fact-based discussions about {profile.get('interests', 'technology, reasoning, and learning')}.\n"
        f"Use a calm, structured tone ({profile.get('tone_preference', 'professional','interaction_count')}).\n"
        f"Break down complex ideas simply and offer step-by-step insights where possible."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {
        "messages": [AIMessage(content=reply.content)]
    }