import random   # import ???
xnum = random.randint(1, 100)

num = int(input('please enter a number between 1 and 100:'))

while num != xnum:
    if num < xnum:
        print(f' {num} enter a greater number ')
        num = int(input())
    else:
        print(f' {num} enter a smaller number ')
        num = int(input())

print(f'congt!')
    