import requests
print("=================")
print("API HEALTH CHECK")
print("=================")
url = "https://httpbin.org/get"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print("URL:", url)
    print("API request failed")
    print("Reason:", e)
    print("Health: UNHEALTHY")
else:
    print("URL:", url)
    print("Status Code:", response.status_code)
    print("Health: HEALTHY")