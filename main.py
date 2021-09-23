import datetime

gender = input("Please enter your gender(M or F):")
birthday_input = input('Enter your birthday in YYYY-MM-DD format')
year, month, day = map(int, birthday_input.split('-'))
birthday = datetime.date(year, month, day)
print(birthday.weekday())

