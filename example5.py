from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
def simple_prompt_template_example():
    llm = ChatOpenAI(model='gpt-5-mini', temperature=0)
    prompt_template= PromptTemplate.from_template(
        "Write a short joke about {topic} that is {style}"
    )
    print("Template:", prompt_template.template)
    print("Variable:",prompt_template.input_variables)
    
   


if __name__=='__main__':
    simple_prompt_template_example()
    