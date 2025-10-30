from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

class PersonInfor(BaseModel):

    name: str = Field(description="person's full name")
    age: int= Field(description="person's age in years")
    occupation: str = Field(description="person's job or profession")
def json_parse_example():
    llm= ChatOpenAI(model='gpt-5-nano', temperature=0)
    parser =JsonOutputParser(pydantic_object= PersonInfor)

    prompt= PromptTemplate.from_template(
        "Extract person information from this text : {text}\n{format_instructions}"

    ).partial(format_instructions = parser.get_format_instructions)

    chain = prompt| llm | parser

    while True:
        text= input("Enter text with person info(or 'exit):").strip()
        if text.lower()=='exit':
            break
        try:
            result =chain.invoke({"text":text})
            print("Parsed JSON")
            print(f"Age : {result['name']}")
            print(f"Occupation:{result['occupation']}")
            print()

        except Exception as e:
            print(f"Error: {e}")


if __name__=="__main__":
    json_parse_example()