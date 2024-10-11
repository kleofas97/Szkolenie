import requests
import os
from dotenv import load_dotenv

# Pobieranie zmiennych środowisk z pliku .env - po co? -> https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/
load_dotenv()

token = os.getenv("TOKEN")

url = f"https://data.fixer.io/api/latest?access_key={token}"  # jest wiele sposobów w jaki mozna dodac token.
#  Token moze tez byc jednorazowy albo wazny np. godzine

# wyslanie zapytania
response = requests.request("GET", url)
# rozpakowanie odpowiedzi
data = response.json()
# iteracja po odpowiedziach
for k, v in data.items():
    print(f"Klucz: {k}, wartosc: {v}")

# w innej wersji odczyt informacji
print(response.text)
# Zaleznie od tego co chcemy zrobić, jest kilka podstawowych metod w Requestach:
# Metoda GET służy do pobierania danych z serwera. Używana jest do uzyskiwania informacji z określonego zasobu.
# Metoda POST jest używana do wysyłania danych do serwera, na przykład w celu utworzenia nowego zasobu.
# itd. np. PATCH, PUT, OPTIONS

# wiecej info
# https://www.w3schools.com/python/module_requests.asp
