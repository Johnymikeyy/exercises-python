#Problem 1
#Try to find the intersection (common) elements of two given lists without using a set?

a = [1,2,3,4,5,6,7,8,9]
b = [1,3,5,7,8,9]
result = list(filter(lambda x : x in a,b))
print(result)