import requests

response = requests.get("https://cat-fact.herokuapp.com/facts/random") # Usuarios da internet colocam as curiosidades sobre gatos

if response.status_code == 200:
    data = response.json()
    print("Fato sobre gato:", data["text"])
else:
    print("Não foi possível obter um fato sobre gato.")

