# Basic print
print("Hello World")

# How to get rid of newline
print("Hello",end='')
print(" World")

# Example output
print('cats','dogs','mice')
# Modify separator
print('cats','dogs','mice',sep=',')

# Print raw strings
print(r'That\'s Alice\'s cat!')

# String concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

# Multiline strings
print('''Dear Alice,

Your cat has been stolen.

Regards,
Jeff''')

# title() capitalizes the first letter of words
print(full_name.title(),end='')

# \t = tab, \n = newline
print("\t\n"+first_name)

# strip whitespace
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# str() is used to convert to text
num = 23
print("The number of choice is: " + str(num))

# note integer division converts to float in python 3
print(2/3)
print(2.0/3)
