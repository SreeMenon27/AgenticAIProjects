from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate(
    [
        ('system',"Please help me with the queries."),
        ('user','Question:{query}')
    ]
)

import streamlit as st
st.title("Chat Bot using Ollama")
input_text = st.text_input('Please type your query here.')

llm = Ollama(model='llama3.2')

output = StrOutputParser()

chain = prompt|llm|output

if input_text:
    st.write(chain.invoke({'query':input_text}))