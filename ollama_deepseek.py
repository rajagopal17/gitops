import ollama

model1 ='deepscaler'
model2 ='deepseek-r1:7b'

def get_ollama_response(prompt: str, model: str = model1) -> str:
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

# Example usage
prompt = "Explain the revenue recognition concept in accounting in 10 sentences as per Indian GAAP"
ollama_response = get_ollama_response(prompt)
print(ollama_response)



