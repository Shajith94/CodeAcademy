# Your code below:
single_digits = list(range(10))
squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)
  print(squares)
#this iterates through single_digits and appends the square value of single digits

cubes = [element **  3 for element in single_digits]
print(cubes)
#list comprehension on single_digits list 

