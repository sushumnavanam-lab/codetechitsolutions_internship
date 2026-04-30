# AI Chatbot with NLP

## Overview
This project is part of Internship Task‑3: AI Chatbot with NLP.  
It is a simple chatbot built using Flask, HTML, CSS, and Python dictionaries.  

The chatbot demonstrates:
- Basic Q&A responses
- Country and state information
- Study roadmap guidance
- Spam detection
- Fuzzy matching for typos

---

## Requirements
Dependencies are listed in requirements.txt:
- Flask
- nltk

---

## Installation
Install all dependencies at once:
pip install -r requirements.txt

Or install them directly:
pip install Flask==3.0.0
pip install nltk==3.8.1

---

## Running the Project
Start the Flask server:
flask run

Open your browser at:
http://127.0.0.1:5000

---

## Features
- Q&A → Handles simple questions like “What is Python?”
- Geography info → Provides country/state details
- Roadmap → Guides learning paths for web development and AI
- Spam filter → Blocks inputs with spam keywords
- Fuzzy matching → Corrects typos and near matches
