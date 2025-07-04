import requests
from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
print("TEST")

def position_dashboard(request):
    api_url = 'https://live.trading212.com/api/v0/equity/portfolio'
    headers = {
        'Authorization': f'{api_key}',
        'Content-Type': 'application/json'
    }

    print(api_key)

    try:
        response = requests.get(api_url, headers=headers)
        print("Status code:", response.status_code)
        print("Response:", response.text)
        positions = response.json() if response.status_code == 200 else []
    except Exception as e:
        print("Error fetching API:", e)
        positions = []

    return render(request, 'dashboard/dashboard.html', {'positions': positions})