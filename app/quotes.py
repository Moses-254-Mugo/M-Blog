import requests

URL = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    response = requests.get(URL)
    if response.status_code == 200:
        print(response.json())
        return response.json()
# get_quotes()