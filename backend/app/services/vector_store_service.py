import weaviate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from app.config.settings import OPENAI_API_KEY, WEAVIATE_URL

client = weaviate.Client(url=WEAVIATE_URL)
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
llm = OpenAI(openai_api_key=OPENAI_API_KEY)


def store_transcription(text: str):
    vector_store = Weaviate(client, index_name="Transcriptions", embedding=embeddings)
    vector_store.add_texts([text])


def query_knowledge_base(query: str) -> str:
    vector_store = Weaviate(client, index_name="Transcriptions", embedding=embeddings)
    retriever = vector_store.as_retriever()
    qa = RetrievalQA(llm=llm, retriever=retriever)
    return qa.run(query)
