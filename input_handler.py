from datetime import datetime
from error_checker import validate_symbol

def get_user_input():
    #stock symbol
    stock_symbol = input("Enter the stock symbol you want: ").upper()
    while not validate_symbol(stock_symbol):
        print("Invalid input. Please enter a valid stock code.")
        stock_symbol = input("Enter the stock symbol: ").upper()

    #chart type
    chart_type = input("Select chart type: 1. Bar, 2. Line: ")
    while chart_type not in ('1', '2'):
        print("Invalid input. Please enter 1 or 2.")
        chart_type = input("Select chart type: 1. Bar, 2. Line: ")

    chart_type = "Bar" if chart_type == '1' else "Line"

    #time series
    time_series = input("Select time series (1: Intraday, 2: Daily, 3: Weekly, 4: Monthly): ")
    #map the user input to the corresponding time series constant
    time_series_options = {'1': "TIME_SERIES_INTRADAY", '2': "TIME_SERIES_DAILY", 
                           '3': "TIME_SERIES_WEEKLY", '4': "TIME_SERIES_MONTHLY"}
    while time_series not in time_series_options:
        print("Invalid option. Please enter a number between 1 and 4.")
        time_series = input("Select time series (1: Intraday, 2: Daily, 3: Weekly, 4: Monthly): ")
    #get time series constant
    time_series = time_series_options[time_series]

    #start and end dates and validate
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


    return stock_symbol, chart_type, time_series, start_date, end_date
