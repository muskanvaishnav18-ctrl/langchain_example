from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain.tools import tool
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

@tool
def calculator(expression: str)-> str:
    """ calculate mathematical expressions. Input should be a valid math expression like '2+2' ."""
    try:
        result=eval(expression)
        return f"The result is:{result}"

    except:
        return "Invalid Mathematical expression"
    

@tool
def text_length(text: str)-> str:
    """Count the number of character in a text string """
    return f"the text has {len(text)} Charactes"

def simple_agent():
    llm= ChatOpenAI(model='gpt-4', temperature=0)
    tools=[calculator,text_length]

    prompt= ChatPromptTemplate.from_messages(
        [
            ("system", """You are a helpful assistant with access to tools. Use them when needed"""),
             ("human","{input}"),
             MessagesPlaceholder(variable_name='agent_scratchpad')
        ]
    )

    agent =create_openai_functions_agent(llm,tools,prompt)
    agent_executor= AgentExecutor(agent= agent, tools = tools, verbose= True)

    print(" Agent with calculator and text length tools ready!")
    print("Try: 'What is 15*17 ' or 'How many character in hello world?' ")

    while True:
        user_input = input("Ask me something (or 'exit'):").strip()
        if user_input.lower()=='exit':
            break
        try:
            reponse = agent_executor.invoke({'input': user_input})
            print("Agent",reponse["output"])
            print()
        except Exception as e:
            print(f"Error: {e}")

if __name__ =="__main__":
    simple_agent()

    
