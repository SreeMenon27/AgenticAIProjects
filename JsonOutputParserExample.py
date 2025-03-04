# %%
import os
from dotenv import load_dotenv
load_dotenv()


# %%
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# %%
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model = "gpt-4o")

# %%
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
[
    ("system","I am doing a geography project. I want to get the {state_name} and their {capital_name} for {country_name}. Please provide me the list in json format."),
    ("user","{my_query}")
]
)

# %%
from langchain_core.output_parsers import JsonOutputParser
output_parser = JsonOutputParser()

my_prompt_attributes = {
    "state_name":"state",
    "capital_name":"capital",
    "country_name":"India",    
    "my_query":"Can you please help me with the list in json format."
}

chain = prompt|llm|output_parser
result = chain.invoke(my_prompt_attributes)
result

# %%
import json

# %%
#data = json.loads(result)
for item in result:
    print(f"State: {item['state']}, Capital: {item['capital']}")


