# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
even_sum = 0
x = [1, 1] # Fibonacci sequence starts with 1,1...

while (x [-2] + x [-1]) < 4000000: # Check if the coming number is smaller than 4 million
    if (x [-2] + x [-1]) % 2 == 0: # Check if the number is even
        even_sum += (x [-2] + x [-1])
    x.append (x [-2] + x [-1]) # Compose the Fibonacci sequence
print (even_sum)

    