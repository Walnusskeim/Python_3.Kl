import time
import os
import requests

key = "7895817390372e14a64c726bb7e1a367"

response = requests.get("https://api.stockdata.org/v1/data/quote?symbols=RHM&api_token=eCyZrqWRmt8UWVvqfyDYH7UwwmMyhjzpkqCu9DEj")

print(response.json())
