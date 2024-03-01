names_string = "Mark, John, Jacob, Sam, Bob"

names = names_string.split(", ")

import random

numItems = len(names)

randomChoice = random.randint(0, numItems - 1)

personWhoWillPay = names[randomChoice]

print(personWhoWillPay + " is going to pay for the meal today!")