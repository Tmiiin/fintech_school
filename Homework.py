import requests

response = requests.get("https://api.github.com/users/Tmiiin")

assert response.text != 0
