from typing import Annotated 
from typing_extensions import TypedDict, Literal , Dict
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field


class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None
    type : str|None
    user_profile: Dict[str, str] 

