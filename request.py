import requests

import json

 

url = "http://localhost:5000/rank"

payload = json.dumps({
      
    "query": "How to speedup LLMs?"
      })

headers = {

            'Content-Type': 'application/json'

            }

print(payload)
response = requests.request("post", url, headers=headers, data=payload)
print(response.text)
