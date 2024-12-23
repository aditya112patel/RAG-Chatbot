﻿# RAG-Chatbot
This project integrates FastAPI as a backend for processing AI-based queries and Streamlit as a frontend for user interaction. The application allows users to submit queries, which are processed by a language model (LLM) and a classifier. Based on the input, the app either retrieves information from a pre-loaded document or generates a response directly using the LLM.

Features
FastAPI Backend:
Processes queries using a machine learning classifier to find whether to call the database or not.
Retrieves document-based answers using a Chroma Vector Database and Langchain for document handling.
Uses a Google Generative AI model (Gemini-1.5) to handle language generation for non-informational queries.
It also provide relevent links to youtube videos explain question related stuff.
Streamlit Frontend:
Provides an interactive web interface for users to submit their queries.
Displays the results returned by the FastAPI backend.
Technology Stack
FastAPI: Backend service to handle API requests and run the model logic.
Streamlit: Frontend framework for building interactive web applications.
Langchain: For handling document retrieval and processing.
Google Generative AI: For language model-based responses.
Chroma: Vector database used to store document embeddings for retrieval.
NLTK: For natural language processing, keyword extraction, and stopword removal.
Setup and Installation
Prerequisites
Ensure you have the following installed on your system:
