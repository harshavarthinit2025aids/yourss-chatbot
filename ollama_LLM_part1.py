import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

st.title("YOURSS CHATBOT")
input_txt = st.text_input("please enter your queries here...")

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful AI assistant. your name is Yoursevagan"),
    ("user", "user query:{query}")
])

# Uses GROQ_API_KEY from Streamlit Secrets
llm = ChatGroq(model="llama-3.1-8b-instant")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_txt:
    st.write(chain.invoke({"query": input_txt}))
