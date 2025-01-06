from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from tools.profit import MetalProfitTool
from utils import print_response

llm = ChatOllama(model="llama3.1:8b")
tool = MetalProfitTool()
agent = create_react_agent(llm, [tool])

# Example 1: Simple metal performance query
question = "What was gold's return in 2023?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

# Example 2: Comparison between two metals
question = "Compare the performance of silver and platinum for year 2022."
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

# Example 3: Performance query of less common metal
question = "How did palladium perform in 2021? Show me its price changes."
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

# Example 4: Multi-metal comparison
question = "Which metal had the best performance in 2023: gold, silver, or platinum?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)