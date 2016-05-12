# Lists act just like C/C++/Java starting from 0
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
# Python allows for -1 access to last entry
print(bicycles[-1].title())

# Append to back
bicycles.append('fuji')
print(bicycles)

# Insert into position
bicycles.insert(0, 'Kestrel')
del bicycles[0]

# Pop last index off & store it in popped
popped = bicycles.pop()
print(popped)

# Pop argument index off & store it in popped
popped = bicycles.pop(0)
print(popped)

# Remove first instance of found string
bicycles.remove('cannondale')

# Don't forget len() works on a lot of data types
print(len(bicycles))

# Use sort() to permanently sort list
# Use sorted() to temporarily sort list
print(sorted(bicycles))

# reverse() permamently reverses list
bicycles.reverse()
print(bicycles)

