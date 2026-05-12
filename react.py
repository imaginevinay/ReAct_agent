from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
load_dotenv()

# define a triple tool
@tool
def triple(num:float) -> float:
    """
    param -> num: a number to triple (type: float)
    return : the triple of the input number (num) in float
    """
    return float(num) * 3

tools = [TavilySearch(max_results = 1), triple]

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0).bind_tools(tools)

