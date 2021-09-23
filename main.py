import datetime

gender = input("Please enter your gender(M or F):")    # getting input
birthday_input = input('Enter your birthday in YYYY-MM-DD format')
year, month, day = map(int, birthday_input.split('-'))   # Splitting the input into separate year, month and date
birthday = datetime.date(year, month, day)  # assigning the values to the birthday variable

day = birthday.weekday()

if gender == "F":
    if day == 0:
        print("Your ghanaian alias is Adjoa ")
    elif day == 1:
        print("Your ghanaian alias is Abenaa ")
    elif day == 2:
        print("Your ghanaian alias is Akua")
    elif day == "Thursday":
        print("Your ghanaian alias is Yaa ")
    elif day == 4:
        print("Your ghanaian alias is Afia")
    elif day == 5:
        print("Your ghanaian alias is Amma")
    elif day == 6:
        print("Your ghanaian alias is Akosua ")
else:
    if day == 0:
        print("Your ghanaian alias is Kwasi ")
    elif day == 1:
        print("Your ghanaian alias is Kodjo ")
    elif day == 2:
        print("Your ghanaian alias is Kwabena")
    elif day == 3:
        print("Your ghanaian alias is Kwaku ")
    elif day == 4:
        print("Your ghanaian alias is Yaw")
    elif day == 5:
        print("Your ghanaian alias is Kofi")
    elif day == 6:
        print("Your ghanaian alias is Kwame")

