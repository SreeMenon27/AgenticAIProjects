# %%
import os
from dotenv import load_dotenv
load_dotenv()

# %%
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# %%
from langchain_community.document_loaders import PyPDFLoader
pdfloader = PyPDFLoader("storytelling-with-data.pdf")
pages = pdfloader.load_and_split()


# %%
pages[10]

# %%
from langchain_text_splitters import RecursiveCharacterTextSplitter
textsplitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=200)
documents = textsplitter.split_documents(pages)
documents[10]

# %%
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# %%
from langchain_community.vectorstores import FAISS
vector_db = FAISS.from_documents(documents,embeddings)

# %%
vector_db

# %%
query = "Summarize the main points of the pdf using bullet points. Be as precise as possible."
result = vector_db.similarity_search(query)


# %%
print(result[0].page_content)


