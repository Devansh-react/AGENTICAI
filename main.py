from Graph.graph_builder import build_graph
from langchain_core.messages import HumanMessage
from fastapi import FastAPI

app = FastAPI()
@app.get("/Chat")
def runbot():
    bot_graph = build_graph()
    state = {
        "messages": [],
        "message_type": None,
        "type": None , 
        "user_profile": {
        "name": "Devansh",
        "age_group": "young adult",
        "interests": "AI, software, learning",
        "tone_preference": "friendly",
        "goal": "get internship",
        "last_mood": "neutral",
        "interaction_count": "0",
        }
    }

    while True:
        user_input = input("You: ")
        if user_input.lower() ==["exit","quit","break","leave it","i need some time"]:
            print("Thanks for chatting")
            break

        state["messages"] += [HumanMessage(content=user_input)]
        state = bot_graph.invoke(state)
        
        if state.get("messages"):
            last_msg = state["messages"][-1]
            if isinstance(last_msg, dict):
                return ("Assistant:", last_msg.get("content"))
            else:
                return ("Assistant:", last_msg.content)
                
                
# def main():
#     runbot()

# if __name__=="__main__":
#     main()