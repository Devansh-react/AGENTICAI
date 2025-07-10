from langchain_community.chat_message_histories import PostgresChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()

connection = os.getenv("DATABASE_URL")


def get_history(session_id: str):
    return PostgresChatMessageHistory(
        connection_string= connection,
        session_id=session_id,
        table_name="chat_messages"  
    )
    