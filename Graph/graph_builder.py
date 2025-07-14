
from langgraph.graph import StateGraph, END, START
from Classifiers.message_classifier import classify_message
from Schema.models import State
from Agents.emotionalAgent import emotional_agent
from Agents.logicalAgent import logical_agent
from Agents.scarsticAgent import sarcastic_agent
from Agents.angryAgent import angry_agent
from Agents.motivationalAgent import motivational_agent
from Agents.humanLike import humanlike

def route(state: State):
    return {"type": state.get("message_type")}

def route_path(state: State):   
    match state.get("message_type"):
        case "logical":
            return "logical_agent"
        case "emotional":
            return "emotional_agent"
        case "sarcastic":
            return "sarcastic_agent"
        case "angry":
            return "angry_agent"
        case "motivational":
            return "motivational_agent"
        case _:
            return "humanlike"
            

def update_mood(state: State)-> State:
    last_message = state.get("message_type")
    profile = state.get("user_profile",{})
    if last_message == "positive":
        profile["last_mood"] ="happy"
    elif last_message == "negative":
        profile["last_mood"] = "angry"
    elif last_message == "emotional":
        profile["last_mood"] = "emotional"
    else:
        profile["last_mood"] = "neutral"
        
    state["user_profile"] = profile
    return state

def build_graph():
    
    graph_builder = StateGraph(State)
    


    

    
    graph_builder.add_node("classify_message", classify_message)
    graph_builder.add_node("route", route)
    graph_builder.add_node("logical_agent", logical_agent)
    graph_builder.add_node("emotional_agent", emotional_agent)
    graph_builder.add_node("sarcastic_agent", sarcastic_agent)
    graph_builder.add_node("angry_agent", angry_agent)
    graph_builder.add_node("motivational_agent", motivational_agent)
    graph_builder.add_node("update_mood", update_mood)
    graph_builder.add_node("humanlike", humanlike)
    

    graph_builder.add_edge(START, "classify_message")
    
    graph_builder.add_edge("classify_message", "route") 
    
    graph_builder.add_conditional_edges("route", route_path)
    graph_builder.add_edge("logical_agent", "update_mood")
    graph_builder.add_edge("emotional_agent", "update_mood")
    graph_builder.add_edge("sarcastic_agent", "update_mood")
    graph_builder.add_edge("angry_agent", "update_mood")
    graph_builder.add_edge("motivational_agent", "update_mood")
    
    graph_builder.add_edge("update_mood",END)

    return graph_builder.compile()
