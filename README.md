# Querify: AI Research Agent

An AI-powered research assistant built with **LangChain** and **Google Gemini**. Give it any topic and it autonomously decides which tools to use (web search, Wikipedia, file saving), gathers information, and returns a clean, **structured research summary** with sources.

---

## Features

- **Autonomous tool selection** - the agent decides when to search the web, look up Wikipedia, or save results.
- **Structured output** - responses are validated with Pydantic into a consistent format (topic, summary, sources, tools used).
- **Web search** - real-time information via DuckDuckGo (no API key needed).
- **Wikipedia lookup** - reliable factual summaries for well-known topics.
- **Save to file** - research results are appended to `research_output.txt` with a timestamp.
- **Transparent reasoning** - verbose mode shows every step the agent takes.

---

## How It Works

```
User query
    │
    ▼
Gemini LLM (tool-calling agent)
    │
    ├── search            → DuckDuckGo web search
    ├── wikipedia         → Wikipedia summary
    └── save_text_to_file → writes results to research_output.txt
    │
    ▼
PydanticOutputParser
    │
    ▼
ResearchResponse { topic, summary, sources, tools_used }
```

The agent is created with LangChain's `create_tool_calling_agent` and run through an `AgentExecutor`. The system prompt instructs the model to return its final answer in a strict JSON format, which is then parsed into a typed Pydantic model.

---

## Project Structure

```
agent ai/
├── main.py            # Agent setup, prompt, output parser, and entry point
├── tools.py           # Custom tools: web search, Wikipedia, save-to-file
└── requirements.txt   # Python dependencies
```

---

## Tech Stack

| Component        | Technology                          |
| ---------------- | ----------------------------------- |
| Language         | Python 3.10+                        |
| Agent framework  | LangChain                           |
| LLM              | Google Gemini 3.5 Flash (`langchain-google-genai`) |
| Data validation  | Pydantic                            |
| Web search       | DuckDuckGo (`ddgs`)                 |
| Knowledge source | Wikipedia (`wikipedia-api`)         |
| Config           | `python-dotenv`                     |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/querify.git
cd querify
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey), then create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the agent

```bash
python main.py
```

---

## Example

**Input**

```
What can I help you research? > Impact of solar energy in India
```

**Output**

```python
topic='Impact of solar energy in India'
summary='India has rapidly expanded its solar capacity ...'
sources=['https://en.wikipedia.org/wiki/Solar_power_in_India', '...']
tools_used=['search', 'wikipedia']
```

If the agent uses the save tool, the full result is also appended to `research_output.txt`.

---

## Configuration

- **Change the model** - the project uses Gemini 3.5 Flash by default. To switch, edit the `model` argument in `main.py`:
  ```python
  llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
  ```
- **Wikipedia user agent** - in `tools.py`, replace the placeholder email in `user_agent` with your own contact (Wikipedia's API policy asks for this).
- **Turn off step-by-step logs** - set `verbose=False` in `AgentExecutor`.

---

## Roadmap

- [ ] Conversation memory for follow-up questions
- [ ] Web UI (Streamlit / Gradio)
- [ ] Export reports as PDF / Markdown
- [ ] Add more tools (arXiv, news APIs, page scraping)
- [ ] Source citations with inline references

---

## Contributing

Contributions are welcome! Fork the repo, create a feature branch, and open a pull request.

---

## License

This project is licensed under the MIT License.
