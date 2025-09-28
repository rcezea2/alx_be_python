#!/usr/bin/python3

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))



def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=days) + datetime.now().date()
    print("Future date: ", future_date.strftime("%Y-%m-%d"))


display_current_datetime()
calculate_future_date()
