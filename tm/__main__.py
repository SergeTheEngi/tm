from __init__ import *

test = requests.get('http://localhost:11434')
print(test.text,"\n")

from litellm import completion

response = completion(
    model = "ollama/qwen2.5-coder:7b",
    messages = [{
        "content": 'You are a banana.',
        "role": "user",
    },{
        "content": "I'm a banana. What I can do for you?",
        "role": "assistant",
    },{
        "content": "Describe this conversation from your standpoint",
        "role": "user",
    }],
    api_base = "http://localhost:11434",
)
    #prompt = "[INST] You are a banana. Describe what you can do. [/INST]",

separator = "\n---\n"
for m in response.choices:
    print(m['message']['content'],separator)
