from datetime import datetime


print datetime.now().strftime("Today is %A, %B %d, %Y")


age = input("Enter your age ")
years = datetime.now().strftime("%Y")

print "You were born back in ", int(years) - age
