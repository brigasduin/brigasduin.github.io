import requests 
from datetime import datetime, timedelta
API_KEY = 'your API'
URL = 'https://newsapi.org/v2/everything'

def buscar_noticias():
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    params = {
        'q': 'cybersecurity OR hacker OR "segurança digital"',
        'from': yesterday,
        'sortBy': 'publishedAt',
        'language': 'en',
        'apiKey': API_KEY
        
    }
    try:
        response = requests.get(URL, params=params)
        if response.status_code == 200:
            return response.json().get('articles', [])
        else:
            print(f'API error: {response.status_code}')
            return []
    except Exception as e:
        print(f'Connection error: {e}')
        return []