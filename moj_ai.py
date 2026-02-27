import os
from dotenv import load_dotenv
from google import genai

# 1. Učitavanje
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Podešavanje klijenta
client = genai.Client(api_key=api_key)

print("\n--- TVOJ AI MENTOR JE ONLINE ---")

while True:
    user_input = input("\nVi: ")
    if user_input.lower() in ['kraj', 'stop', 'izlaz']:
        print("Mentor: Srećno sa učenjem! Vidimo se uskoro.")
        break

    try:
        # Obriši onaj 'for' krug što smo dodali za listanje, više nam ne treba
        
        response = client.models.generate_content(
            model="gemini-2.5-flash", # Koristimo tačno ime sa tvog ekrana (bez models/ prefiksa često radi bolje)
            config={
                'system_instruction': "Ti si moj ljubazni Python mentor. Ohrabruj me i povremeno mi postavi po jedan mali zadatak.",
            },
            contents=user_input
        )
        print(f"\nMentor: {response.text}")
    except Exception as e:
        print(f"\nDošlo je do greške: {e}")