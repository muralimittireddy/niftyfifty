import os
import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def insert_data(df, table_name="nifty50_stocks"):
    """Insert or update data in PostgreSQL without duplicates (UPSERT)."""
    # conn = psycopg2.connect(
    #     dbname=DB_NAME,
    #     user=DB_USER,
    #     password=DB_PASSWORD,
    #     host=DB_HOST,
    #     port=DB_PORT
    # )
    conn = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD")
    )
    cur = conn.cursor()

    insert_query = f"""
        INSERT INTO {table_name} (
            symbol, company_name, industry, open, high, low,
            last_price, previous_close, change, percent_change,
            total_traded_volume, total_traded_value, week_52_high, week_52_low,
            near_52w_high_percent, near_52w_low_percent, isin, fo_stock, trade_date
        )
        VALUES (
            %(symbol)s, %(company_name)s, %(industry)s, %(open)s, %(high)s, %(low)s,
            %(last_price)s, %(previous_close)s, %(change)s, %(percent_change)s,
            %(total_traded_volume)s, %(total_traded_value)s, %(week_52_high)s, %(week_52_low)s,
            %(near_52w_high_percent)s, %(near_52w_low_percent)s, %(isin)s, %(fo_stock)s, %(trade_date)s
        )
        ON CONFLICT (symbol, trade_date) DO UPDATE
        SET company_name = EXCLUDED.company_name,
            industry = EXCLUDED.industry,
            open = EXCLUDED.open,
            high = EXCLUDED.high,
            low = EXCLUDED.low,
            last_price = EXCLUDED.last_price,
            previous_close = EXCLUDED.previous_close,
            change = EXCLUDED.change,
            percent_change = EXCLUDED.percent_change,
            total_traded_volume = EXCLUDED.total_traded_volume,
            total_traded_value = EXCLUDED.total_traded_value,
            week_52_high = EXCLUDED.week_52_high,
            week_52_low = EXCLUDED.week_52_low,
            near_52w_high_percent = EXCLUDED.near_52w_high_percent,
            near_52w_low_percent = EXCLUDED.near_52w_low_percent,
            isin = EXCLUDED.isin,
            fo_stock = EXCLUDED.fo_stock;
    """

    for _, row in df.iterrows():
        cur.execute(insert_query, row.to_dict())

    conn.commit()
    cur.close()
    conn.close()
    print(f"Data inserted/updated into table {table_name}")
	
	
	

