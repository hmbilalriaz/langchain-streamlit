import streamlit as st
from langchain_ollama import ChatOllama

# Initialize the ChatOllama model
chat_model = ChatOllama(model="deepseek-r1:latest",
                        temperature=0)

# Streamlit app
st.title("Chat with Ollama")

# User input
user_input = st.text_input(label="Enter your query")

# Submit button
if st.button(label="Ask LLM", type="primary"):
    with st.container(border=True):
        with st.spinner(text="Generating response"):
            try:
                # Get response from llm
                response = chat_model.invoke(user_input)
                # Display it
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")
                st.stop()
                