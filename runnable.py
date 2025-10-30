from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
 
from dotenv import load_dotenv
load_dotenv()
 
def chat_with_memory_updated():
    # Initialize ChatOpenAI LLM
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    
    # Create a prompt template with message history placeholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are my helpful assistant. Keep your conversations concise, informative and to the point. Do not talk much. User is chatting with you from mobile device."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    # Create the chain (prompt + llm)
    chain = prompt | llm
    
    # Store for session histories
    store = {}
    
    def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]
    
    # Create RunnableWithMessageHistory with the chain and session history function
    conversation = RunnableWithMessageHistory(
        runnable=chain,
        get_session_history=get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    print("Chat with memory enabled! (Type 'exit' to quit)")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            # Invoke with session configuration
            response = conversation.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": "default_session"}}
            )
            
            print("Assistant:", response.content)
            
        except Exception as e:
            print("Oops! Something went wrong:", e)
 
if __name__ == "__main__":
    chat_with_memory_updated()