# LangChain Search Chatbot

## Overview
This project is a **Streamlit-based chatbot application** that integrates with LangChain to provide conversational search capabilities using tools like:

- **Arxiv API** for academic research articles.
- **Wikipedia API** for summarizing Wikipedia content.
- **DuckDuckGo** for general web searches.

It uses the `ChatGroq` model and `LangChain` tools to create a responsive, intelligent chatbot capable of retrieving, summarizing, and presenting relevant information from various sources.

---

## Features
- **Interactive Chat**: Users can interact with the chatbot in a Streamlit app interface.
- **Multi-source Search**: The bot leverages Arxiv, Wikipedia, and DuckDuckGo for comprehensive search results.
- **Customizable Settings**: Users can input their Groq API key via the sidebar.
- **Session Memory**: The bot retains conversational history for a seamless user experience.
- **Real-time Feedback**: Displays the agent's thought process and responses dynamically.

---

## Prerequisites
Before running the app, ensure you have the following installed:

- **Python** (>= 3.8)
- **Streamlit**
- **LangChain**
- **dotenv**

You also need a **Groq API Key** to use the `ChatGroq` model.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/langchain-search-chatbot.git
   cd langchain-search-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory to store your environment variables. Add your Groq API Key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

---

## How It Works
### Code Walkthrough

1. **Imports and Setup**:
   - Import necessary libraries, including `Streamlit`, `LangChain`, and API wrappers.
   - Load the environment variables using `dotenv`.

2. **Tool Initialization**:
   - `ArxivAPIWrapper` and `WikipediaAPIWrapper` are configured to retrieve a limited number of results and summarize them.
   - `DuckDuckGoSearchRun` enables general web search functionality.

3. **Streamlit UI**:
   - A sidebar collects the Groq API key.
   - A chat interface displays the conversation and takes user input.

4. **Chatbot Logic**:
   - A `ChatGroq` instance processes user input and generates responses.
   - An agent is initialized with the search tools using LangChain's `initialize_agent`.
   - The `StreamlitCallbackHandler` handles real-time visualization of the agent's reasoning and responses.

5. **Conversation Management**:
   - User inputs and bot responses are stored in `st.session_state` to maintain session history.

---

## Running the App
1. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (typically at `http://localhost:8501`).

3. Enter your Groq API key in the sidebar and start chatting!

---

## Example Queries
- **What is machine learning?**
- **Find recent research papers on quantum computing.**
- **Summarize the Wikipedia page for artificial intelligence.**

---

## Key Dependencies
- `Streamlit`: For building the web-based user interface.
- `LangChain`: For integrating language models and search tools.
- `langchain_community`: For community-contributed tools like Arxiv and Wikipedia wrappers.
- `dotenv`: For securely managing environment variables.

---

## Project Structure
```
langchain-search-chatbot/
├── app.py          # Main application code
├── requirements.txt # Python dependencies
├── .env             # Environment variables (not committed)
└── README.md        # Documentation
```

---

## Future Improvements
- Add support for additional APIs and tools.
- Enhance UI with more customization options.
- Implement user authentication for secure API key handling.

---

## Acknowledgments
This project is inspired by the [LangChain](https://github.com/hwchase17/langchain) library and its integration with Streamlit.
