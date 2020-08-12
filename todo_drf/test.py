import requests
import json
baseurl = "http://127.0.0.1:8000/"
endpoint = "api/task-create/"
headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk2NjI0MTIyLCJqdGkiOiJkZDJkYTM4MTYzYWU0YjdkODBiNWU2NzE2MGY0N2IxMyIsInVzZXJfaWQiOjF9.fTAlFQ76V-oEIonXgMi-2_-oX9PlmP7cbLWZ_PaAnYo"}
response = requests.post(baseurl+endpoint, data={"title":"hello"})
print(response.json())