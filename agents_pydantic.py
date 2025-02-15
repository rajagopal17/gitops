import os
from dotenv import load_dotenv
load_dotenv()

#********************************************************************************** gemini_llm
gemini_api_key = os.getenv("GEMINI_API_KEY")
from google import genai

client      = genai.Client(api_key=gemini_api_key)
response    = client.models.generate_content(
                        model    ="gemini-2.0-flash", 
                        contents ="Explain how combustion engine works in 10 sentences."
                      )

gemini_response = response.candidates[0].content.model_dump()
print(gemini_response)

