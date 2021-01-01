minNum = int(input('please enter min number:'))
maxNum = int(input('please enter max number:'))

for evenNum in range(minNum, maxNum):
    if evenNum % 2 != 0:
        continue
    else:
        print(evenNum)