notes = {'ahmet' : 58, 'mehmet' : 76, 'ebru' : 44, 'pinar' : 90}

for key, value in notes.items():
    
    if value > 50:
        print(f"{key} got {value} : succesful")
    
    else: 
        print(f"{key} got {value} : failed")