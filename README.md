This repository contains Python projects that I built while learning Python programming. Each project helped me practice different programming concepts and improve my problem-solving skills.
## Projects

1. Calculator App
2. Password Generator
3. Quiz Application
4. Expense Tracker
5. AI Chatbot (Ollama + Qwen)
6. AI Resume Analyzer

### 1. Calculator App
- Perform basic arithmetic operations
- Uses functions, user input, and conditional statements
### 2. Password Generator
- Generate random secure passwords
- Uses the `random` module, strings, and loops

### 3. Quiz Application
- Multiple-choice quiz
- Calculates the final score
- Uses lists, dictionaries, loops, and functions

### 4. Expense Tracker
- Add expenses
- View all expenses
- Calculate total expenses
- Search expenses
- Delete expenses
- Uses lists, dictionaries, loops, and input validation

## Technologies Used

- Python 3

### 5. AI Chatbot (Ollama + Qwen)

A command-line AI chatbot built with Python, Ollama, and the Qwen language model. The application allows users to have interactive conversations with a locally running Large Language Model (LLM) without relying on cloud APIs.

## Features

* Interactive command-line chat interface
* Conversation memory within the session
* Local AI inference using Ollama
* Natural language question answering
* Continuous chat loop until user exits
* Lightweight and easy to run

## Technologies Used

* Python
* Ollama
* Qwen 2.5 3B
* Lists and Dictionaries
* Loops and Conditional Statements

## How It Works

1. The user enters a message.
2. The message is sent to the Qwen model through Ollama.
3. The AI generates a response.
4. The conversation history is maintained for context.
5. The chat continues until the user chooses to exit.

## Installation

Install Ollama and pull the model:

```bash
ollama pull qwen2.5:3b
```

Install the Ollama Python package:

```bash
pip install ollama
```

## Usage

Run the chatbot:

```bash
python chatbot.py
```

Start chatting with the AI directly from the terminal.

## Learning Outcomes

* Working with Large Language Models (LLMs)
* Ollama Integration
* Chat Message Management
* Prompt Engineering
* Python Programming
* Building Conversational AI Applications

### 6. AI Resume Analyzer

AI Resume Analyzer is a command-line Python application that analyzes a resume against a job description using a local Large Language Model (LLM) through Ollama.

The application extracts text from a PDF resume, compares it with a job description, generates an ATS-style analysis report, and allows users to ask follow-up questions about their resume and career growth.

## Features

* PDF resume validation and processing
* Job description file validation
* Resume text extraction using PyPDF
* ATS-style resume analysis
* Match score generation
* Matching skills identification
* Missing skills detection
* Strengths and weaknesses analysis
* Resume improvement recommendations
* Interactive AI career counselor mode
* Corrupted PDF handling

## Technologies Used

* Python
* Ollama
* Qwen 2.5 3B
* PyPDF
* JSON
* File Handling
* Exception Handling

## Project Workflow

1. Upload a resume in PDF format.
2. Upload a job description in TXT format.
3. Extract text from the resume.
4. Analyze the resume against the job description.
5. Generate an ATS report containing:

   * Summary
   * Match Score
   * Matching Skills
   * Missing Skills
   * Strengths
   * Weaknesses
   * Recommendations
6. Ask follow-up questions about the resume and career path.

## Installation

Install the required packages:

```bash
pip install pypdf ollama
```

Make sure Ollama is installed and running locally.

## Usage

Run the application:

```bash
python CV_Analyzer.py
```

Provide:

* Resume file (.pdf)
* Job description file (.txt)

The application will generate an ATS report and allow interactive career-related questions.

## Example Output

* Resume Summary
* Match Score
* Matching Skills
* Missing Skills
* Strengths
* Weaknesses
* Recommendations

## Learning Outcomes

This project helped me practice:

* Python programming
* File handling
* Exception handling
* PDF processing
* JSON parsing
* Prompt engineering
* Working with Large Language Models (LLMs)
* Building command-line applications


## Purpose

This repository documents my Python learning journey and contains projects built while exploring programming, problem-solving, and AI development. I will continue adding new projects as I learn and grow my skills.
---
More projects coming soon.
## Author

Sameeha Ahmad
