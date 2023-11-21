import requests
import json

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "joe", "views":10},
        {"likes": 10, "name": "tim", "views":10000},
        {"likes": 47, "name": "Frank", "views":2000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
    
input()    
response = requests.delete(BASE + "videos/0")
print(response.json())
input()
response = requests.get(BASE + "video/2")
print(response.json()) 
