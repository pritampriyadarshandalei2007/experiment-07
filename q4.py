# wap to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.
text = "PRITAM PRIYADARSHAN DALEI"
unique = set(text)

upper = list(map(lambda x: x.upper(), unique))

lower = list(map(lambda x: x.lower(), unique))

print("Uppercase:", upper)
print("Lowercase:", lower)
