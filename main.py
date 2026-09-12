import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
import json

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None: raise RuntimeError("openrouter api key not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

def generate_content(client, messages):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    return response

def print_metrics(response):
    usage = response.usage
    if usage is None: raise RuntimeError("unable to get usage metrics")
    print(f"Prompt tokens: {usage.prompt_tokens}")
    print(f"Response tokens: {usage.completion_tokens}")

def main():
    if args.verbose: 
        print(f"System prompt: {system_prompt}")
        print(f"User prompt: {args.user_prompt}")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    for _ in range(20):
        response = generate_content(client, messages)
        if args.verbose: print_metrics(response)
        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls is not None and message.tool_calls != []:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)
                if result_message["content"] == "": raise Exception("Empty result")
                if args.verbose:
                    print(f"-> {result_message["content"]}")
        else:
            print(message.content)
            return
    print("Maximum number of iterations exceeded")
    exit(1)



if __name__ == "__main__":
    main()
