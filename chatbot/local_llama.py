from langchain_openai import ChatOpenAI
#from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#Langsmith Trackingstr
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","""you should answer the question asked.
"""),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title('Langchain with local model')
input_text=st.text_area("Search the topic you want")

#llm = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct')
llm=Ollama(model='gemma3:1b')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text}))