from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
def simple_prompt_template_example():
    llm = ChatOpenAI(model='gpt-5-nano', temperature=0)
    prompt_template= PromptTemplate.from_template(
        "Write a short joke about {topic} that is {style}"
    )
    print("Template:", prompt_template.template)
    print("Variable:",prompt_template.input_variables)

    chain =prompt_template | llm

    print("Welcome to the Joke Genrator!")
    print("Type 'exit' to quit\n")

    while True:
        topic = input("Topic:").strip()
        if topic.lower() == 'exit':
            break
        style= input("Style:").strip()
        if style.lower() == 'exit':
            break

        try:
            response = chain.invoke({"topic":topic,"style":style})
            print(response.context)
            print()
        except KeyboardInterrupt:
            print("\n\ngoodbye!")
            break
        except Exception as e:
            print(f"Error:{e}")
    
   


if __name__=='__main__':
    simple_prompt_template_example()
    