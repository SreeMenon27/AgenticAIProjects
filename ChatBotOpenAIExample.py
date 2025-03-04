import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages(
  [
    ("system","Please provide me answers to the queries."),
    ('user','Question:{query}')
  ]
)

#streamlit framework
import streamlit as st
st.title("Chat Bot using Open AI")
input_text = st.text_input('Please enter your query here')

#llm
llm = ChatOpenAI(model = "gpt-3.5-turbo")

#output parser
output = StrOutputParser()

#chain

chain = prompt|llm|output

if input_text:
    st.write(chain.invoke({'query':input_text}))
