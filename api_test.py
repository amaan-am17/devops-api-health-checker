import requests
try:
    response = requests.get("https://httpbin.org/get")
    response.raise_for_status()
    data = response.json()  
except requests.RequestException as e:
    print("API request failed")
    print("Reason:", e)
else:
    print("Status code:", response.status_code)
    print("Health: HEALTHY")