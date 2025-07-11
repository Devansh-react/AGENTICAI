from typing_extensions import TypedDict, Literal
from utilities.LLM_init import llm
from pydantic import BaseModel, Field
from Schema.models import State

class MessageClassifier(BaseModel):
    message: Literal["emotional", "logical","sarcastic","angry","motivational" , "Humanlike"] = Field(
        ..., description="Classify the user message upon the following catagory "
    )
    
def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)

    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as either:
            'humanlike':for normal humam like response eg hi hello how are you
            - 'emotional': for emotional support
            - 'logical': for factual/logical queries
            - 'sarcastic': witty assistant that responds sarcastically
            - 'angry': calm down the user and ask to take deep breath 
            - 'motivational': praise the user and ask to keep moving forward
            also analyse the user's language and aswer in that language only eg. is user ask in hindi answer in hindi onloy , id chinese answer in chinese only etc.
            """
        },
        {"role": "user", "content": last_message.content}
    ])
    return {
        "message_type": result.message,
        "type": result.message 
    }
    
