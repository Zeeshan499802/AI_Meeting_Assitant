import os
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from core.vector_store import load_vector_store, get_retriever, build_vector_store


def get_llm():
    return ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=os.getenv("MISTRAL_API_KEY"),
        temperature=0.3
    )


def format_docs(docs):
    return "\n\n".join(
        [f"Chunk {doc.metadata['chunk_index']}:\n{doc.page_content}" for doc in docs]
    )


def build_rag_chain(transcript: str):
    vector_store = build_vector_store(transcript)
    retriever = get_retriever(vector_store)
    llm = get_llm()

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant using meeting transcript chunks."),

        ("human",
         "Context:\n{context}\n\n"
         "Question:\n{question}")
    ])

    # 🔥 FIXED PIPELINE (IMPORTANT CHANGE)
    rag_chain = (
        RunnablePassthrough()  # keeps input dict
        | RunnableLambda(lambda x: {
            "context": retriever.invoke(x["question"]),
            "question": x["question"]
        })
        | RunnableLambda(lambda x: {
            "context": format_docs(x["context"]),
            "question": x["question"]
        })
        | prompt_template
        | llm
        | StrOutputParser()
    )

    return rag_chain


def load_rag_chain():
    vector_store = load_vector_store()
    retriever = get_retriever(vector_store)
    llm = get_llm()

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant using meeting transcript chunks."),

        ("human",
         "Context:\n{context}\n\n"
         "Question:\n{question}")
    ])

    rag_chain = (
        RunnablePassthrough()
        | RunnableLambda(lambda x: {
            # "context": retriever.get_relevant_documents(x["question"]),
            "context": retriever.invoke(x["question"]), 
            "question": x["question"]
        })
        | RunnableLambda(lambda x: {
            "context": format_docs(x["context"]),
            "question": x["question"]
        })
        | prompt_template
        | llm
        | StrOutputParser()
    )

    return rag_chain


def ask_question(rag_chain, question: str):
    print("Question:", question)
    return rag_chain.invoke({"question": question})