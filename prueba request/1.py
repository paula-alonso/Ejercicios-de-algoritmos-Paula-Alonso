from urllib import request
import requests
res = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
data = requests.get(res)
if data.status_code == 200:
    equipo= data.json()

for i in equipo:
    print(i["fifa_code"])