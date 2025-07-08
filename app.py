from langchain_openai import ChatOpenAI
#from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
#Langsmith Trackingstr
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","""You are Cascade, a highly capable AI coding assistant 
"""),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title('Langchain Demo with Grok Api')
input_text=st.text_area("Search the topic you want")

#llm = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct')
llm = ChatOpenAI(model="deepseek/deepseek-chat-v3-0324:free",
                 base_url=os.environ["OPENAI_API_BASE"],
                 api_key=os.environ["OPENAI_API_KEY"])
output_parser=StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))