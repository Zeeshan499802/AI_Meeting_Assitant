# Actionableitems, decision, questions

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import os

def get_llm():
    return ChatMistralAI(model="mistral-small-latest", mistral_api_key = os.getenv("MISTRAL_API_KEY"), temperature=0.2)

def build_chain(system_prompt: str):
    llm = get_llm()
    return (RunnablePassthrough() | RunnableLambda(lambda x: {"transcript": x}) | ChatPromptTemplate.from_messages([
        ("system", system_prompt), 
        ("human", "Extract the relevant information from the following meeting transcript:\n\n{transcript}")
    ]) | llm | StrOutputParser())

def extract_actionable_items(transcript: str) -> str:
    system_prompt = "You are a helpful assistant that extracts actionable items from meeting transcripts. Actionable items are specific tasks or follow-up actions that need to be completed after the meeting."
    chain = build_chain(system_prompt)
    return chain.invoke(transcript[:2000])

def extract_key_decisions(transcript: str) -> str:
    system_prompt = "You are a helpful assistant that extracts key decisions from meeting transcripts. Key decisions are important conclusions or agreements reached during the meeting."
    chain = build_chain(system_prompt)
    return chain.invoke(transcript[:2000])

def extract_questions(transcript: str) -> str:
    system_prompt = "You are a helpful assistant that extracts questions from meeting transcripts. Questions are inquiries or points of clarification raised during the meeting."
    chain = build_chain(system_prompt)
    return chain.invoke(transcript[:2000])

 