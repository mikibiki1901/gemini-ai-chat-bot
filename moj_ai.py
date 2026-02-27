import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("\n--- TVOJ AI MENTOR JE ONLINE ---")

while True:
    user_input = input("\nVi: ")
    if user_input.lower() in ['kraj', 'stop', 'izlaz']:
        print("Mentor: Srećno sa učenjem! Vidimo se uskoro.")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            config={
                'system_instruction': "Ti si moj ljubazni Python mentor. Ohrabruj me i povremeno mi postavi po jedan mali zadatak.",
            },
            contents=user_input
        )
        print(f"\nMentor: {response.text}")
    except Exception as e:
        print(f"\nDošlo je do greške: {e}")