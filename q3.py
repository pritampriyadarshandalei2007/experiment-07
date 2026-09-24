# wap to create a list containing the power of said number in bases raised to the corresponding number in the index using python map .
numbers = [2, 3, 4, 5]

result = list(map(lambda x, i: x ** i, numbers, range(len(numbers))))

print(result)
