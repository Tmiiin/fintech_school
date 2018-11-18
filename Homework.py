import requests

response = requests.get("https://api.github.com/users/Tmiiin")

assert response.status_code == 200
