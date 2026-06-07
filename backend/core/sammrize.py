from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

import os

def get_llm():
    return ChatMistralAI(model="mistral-small-latest", mistral_api_key = os.getenv("MISTRAL_API_KEY"), temperature=0.3)

def split_transcript(transcript: str) -> list:
    splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
    return splitter.split_text(transcript)  

def summarize(transcript: str) -> str:
    llm = get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that summarizes meeting transcripts."),
        ("human", "Summarize the following meeting transcript in a concise manner, highlighting key points and action items:\n\n{transcript}")
     ])
    map_chain = prompt | llm | StrOutputParser()
    chunks = split_transcript(transcript)

    chunk_summaries = [map_chain.invoke({"transcript": chunk}) for chunk in chunks]

    combined = "\n\n".join(chunk_summaries)

    combine_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that combines summaries of meeting transcripts into a single concise summary."),
        ("human", "Combine the following summaries into a single concise summary, ensuring that key points and action items are clearly highlighted:\n\n{transcript}")
    ])

    combined_summary = (RunnablePassthrough() | RunnableLambda(lambda x: {"transcript":x}) | combine_prompt | llm | StrOutputParser())
    return combined_summary.invoke(combined)

def generate_title(transcript: str) -> str:
    llm = get_llm()
    title_chain = (
        RunnablePassthrough() | RunnableLambda(lambda x: {"transcript": x}) | ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that generates concise and descriptive titles for meeting transcripts."),
            ("human", "Generate a concise and descriptive title for the following meeting transcript:\n\n{transcript}")
        ]) | llm | StrOutputParser())
    
    return title_chain.invoke(transcript[:2000])