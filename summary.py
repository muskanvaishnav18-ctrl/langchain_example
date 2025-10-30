from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv # pip install dotenv
load_dotenv()

def simple_prompt_template_example():
    llm =ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0)
    memory= ConversationBufferMemory(return_messages=True)
    conversation = ConversationChain(llm=llm,memory=memory)
    # prompt_template = PromptTemplate.from_template(
    # #     "write a summary about {topic} that is {style}."
    # #  )
    system_prompt = PromptTemplate(
        input_variables=["history","input"],
        template= """
        Previous conversation:{history}
        Current input:{input}"""

    )
    
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=system_prompt,
        verbose=True  # Optional: shows internal steps
    )
    prompt_template= PromptTemplate.from_template(
        "write a summary about {topic} that is {style}."
    )

    #intractive useer input loop
    print("Welcome to the Summary Generator!")
    print("type 'exit' to quit\n")
 
    
    
    while True:
        topic = input("You:").strip()
        if topic.lower() == "exit":
            break
 
        style = input("Style:").strip()
        if style.lower() == 'exit':
            break
        try:
            response = conversation.invoke({"you":topic,"style":style})
            print("Your Output:",response.content)
            print()
            # print(memory.buffer)
            # print(memory.load_memory_variables({})['history'])
            # print("------------------------------")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"error:{e}")



if __name__ == "__main__":
    simple_prompt_template_example()
