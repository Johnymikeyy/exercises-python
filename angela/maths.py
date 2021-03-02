# create a program using maths and f strings that tells us how many days, weeks, months 
#we have left if we live until 90 years old 

age = int(input("enter your age: \n"))

years_remaining = 90 - age
days_remaning = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"you have {days_remaning} days, {weeks_remaining} weeks, {months_remaining} months left"

message