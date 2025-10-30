from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
def chat_with_assistant():
    llm = ChatOpenAI(model='gpt-5-mini', temperature=0)
    print("start Typing with the Assistant")
    while True:
        try:
            user_input=input("You:")
            if user_input.lower() in ['exit','quit']:
                print("Exiting the chat. Goodbye!")
                break
            messages=[
            ("system"," You are a helpful assistant"),
            ("user",user_input)
            ]  
            response= llm.invoke(messages)
            print("Assistant:",response.content)

        except Exception as e:
            print("Aome error occured :",e)
            break


if __name__=='__main__':
    chat_with_assistant()
    