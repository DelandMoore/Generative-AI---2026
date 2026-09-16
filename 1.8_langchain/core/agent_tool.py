from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from config import DEFAULT_MODEL, TAVILY
from dotenv import load_dotenv

load_dotenv()
web_search = TavilySearch(
    max_results = 5,
    topic = "general"
)

#testing 
# result = web_search.invoke({"query": "latest news on AI  IN Africa"})
# print(result)

@tool
def tavily_search(query: str) -> str:
    """Search the web using TavilySearch."""
    result = web_search.invoke({"query": query})
    return str(result)