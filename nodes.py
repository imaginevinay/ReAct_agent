from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
# tool node is a node that rune the tools called in the last AI message
from react import llm,tools
load_dotenv()

SYSTEM_MSG="""
You are a helpful assistant that can use tools to answer user questions.
"""

def run_reasoning_agent(state:MessagesState)->MessagesState:
    """
    Run the agent reasoning node
    """
    response = llm.invoke([
        {
            "role": "system",
            "content": SYSTEM_MSG
        },
        *state["messages"]
    ])
    
    return {"messages": [response]}


tool_node = ToolNode(tools)

