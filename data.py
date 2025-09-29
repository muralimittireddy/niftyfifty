

import pandas as pd
from datetime import datetime

def create_stock_table(stock_data):
    """Transform raw JSON stock data into DataFrame"""
    table_rows = []

    for data in stock_data:
        meta = data.get('meta', {})
        row = { 
            'symbol': data.get('symbol'),
            'company_name': meta.get('companyName'),
            'industry': meta.get('industry'),
            'open': data.get('open'),
            'high': data.get('dayHigh'),
            'low': data.get('dayLow'),
            'last_price': data.get('lastPrice'),
            'previous_close': data.get('previousClose'),
            'change': data.get('change'),
            'percent_change': data.get('pChange'),
            'total_traded_volume': data.get('totalTradedVolume'),
            'total_traded_value': data.get('totalTradedValue'),
            'week_52_high': data.get('yearHigh'),
            'week_52_low': data.get('yearLow'),
            'near_52w_high_percent': data.get('nearWKH'),
            'near_52w_low_percent': data.get('nearWKL'),
            'isin': data.get('isin'),
            'fo_stock': meta.get('isFNOSec'),
            'trade_date': datetime.now().date()
        }
        table_rows.append(row)
    
    df = pd.DataFrame(table_rows)
    return df



