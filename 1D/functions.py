import random

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

def pick_a_random_dessert(*desserts):
    random_dessert = random.choice(desserts)
    print (f"My favourite dessert is {random_dessert}")

pick_a_random_dessert("Banoffee Pie", "Chocolate Torte", "Rhubarb Crumble")

pick_a_random_dessert("Banoffee Pie")

