friends = {'mike' : 20, 'charlie' : 22, 'johny' : 30, 'katie' : 25}

for friend in friends.keys():
    print(friend)
    
for key, value in friends.items():
    if key == 'charlie':
        break          # broke the chaine
    print(key, value)
    
for key, value in friends.items():
    if key == 'charlie':
        continue       # goes on the chaine by jumping itself
    print(key, value)