from input_handler import get_user_input
from app_data import set_stock_symbol, set_chart_type, set_time_series, set_dates, get_chart_type
from api_handler import fetch_stock_data
from chart_generator import generate_chart

def main():
    while True:
        symbol, chart_type, time_series, start, end = get_user_input()
        set_stock_symbol(symbol)
        set_chart_type(chart_type)
        set_time_series(time_series)
        set_dates(start, end)

        fetch_stock_data()
        
        try:
            generate_chart(get_chart_type())
        except ValueError as e:
            print(f"Error generating chart: {e}")
            continue
        
        restart = input("Do you want to restart the program? (y/n): ").strip().lower()
        if restart != 'y':
            break

if __name__ == "__main__":
    main()
