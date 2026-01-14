import requests
import time

# Konfiguracja
API_URL = "http://127.0.0.1:8000/analyze"
IMAGE_PATH = "klasa.jpeg"  #zdjecie
LICEBA_ZADAN = 1000 

print(f"Rozpoczynam wysyłanie {LICEBA_ZADAN} zadań do API...")

start_time = time.time()

for i in range(LICEBA_ZADAN):
    try:
        
        response = requests.get(f"{API_URL}?path={IMAGE_PATH}")
        
        if response.status_code == 200:
            if i % 100 == 0:
                print(f"Wysłano: {i} zadań...")
        else:
            print(f"Błąd przy zadaniu {i}: {response.status_code}")
            
    except Exception as e:
        print(f"Błąd połączenia: {e}")
        break

end_time = time.time()
total_time = end_time - start_time

print("--- KONIEC TESTU ---")
print(f"Wysłano łącznie: {LICEBA_ZADAN} zadań")
print(f"Czas wysyłania: {total_time:.2f} sekund")
