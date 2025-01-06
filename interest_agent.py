from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from tools.interest import InterestTool
from utils import print_response

llm = ChatOllama(model="llama3.1:8b")
tool = InterestTool()
agent = create_react_agent(llm, [tool])

question = "with 2% monthly interest, I want to invest my 10K for 24 months. How much would I have after that time?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

question = "What would $7500 become with 5.25% monthly interest after 20 months?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

question = "Banka hesabımda 18,000 Türk Lirası var, aylık 0.75% faiz ile bir buçuk yıl sonra ne kadar param olur?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

question = "What would 4500 CHF become with 10% monthly interest after 9 months?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)

question = "What would 8000 become with 1.5% monthly interest after 3 years?"
print(question)
question_dict = {"messages": [HumanMessage(content=question)]}
response = agent.invoke(question_dict)
print_response(response)