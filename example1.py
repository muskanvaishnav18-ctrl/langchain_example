# # os.eviron.items()
# # print(os.environ.get("OpenAI_API_Key"))
# # print(os.environ.get("Gemini_API_Key"))
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv()

# Optional: Check if API key is loaded
# print("API Key:", os.getenv("OPENAI_API_KEY"))
def main():
    llm = ChatOpenAI(model='gpt-5-mini', temperature=0)

    messages=[
    ("system"," You are a helpful assistant"),
    ("user","Hello")
    ]  
    response= llm.invoke(messages)
    print("Assistant:",response.content)


if __name__=='__main__':
    main()
    