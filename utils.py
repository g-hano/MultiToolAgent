from langchain_core.messages import AIMessage
import json
from colorama import Fore, init
init(autoreset=True)

def print_response(response):
    tool_used = [tm for tm in response["messages"] if type(tm) == AIMessage]
    for tool_msg in tool_used:
        message = tool_msg.response_metadata["message"]
        if "tool_calls" in message:
            print()
            for tool_calls in message["tool_calls"]:
                print(Fore.GREEN + json.dumps(tool_calls, indent=4))
    print(response["messages"][-1].content)
    print("-"*20, end="\n\n")