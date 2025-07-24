# AIVIS_MCP Workspace Guide

## Overview

This workspace provides a set of tools and demos for interacting with LLMs (Groq, Ollama), MCP tool servers, and n8n automation. It includes Python scripts, Streamlit apps, and server modules for math and weather tasks.

---

## 1. Prerequisites

- **Python 3.11+** (recommended)
- **Node.js & npm** (for n8n)
- **Ollama** (for local LLM inference)
- **Groq API Key** (for Groq cloud LLMs)

---

## 2. Setting Up Python Virtual Environment

1. Open a terminal in your project folder.
2. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```
3. Activate the environment:
    - **Windows:**
        ```sh
        .venv\Scripts\activate
        ```
    - **macOS/Linux:**
        ```sh
        source .venv/bin/activate
        ```
4. Upgrade pip:
    ```sh
    pip install --upgrade pip
    ```

---

## 3. Install Python Dependencies

Install all required packages from [`requirements.txt`](requirements.txt):

```sh
pip install -r requirements.txt
```

---

## 4. Setting Up Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY="your_groq_api_key_here"
```

Replace with your actual Groq API key.

---

## 5. Download & Install Ollama

Ollama is required for local LLM inference.

- Visit [https://ollama.com/download](https://ollama.com/download) and follow instructions for your OS.
- After installation, start Ollama:
    ```sh
    ollama serve
    ```
- Pull a model (example: llama3):
    ```sh
    ollama pull llama3
    ```

---

## 6. Running the Python Scripts

### Weather & Math MCP Servers

- **Weather Server:**  
  Run with:
  ```sh
  python server/weather.py
  ```
- **Math Server:**  
  Run with:
  ```sh
  python server/math_server.py
  ```

### MCP Client

- Run the client to interact with the weather server:
  ```sh
  python mcp_client.py
  ```

### Streamlit Apps

- **Groq Chatbot:**
  ```sh
  streamlit run streamlit_groq.py
  ```
- **Ollama Chatbot:**
  ```sh
  streamlit run ollama_frontend.py
  ```
- **n8n Test Chatbot:**
  ```sh
  streamlit run n8n_test.py
  ```

---

## 7. Using Jupyter Notebook

- Open [`groq.ipynb`](groq.ipynb) in Jupyter or VS Code.
- Run the cells to interact with Groq API.

---

## 8. Setting Up n8n Locally & Using the Provided Workflow

### Install n8n

1. **Install Node.js & npm**  
   Download and install Node.js from [https://nodejs.org/](https://nodejs.org/).

2. **Install n8n globally**  
   ```sh
   npm install -g n8n
   ```

3. **Start n8n**  
   ```sh
   n8n
   ```
   By default, n8n runs at [http://localhost:5678](http://localhost:5678).

---

### Import and Configure the Workflow

1. **Open n8n in your browser:**  
   Go to [http://localhost:5678](http://localhost:5678).

2. **Import the workflow template:**  
   - Click the menu (top right) → "Import workflow".
   - Copy the contents of `N8N_workflow_template.json` and paste it into the import dialog.
   - Click "Import".

3. **Configure Credentials:**
   - Set up your Ollama and SerpAPI credentials in n8n:
     - Go to "Credentials" in n8n.
     - Add your Ollama API and SerpAPI keys.
     - Make sure the credential names match those referenced in the workflow (`Ollama account`, `SerpAPI account`).

4. **Activate the workflow:**  
   - Click "Activate" to enable the workflow.

---

### How the Workflow Works

- **Webhook Trigger:**  
  The workflow listens for POST requests at `/webhook/invoke_agent`.  
  You can send messages to this endpoint (see `n8n_test.py` for an example).

- **AI Agent Node:**  
  Handles user queries, uses Ollama for LLM responses, and can access Google search via SerpAPI.

- **Memory & Tools:**  
  Includes a memory buffer and SerpAPI integration for enhanced responses.

---

### Example: Sending a Message to the Workflow

You can use the provided `n8n_test.py` Streamlit app to interact with the workflow, or send a POST request manually:

```sh
curl -X POST http://localhost:5678/webhook/invoke_agent \
  -H "Content-Type: application/json" \
  -d '{"sessionId": "your-session-id", "chatInput": "What is the weather in Delhi?"}'
```

---

**Tip:**  
If you change the workflow, export it from n8n to update your local `N8N_workflow_template.json`.

---

## 10. File Overview

- [`mcp_client.py`](mcp_client.py): Python client for MCP tool servers.
- [`streamlit_groq.py`](streamlit_groq.py): Streamlit app for Groq LLM chat.
- [`ollama_frontend.py`](ollama_frontend.py): Streamlit app for Ollama LLM chat.
- [`n8n_test.py`](n8n_test.py): Streamlit app for n8n webhook chat.
- [`server/weather.py`](server/weather.py): MCP weather tool server.
- [`server/math_server.py`](server/math_server.py): MCP math tool server.
- [`groq.ipynb`](groq.ipynb): Jupyter notebook for Groq API demo.

---

## 11. Troubleshooting

- Ensure `.venv` is activated before running Python scripts.
- Make sure Ollama is running for local LLM inference.
- Check `.env` for correct API keys.
- For n8n, ensure Node.js is installed and n8n