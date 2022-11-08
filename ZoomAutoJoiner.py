import time
import re

from selenium import webdriver
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def valid_date():
    # List of days
    correct_dates = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Loops until the user input a valid day
    while True:
        user_day = input("input valid day of the week!")
        if user_day.lower() in correct_dates:
            return user_day


def valid_time(user_time):
    # Regex to check valid time in 24-hour format.
    regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
    # Compile the ReGex
    p = re.compile(regex)
    # If the time is empty
    # Return false
    if user_time == "":
        return False
    # Pattern class contains matcher() method
    # To find matching between given time
    # And regular expression.
    m = re.search(p, user_time)
    # Return True if the time
    # Matched the ReGex otherwise False
    if m is None:
        return False
    else:
        return True


def time_passer():
    # Loops until user inputs a valid time
    while True:
        user_time = (input("Please enter military time: "))
        if valid_time(user_time):
            break
    return user_time


def check_day():
    # Creates empty lists
    class_link = []
    class_time = []
    class_date = []

    while True:
        # Asks user to input a link
        link = input("link: ")
        class_link.append(link)

        # Asks user for time
        user_time = time_passer()
        class_time.append(user_time)

        # Asks user for date
        user_date = valid_date()
        class_date.append(user_date)

        cont = input("hit n to stop adding")
        if str.upper(cont) == "N":
            break

    # Counts how many elements are in the list
    n = len(class_link)
    # Infinitely runs to check date and time
    while True:
        # Loops through all three lists at once
        for (a, b, c) in zip(class_link, class_time, class_date):

            # Checks if the users day matches the computers day
            if c.lower() == datetime.today().strftime('%A').lower() and b == time.strftime("%H:%M"):
                driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
                # Maximizes the browser window
                driver.maximize_window()
                # Gets method to launch the URL
                driver.get(a)

            # Divides 60 with however many elements there are in a loop
            # In order to ensure that every minute has every list iterated through
            time.sleep(60 / n)


# Begins entire function
check_day()
