# wap to triple all numbers in a given list of integers. Use map() 
def triple(x):
    return x * 3

numbers = [1, 2, 3, 4, 5]

result = list(map(triple, numbers))

print(result)
