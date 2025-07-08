from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage  
from typing import Annotated
from typing_extensions import TypedDict, Literal
from langgraph.graph import StateGraph, END, START

from Graph.graph_builder import build_graph
from langchain_core.messages import HumanMessage


def runbot():
    bot_graph = build_graph()
    state = {
        "messages": [],
        "message_type": None,
        "type": None
    }

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Thanks for chatting.")
            break

        state["messages"] += [HumanMessage(content=user_input)]
        state = bot_graph.invoke(state)
        
        if state.get("messages"):
            last_msg = state["messages"][-1]
            if isinstance(last_msg, dict):
                print("Assistant:", last_msg.get("content"))
            else:
                print("Assistant:", last_msg.content)


if __name__ == "__main__":
    runbot()
