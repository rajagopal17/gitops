import ollama

def get_ollama_response(prompt: str, model: str = "deepseek-r1:7b") -> str:
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

# Example usage
prompt = "Explain the revenue recognition concept in accounting in 10 sentences."
ollama_response = get_ollama_response(prompt)
print(ollama_response)


import random

def generate_random_number(min_val: int = 0, max_val: int = 100) -> int:
    return random.randint(min_val, max_val)
