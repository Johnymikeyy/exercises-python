celcius = [20, 56, 86, 51]

kelvin = []

fahrenheit = []

for c in celcius:
    k = c + 273
    kelvin.append(k)
    f = c * 9/5 + 32
    fahrenheit.append(f)
    
print(kelvin)
print(fahrenheit)
