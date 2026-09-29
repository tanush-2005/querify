from langchain_community.tools import DuckDuckGoSearchRun, Tool
import wikipediaapi
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)


search = DuckDuckGoSearchRun()
search_tool = Tool (
    name = "search",
    func = search.run,
    description = "Search the web for information",
)


import requests
from langchain_core.tools import Tool


wiki = wikipediaapi.Wikipedia(
    user_agent="CodingAgent/1.0 (your-email@example.com)",
    language="en"
)

def wikipedia_search(query: str) -> str:
    page = wiki.page(query)

    if not page.exists():
        return f"No Wikipedia page found for: {query}"

    return page.summary


wiki_tool = Tool(
    name="wikipedia",
    func=wikipedia_search,
    description="Search Wikipedia for factual information about a topic."
)