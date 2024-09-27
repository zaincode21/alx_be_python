from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    format_date = current_date.strftime('%Y-%m-%d %H:%M:%S')

    print(f"Current date and time: {format_date}")
    return current_date

# display_current_datetime()

def calculate_future_date(today):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = today + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

calculate_future_date(display_current_datetime())