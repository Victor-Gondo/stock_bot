from dotenv import load_dotenv
import os
import requests

load_dotenv()

# api_key = os.getenv("API_KEY")
api_key = '7d9b64f51c3d474d9c6d6a0eed986de17a'

base_url = f'https://api.finazon.io/latest'

dataset = 'us_stocks_essential'
ticker = 'META'
interval = '1h'
endpoint = 'time_series'

#this gets the latest close high low open t and v of the
url = f'{base_url}/{endpoint}?ticker={ticker}&dataset={dataset}&interval={interval}&apikey={api_key}'

data = requests.get(url).json()
print(data)