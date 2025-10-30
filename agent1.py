from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

@tool
def write_blog_post(topic: str, length: str = "medium") -> str:
    """Write a blog post about a given topic. Length can be 'short', 'medium', or 'long'"""
    lengths = {"short": "2-3 paragraphs", "medium": "4-5 paragraphs", "long": "6-8 paragraphs"}
    return f"Generate a {lengths.get(length, 'medium')} blog post about {topic} with engaging introduction, main points, and conclusion."

@tool
def create_social_media_post(platform: str, topic: str) -> str:
    """Create social media content for different platforms. Platform can be 'twitter', 'linkedin', 'facebook', or 'instagram'"""
    platform_styles = {
        "twitter": "concise, hashtag-friendly, max 280 characters",
        "linkedin": "professional, engaging, business-focused",
        "facebook": "conversational, engaging, community-focused", 
        "instagram": "visual-friendly, trendy, hashtag-heavy"
    }
    style = platform_styles.get(platform.lower(), "engaging and appropriate")
    return f"Create a {style} post about {topic} for {platform}"

@tool
def generate_headline(topic: str, style: str = "catchy") -> str:
    """Generate headlines for articles or posts. Style can be 'catchy', 'professional', 'clickbait', or 'news'"""
    return f"Generate 3 {style} headlines about {topic}"

def content_generation_agent():
    # MUST USE A MORE CAPABLE MODEL LIKE GPT-4 FOR CONTENT GENERATION
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    
    tools = [write_blog_post, create_social_media_post, generate_headline]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a creative content generation assistant. Use the available tools to help create various types of content based on user requests."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    print("Content Generation Agent Ready!")
    print("Try: 'Write a blog post about AI' or 'Create a Twitter post about coffee' or 'Generate headlines for travel tips'")
    
    while True:
        user_input = input("What content do you need? (or 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break
            
        try:
            response = agent_executor.invoke({"input": user_input})
            print("Generated Content:")
            print(response["output"])
            print("-" * 50)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    content_generation_agent()