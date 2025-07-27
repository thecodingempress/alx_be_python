from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date(days):
    days = int(input("Enter the number of days to add to the current date:"))
    
    today = datetime.now()
    future_date = today + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))


display_current_datetime()
calculate_future_date(0)  # Placeholder to call the function
# This is a placeholder to call the function, as the function expects user input.