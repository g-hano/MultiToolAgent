from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from tools.interest import InterestTool
from tools.profit import MetalProfitTool
from utils import print_response

llm = ChatOllama(model="llama3.1:8b")
agent = create_react_agent(llm, [MetalProfitTool(), InterestTool()])

# Example 1: Comparing investment options
question = "What would give better returns: investing in gold for all of 2023, or putting money in a 3% monthly interest account for 12 months?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

# Example 2: Complex scenario
question = "If I had invested in silver during 2023 and earned 3000 dollars, and then put that profit in a 2% monthly interest account for 6 months, what would my final returns be?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)