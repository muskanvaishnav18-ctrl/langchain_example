from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def simple_prompt_template_example():
    # Step 1: Initialize Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",  # Use a valid model name
        api_key=api_key,
        temperature=0
    )

    # Step 2: Setup memory
    memory = ConversationBufferMemory(return_messages=True)

    # Step 3: Create a prompt template compatible with ConversationChain
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template="""
        You are a helpful assistant. Keep your responses short and clear.

        Previous conversation:
        {history}

        User input:
        {input}

        Your response:
        """
    )

    # Step 4: Create the conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=True  # Optional: shows internal steps
    )

    # Step 5: Interactive loop
    print("Welcome to the Summary Generator!")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            response = conversation.run(user_input)
            print("Assistant:", response)
            print()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_prompt_template_example()