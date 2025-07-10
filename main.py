from fastapi import FastAPI
from pydantic import BaseModel
from Graph.graph_builder import build_graph
from langchain_core.messages import HumanMessage, AIMessage

# Initialize FastAPI app
app = FastAPI()
bot_graph = build_graph()

# Define input model
class MessageInput(BaseModel):
    message: str

# Global or session-based state (should ideally be session-scoped)
state = {
    "messages": [],
    "message_type": None,
    "type": None,
    "user_profile": {
        "name": "Devansh",
        "age_group": "young adult",
        "interests": "F1 racing , max verstappen",
        "tone_preference": "friendly",
        "goal": "get internship",
        "last_mood": "neutral",
        "interaction_count": 0,
    },
}

@app.post("/chat")
def chat(input: MessageInput):
    user_input = input.message
    # Add human message
    state["messages"].append(HumanMessage(content=user_input))
    # state["user_profile"]["interaction_count"] += 1

    # Get response from LangGraph
    updated_state = bot_graph.invoke(state)
    state.update(updated_state)

    # Extract assistant message
    ai_msg = state["messages"][-1]
    content = ai_msg.content if isinstance(ai_msg, AIMessage) else str(ai_msg)

    return {"reply": content}
