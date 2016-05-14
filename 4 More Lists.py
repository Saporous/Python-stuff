
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

for bikes in bicycles:
	print(bikes)

# list() creates a list
val = list(range(1,6))

# range(x, y) creates a list from x to y
print('1:')
for val in range(1,5):
	print(val)

print(list(range(1,6,2)))

# ** is exponent operator
print('2:')
squares = []
for val in range(1,5):
	squares.append(val**2)
print(squares)

# List comprehension
print('3:')
squares = [val**2 for val in range(1,5)]
print(squares)

# Using slices of lists
print('4:')
print(squares[2:])
print(squares[-2:])

# Shallow copy lists
print('5:')
rectangles = squares
rectangles[1] = 100
print(squares[:])

# Deep copy lists
print('6:')
squares[1] = 3
rectangles = squares[:]
print(squares[:])

# Immutable lists are Tuples
print('7:')
tup = (10, 20)
print(tup)
