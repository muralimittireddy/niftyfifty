from data_fetch import fetch_nifty50_data
from data import create_stock_table
from db import insert_data
from email_report import send_email
import pandas as pd
from datetime import datetime
import os

def save_to_excel(df):
    """Save the DataFrame as a daily Excel report"""
    today = datetime.today().strftime("%Y-%m-%d")
    os.makedirs("DailyReports", exist_ok=True)
    file_path = f"DailyReports/nifty50_stock_report_{today}.xlsx"

    gainers = df.sort_values(by="percent_change", ascending=False).head(5)
    losers = df.sort_values(by="percent_change", ascending=True).head(5)

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="NIFTY50 Data", index=False)
        gainers.to_excel(writer, sheet_name="Top Gainers", index=False)
        losers.to_excel(writer, sheet_name="Top Losers", index=False)

    print(f"Excel report saved: {file_path}")
    return file_path

def main():
    stock_data = fetch_nifty50_data()
    print("Data fetched from NSE")

    df = create_stock_table(stock_data)
    print("Data transformed into DataFrame")

    insert_data(df)
    print("Data stored in PostgreSQL successfully")

    report_path = save_to_excel(df)
    send_email(report_path)

if __name__ == "__main__":
    main()