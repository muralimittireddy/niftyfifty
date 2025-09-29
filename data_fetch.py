
import requests
from config import NSE_BASE_URL, NSE_NIFTY50_URL, HEADERS

def fetch_nifty50_data():
    """Fetch NIFTY 50 stock data from NSE"""
    session = requests.Session()
    session.get(NSE_BASE_URL, headers=HEADERS)
    response = session.get(NSE_NIFTY50_URL, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    data = response.json().get('data', [])
    return data
	
	


