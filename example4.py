from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
def chat_with_assistant():
    llm = ChatOpenAI(model='gpt-5-mini', temperature=0)
    memory= ConversationBufferMemory(return_messages=True)
    conversation = ConversationChain(llm=llm,memory=memory)
    print("Chat with memory enable! (Type 'exit'to quit)")
    while True:
        try:
            user_input=input("You:")
            if user_input.lower() in ['exit','quit']:
                print("Exiting the chat. Goodbye!")
                break
            # messages=[
            # ("system"," You are a helpful assistant"),
            # ("user",user_input)
            # ]  
            response= llm.invoke({"input":user_input})
            print("Assistant:",response.content)

        except Exception as e:
            print("Oops! Something went wrong:" ,e)
            break


if __name__=='__main__':
    chat_with_assistant()
    