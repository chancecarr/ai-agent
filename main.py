import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

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
        messages=messages
    )
    return response

def print_metrics(response):
    usage = response.usage
    if usage is None: raise RuntimeError("unable to get usage metrics")
    print(f"Prompt tokens: {usage.prompt_tokens}")
    print(f"Response tokens: {usage.completion_tokens}")

def main():
    if args.verbose: print(f"User prompt: {args.user_prompt}")
    messages = [
        {"role": "user", "content": args.user_prompt}
    ]
    response = generate_content(client, messages)
    if args.verbose: print_metrics(response)
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
