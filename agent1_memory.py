from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.tools import tool # tool decorator
from dotenv import load_dotenv
load_dotenv()

# Global storage for user preferences
user_preferences = {}

@tool
def save_user_preference(category: str, preference: str) -> str:
    """Save user preferences like favorite topics, writing style, etc."""
    user_preferences[category] = preference
    return f"Saved {category}: {preference}"

@tool
def get_user_preference(category: str) -> str:
    """Retrieve saved user preferences"""
    if category in user_preferences:
        return f"{category}: {user_preferences[category]}"
    return f"No preference saved for {category}"

@tool
def create_personalized_content(content_type: str, topic: str) -> str:
    """Create content based on user's saved preferences"""
    style = user_preferences.get('writing_style', 'default')
    return f"Create a {content_type} about {topic} in {style} style, considering user's preferences"

@tool
def list_all_preferences() -> str:
    """Show all saved user preferences"""
    if user_preferences:
        prefs = ", ".join([f"{k}: {v}" for k, v in user_preferences.items()])
        return f"Your saved preferences: {prefs}"
    return "No preferences saved yet"

def memory_agent_example():
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)
    
    tools = [save_user_preference, get_user_preference, create_personalized_content, list_all_preferences]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a smart assistant with memory and tools. You can:
        1. Remember user preferences and past conversations
        2. Save and retrieve user information
        3. Create personalized content based on saved preferences
        
        Use your tools wisely and remember context from previous interactions."""),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    # Memory management
    store = {}
    def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]
    
    agent_with_memory = RunnableWithMessageHistory(
        agent_executor,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )
    
    print("Smart Agent with Memory & Tools Ready!")
    print("Try: 'Save my writing style as casual' or 'Create a blog post about AI' or 'Show my preferences'")
    
    session_id = "user_session"
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            break
            
        try:
            response = agent_with_memory.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )
            print("Agent:", response["output"])
            print("-" * 50)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    memory_agent_example()