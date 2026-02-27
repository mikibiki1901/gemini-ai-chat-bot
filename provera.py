import os
from dotenv import load_dotenv

print("--- START TESTA ---")
load_dotenv()
kljuc = os.getenv("GEMINI_API_KEY")

if kljuc is None:
    print("REZULTAT: Python uopšte ne vidi .env fajl!")
elif kljuc == "":
    print("REZULTAT: .env fajl postoji, ali je ključ prazan!")
else:
    print(f"REZULTAT: Pronašao sam ključ: {kljuc[:5]}... (ukupno {len(kljuc)} znakova)")
print("--- KRAJ TESTA ---")