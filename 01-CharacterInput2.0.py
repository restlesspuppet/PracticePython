# CharacterInput
# RestlessPuppet
# 11-9-2019

import datetime
while True:
    name = input("What name do you go by? ")
    c = input("Is " + name +" correct? (y/n) ")
    if c == "y":
        break

age = input("How old are you? ")
age = int(age)
b = input("Have you had your birthday yet this ccalander year? (y/n) ")
if b == "n":
    age = age + 1
years = 100 - age
now = datetime.datetime.now()
year = int(now.year)+ years 
years = str(years)
year = str(year)
print("Thank you, " + name + ". Just so you know, in " + years + " years,(" +year + ") you will be 100 years old!")
input("(press enter to continue)")
