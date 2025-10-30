from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv


load_dotenv()
def translator_app():
    
    llm = ChatGoogleGenerativeAI( model="gemini-pro", temperature=0)
    memory= ConversationBufferMemory(return_messages=True)
    
    prompt = PromptTemplate(
            input_variables=["input", "language"],
            template="Translate the following sentence to {language}:\n\n{input}"
        )

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=True 
    )   
    print("Welcome to the Translator!")
    print("Type 'exit' to quit.\n")

    while True:
        input_text = input("Enter text in English: ").strip()
        if input_text.lower() == "exit":
            print("Goodbye!")
            break 
        
        target_language = input("Translate to which language? ").strip()
        if target_language.lower() == "exit":
            print("Goodbye!")
            break
        try:
            response = conversation.invoke({
                "input": input_text,
                "language": target_language
            })
            print(f"{target_language.capitalize()} Translation:", response["response"])
            print()


        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    translator_app()