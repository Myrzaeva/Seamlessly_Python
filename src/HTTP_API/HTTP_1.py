"api.weather.com"

import requests
url="http://google.com"
response = requests.get(url)


print(f"your request to {url} came back with {response.status_code} ")
