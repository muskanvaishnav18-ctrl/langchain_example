from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv
load_dotenv()



def chat_with_memory():
    llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
    memory= ConversationBufferMemory(return_messages=True)

    system_prompt = PromptTemplate(
        input_variables=["history","input"],
        template= """You are a helpful AI assistant . Pleasee keep your reponse 
        concise and to the point.
        Aim for brief, clear answer without unnecessary elaboration.
        
        
        Previous conversation:
        {history}

        Current input: {input}
        please provide a brief and helpful reponse:"""

    )

    conversation= ConversationChain(
        llm=llm,
        memory=memory,
        prompt= system_prompt

    )

    print("Chat with memory enable!( Type 'exit to quit)")


    while True:
        try:
            user_input= input("You:").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            response = conversation.run(user_input)
            print("Assistant:", response)
        except Exception as e:
            print("Oops! Something wnt wrong:", e)

if __name__=="__main__":
    chat_with_memory()
