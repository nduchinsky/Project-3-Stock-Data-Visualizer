import requests
import matplotlib.pyplot as plt
from datetime import datetime
# Function to query Alpha Vantage API
def get_stock_data(symbol, api_key, function='TIME_SERIES_DAILY'):
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data from Alpha Vantage API.")
        return None
# Helper function to filter data by date
def filter_by_date(data, start_date, end_date):
    time_series = data['Time Series (Daily)']
    filtered_data = {date: time_series[date] for date in time_series if start_date <= date <= end_date}
    return filtered_data
# Function to plot stock data
def plot_stock_data(data, chart_type='line'):
    dates = list(data.keys())
    close_prices = [float(data[date]['4. close']) for date in dates]
    
    plt.figure(figsize=(10, 5))
    
    if chart_type == 'line':
        plt.plot(dates, close_prices, label='Close Price')
    elif chart_type == 'bar':
        plt.bar(dates, close_prices, label='Close Price')
    else:
        print("Invalid chart type.")
        return
    
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.title('Stock Price Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.show()
# Validate date inputs
def validate_dates(start_date, end_date):
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
        if end_date < start_date:
            raise ValueError("End date cannot be before start date.")
    except ValueError as e:
        print(f"Error: {e}")
        return False
    return True
# Main Function
def main():
    api_key = 'OD3EFEVXOZ4MW4NC'  # Use your Alpha Vantage API key here
    stock_symbol = input("Enter the stock symbol: ")  # e.g., 'AAPL'
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    # Validate date input
    if validate_dates(start_date, end_date):
        stock_data = get_stock_data(stock_symbol, api_key)
        if stock_data:
            filtered_data = filter_by_date(stock_data, start_date, end_date)
            chart_type = input("Enter chart type (line/bar): ")
            plot_stock_data(filtered_data, chart_type)
if __name__ == '__main__':
    main()