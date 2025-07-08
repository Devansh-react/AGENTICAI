from typing_extensions import TypedDict, Literal
from utilities.LLM_init import llm
from pydantic import BaseModel, Field
from Schema.models import State

class MessageClassifier(BaseModel):
    message: Literal["emotional", "logical","sarcastic","angry","motivational"] = Field(
        ..., description="Classify the user message"
    )
    
def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)

    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as either:
            - 'emotional': for emotional support
            - 'logical': for factual/logical queries
            - 'sarcastic': witty assistant that responds sarcastically
            - 'angry': calm down the user and ask to take deep breath 
            - 'motivational': praise the user and ask to keep moving forward
            """
        },
        {"role": "user", "content": last_message.content}
    ])
    return {
        "message_type": result.message,
        "type": result.message 
    }
    
