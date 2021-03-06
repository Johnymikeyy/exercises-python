# love calculator

name1 = input("What is your name\n")
name2 = input("What is their name\n")

combined_name = name1 + name2

lower_name =combined_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score}, you go together coke.")
elif (love_score >= 40) or (love_score <= 90):
    print(f"your love score is {love_score}, you are alright together")
else:
    print(f"your love score is {love_score}")
    # love calculator

name1 = input("What is your name\n")
name2 = input("What is their name\n")

combined_name = name1 + name2

lower_name =combined_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score}, you go together coke.")
elif (love_score >= 40) or (love_score <= 90):
    print(f"your love score is {love_score}, you are alright together")
else:
    print(f"your love score is {love_score}")
    