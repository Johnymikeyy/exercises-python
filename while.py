  
my_flag = True
message = ''
while my_flag:
    message = input('to quit write quit')
    if message == 'quit':
        my_flag = False
    else: 
        print(message)