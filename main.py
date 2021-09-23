import datetime

gender = input("Please enter your gender(M or F):")    # getting input
birthday_input = input('Enter your birthday in YYYY-MM-DD format')
year, month, day = map(int, birthday_input.split('-'))   # Splitting the input into separate year, month and date
birthday = datetime.date(year, month, day)  # assigning the values to the birthday variable


