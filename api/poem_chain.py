from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

def get_openai_chain():
    model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    prompt = ChatPromptTemplate.from_template("Write a poem about: {prompt}")
    chain = prompt | model | StrOutputParser()
    return chain

def get_ollama_chain():
    model = ChatOllama(model="llama3")
    prompt = ChatPromptTemplate.from_template("Write a poem about: {prompt}")
    chain = prompt | model | StrOutputParser()
    return chain
