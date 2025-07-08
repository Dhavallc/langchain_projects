from fastapi import FastAPI
from api import poem_chain
from langserve import add_routes

app = FastAPI(title="Poem API via LangChain + LangServe")

# Add LangServe routes for each chain
add_routes(
    app,
    poem_chain.get_openai_chain(),
    path="/chains/openai"
)

add_routes(
    app,
    poem_chain.get_ollama_chain(),
    path="/chains/ollama"
)
