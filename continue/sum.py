num = int(input('enter a number:'))

if num < 0:
    print('this is a negative number')
else:
    sum = 0
    
    while num > 0:
        sum += num
        num -= 1
    print('total :', sum)