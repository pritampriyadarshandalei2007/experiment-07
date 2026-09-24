# wap to find the ratio of positive numbers,negative numbers and zeroes in an array of integers using map().
numbers = [1, -2, 0, 4, -5, 0, 3]

positive = sum(map(lambda x: x > 0, numbers))
negative = sum(map(lambda x: x < 0, numbers))
zero = sum(map(lambda x: x == 0, numbers))

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
