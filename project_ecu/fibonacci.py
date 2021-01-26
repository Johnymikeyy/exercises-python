# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
even_sum = 0
x = [1, 1] # Fibonacci sequence starts with 1,1...

while (x [-2] + x [-1]) < 4000000: # Check if the coming number is smaller than 4 million
    if (x [-2] + x [-1]) % 2 == 0: # Check if the number is even
        even_sum += (x [-2] + x [-1])
    x.append (x [-2] + x [-1]) # Compose the Fibonacci sequence
print (even_sum)

    
######
x = [1, 1] # Fibonacci sequence starts with 1,1...

while (x [-2] + x [-1]) < 56: # Check if the coming number is smaller than 4 million
    if (x [-2] + x [-1]) % 2 == 0: # Check if the number is even
        x.append (x [-2] + x [-1]) # Compose the Fibonacci sequence
print (x)


##########
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1