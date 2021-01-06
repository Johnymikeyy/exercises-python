numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

print("Given List:",numbers)

repeat = max(set(numbers), key = numbers.count)

print("the most frequent number is", int(repeat), "and", "it was repeated", numbers.count(3), "times")