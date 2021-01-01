friends = ['elora', 'charlie', 'mamy','claire', 'tom']

x = 0
while (x < len(friends)):
    friend = friends[x]
    x = x + 1
    if friend == 'mamy':
        continue
    print(friend)
    
for friend in friends:
    if friend == 'mamy':
        continue
    print(friend)
    