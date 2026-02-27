import os
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv

# 1. Učitavamo tajne podatke iz .env fajla
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Provera da li je ključ uopšte tu (da ne pukne program kasnije)
if not api_key:
    print("Greška: API ključ nije pronađen! Proverite .env fajl.")
    exit()

# 2. Konfiguracija AI modela
genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-3-flash-preview')
chat = model.start_chat(history=[])

# 3. Podešavanje fajla za čuvanje razgovora
ime_fajla = f"razgovor_{datetime.now().strftime('%Y-%m-%d')}.txt"

print(f"\n--- AI Čet spreman (Automatsko logovanje ključa aktivno) ---")
print(f"Razgovor se čuva u: {ime_fajla}")

while True:
    pitanje = input("\nVi: ")
    
    if pitanje.lower() in ["izlaz", "exit"]:
        print("Doviđenja!")
        break

    try:
        # Slanje poruke modelu
        response = chat.send_message(pitanje)
        odgovor = response.text
        
        print(f"\nAI: {odgovor}")

        # Čuvanje razgovora u fajl
        with open(ime_fajla, "a", encoding="utf-8") as f:
            vreme = datetime.now().strftime("%H:%M:%S")
            f.write(f"[{vreme}] Vi: {pitanje}\n")
            f.write(f"[{vreme}] AI: {odgovor}\n")
            f.write("-" * 30 + "\n")
            
    except Exception as e:
        print(f"Došlo je do greške: {e}")