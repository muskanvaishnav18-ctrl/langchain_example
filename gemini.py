from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv # pip install dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
def simple_prompt_template_example():
    llm =ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key= api_key,temperature=0)
 
    prompt_template = PromptTemplate.from_template(
        "write a summary about {topic} that is {style}."
     )
 
    print("Template:" , prompt_template.template)
    print("variables:", prompt_template.input_variables)
 
    chain = prompt_template | llm
 
    #intractive useer input loop
    print("Welcome to the Summary Generator!")
    print("type 'exit' to quit\n")
 

    while True:
        topic = input("Topic:").strip()
        if topic.lower() == "exit":
            break
 
        style = input("Style:").strip()
        if style.lower() == 'exit':
            break
        try:
            response = chain.invoke({"topic":topic,"style":style})
            print("Your Output:",response.content)
            print()
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"error:{e}")



if __name__ == "__main__":
    simple_prompt_template_example()
