from fastapi import FastAPI
from pydantic import BaseModel
from Graph.graph_builder import build_graph
from langchain_core.messages import HumanMessage, AIMessage , BaseMessage
from Database.memory_manager import get_history
# Initialize FastAPI app
app = FastAPI()
bot_graph = build_graph()

# Define input model
class MessageInput(BaseModel):
    session_id:str
    message: str

# Global or session-based state (should ideally be session-scoped)


@app.post("/chat")
def chat(input: MessageInput):
    session_id = input.session_id
    user_input = input.message
    
    
    # retriving onder messages 
    history_message = get_history(session_id)
    
    # saving new user messages 
    history_message.add_user_message(user_input)
    
    
    # adding messages to message list filtering out the ai and humna message 
    messages = []
    for m in history_message.messages:
        if(m.type=="human"):
            messages.append(HumanMessage(content=m.content))
        else:
            messages.append(AIMessage(content=m.content))
            
    # now updating the message in state   
    state = {
    "messages":messages,
    "message_type": None,
    "type": None,
    #  for secutrity reason we cannot senhd the data to LLm  have to remove it 
    "user_profile": {
        "session_id":session_id,
        "last_mood": "neutral",
    },
    }     
    new_state = bot_graph.invoke(state)
    ai_response = new_state["messages"][-1].content

    # Save assistant message
    history_message.add_ai_message(ai_response)

    return {"reply": ai_response}