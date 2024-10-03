import os
import pickle
import nltk
import string
from fastapi import FastAPI, Form
from pydantic import BaseModel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import uvicorn
from youtubesearchpython import VideosSearch

app = FastAPI()

os.environ["GOOGLE_API_KEY"] = "AIzaSyAR49C0ctufga3-lkIKDn2f7YqXjaZOH4k"

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# nltk.download('punkt')
# nltk.download('stopwords')

def extract_keywords(prompt):
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)
    words = word_tokenize(prompt.lower())
    keywords = [word for word in words if word not in stop_words and word not in punctuation]
    return keywords

def doc_loader(path):
    loader = PyPDFLoader(path)
    pages = loader.load()
    return pages


classifier = pickle.load(open('classifier_model.sav', 'rb'))
vectorizer = pickle.load(open('vectorizer.sav', 'rb'))

document = doc_loader('docs/iesc111.pdf')
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(document)
db = Chroma.from_documents(documents, embeddings)
retriever = db.as_retriever(search_kwargs={"k": 5})


template = """
You are a helpful AI assistant.
Answer based on the context provided. 
context: {context}
input: {input}
answer:
"""
prompt_template = PromptTemplate.from_template(template)
combine_docs_chain = create_stuff_documents_chain(llm, prompt_template)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)


class QueryInput(BaseModel):
    query: str


@app.post("/process_query/")
async def process_query(query: QueryInput):
    arr = extract_keywords(query.query)
    prompt = ' '.join(arr)

    prompt_vec = vectorizer.transform([prompt])
    check = classifier.predict(prompt_vec)

    if check == 1:
        response = '[From Database] '+retrieval_chain.invoke({"input": query.query})['answer']
        links=VideosSearch(query.query, limit = 2)
        response=response+'\n'+'Related links:'
        response=response+'\n'+links.result()["result"][0]['link']
    else:
        response = '[From LLM] '+llm.invoke(query.query).content

    return {"response": response}

#uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
