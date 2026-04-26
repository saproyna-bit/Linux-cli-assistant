
  
import requests
import os

API_KEY = "Enter your API key here"
def ask_ai(task):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a Linux assistant running inside a proot Debian en>
            {"role": "user", "content": task}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        result = response.json()
        output = result['choices'][0]['message']['content'].strip()

        # CLEAN OUTPUT
        output = output.replace("```bash", "").replace("```", "").strip()
        output = output.split("\n")[0]  # take first line only

        return output

    except:
        print("DEBUG:", response.text)
        return "Error from API"
print("=== AI Agent (SAFE MODE) ===")
while True:
    current_path = os.getcwd()

    task = input(f"\n{current_path} $ ")

    command = ask_ai(task)

    print("\nAI suggests:", command)

    confirm = input("Run this command? (y/n): ")

    if confirm.lower() == 'y':
        os.system(command)
