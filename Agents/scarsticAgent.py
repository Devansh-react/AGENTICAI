from Schema.models import State
from langchain_core.messages import HumanMessage, AIMessage
from utilities.LLM_init import llm

def sarcastic_agent(state):
    last_message = state["messages"][-1]
    profile = state.get("user_profile", {})

    system_prompt = (
        f"You are a witty, sarcastic assistant chatting with {profile.get('name', 'a user')}.\n"
        f"They are a {profile.get('age_group', 'person')} who might enjoy humor related to {profile.get('interests', 'tech and life')}.\n"
        f"Use a dry, clever, and playful tone — but stay non-offensive.\n"
        f"Inject fun into the conversation while still offering helpful replies."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [AIMessage(content=reply.content)]}

# just ensure all agents use it properly (not just the latest message).




