import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000/process_query/"

st.title("AI Assistant")

query = st.text_input("Enter your question")

if st.button("Submit"):
    if query:
        response = requests.post(FASTAPI_URL, json={"query": query})
        
        if response.status_code == 200:
            result = response.json().get("response", "No response")
            st.subheader("Response:")
            st.write(result)
        else:
            st.error("Error: Could not retrieve response.")
    else:
        st.error("Please enter a query to get a response.")
