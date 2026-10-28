from datetime import date, datetime

def say_hi_to_dan():
    print ("Hi Dan!")

say_hi_to_dan()

def say_hi_to_person(name):
    print (f"Hi {name}!")

say_hi_to_person("Sammi")

def say_hi_with_location(name, location):
    print (f"Hi {name}!  How's {location} today?")

say_hi_with_location("Dan", "Cornwall")

def say_hi_with_defaults(name="User", location="the world"):
    print (f"Hi {name}!  How's {location} today?")

say_hi_with_defaults()
say_hi_with_defaults(name="Dan")
say_hi_with_defaults(location="Cornwall")

def calculate_age(date_of_birth):
    current_date = date.today()

    if (
        (current_date.day, current_date.month) <
        (date_of_birth.day, date_of_birth.month)
    ):
        had_birthday_this_year = False
    else:
        had_birthday_this_year = True

    age = current_date.year - date_of_birth.year
    if not had_birthday_this_year:
        age -= 1

    return age

dob_input = input("Input your date of birth in DD/MM/YYYY format: ")
dob = datetime.strptime(dob_input, "%d/%m/%Y").date()

age_now = calculate_age(dob)
print (f"So you're {age_now}")
#print (f"So you're {calculate_age(dob)}")

def gather_user_details():
    name = input("What's your name? ")
    location = input("Where are you from? ")
    age = int(input("How old are you? "))

    return name, location, age

user_name, user_location, user_age = gather_user_details()
print (f"Hi {user_name}!  How are things in {user_location}?")
print (f"I've heard you'll be {user_age+1} at your next birthday.")

