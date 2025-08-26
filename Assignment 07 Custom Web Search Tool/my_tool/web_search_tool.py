from tavily import TavilyClient
from agents import function_tool

tavily_client = TavilyClient("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")

@function_tool
def web_search_tool(query: str) -> str:
    """
    Search the web using Tavily API and return summarized results.
    """
    print("🔍 Searching the web...")
    results = tavily_client.search(query)
    return str(results)
