import re
# https://docs.python.org/2/library/re.html

text = 'Something number 444-444-4444'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Search through the text & store in match
match = phoneNumRegex.search(text)
print("Phone # is:" + match.group())

phoneParens = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
match = phoneParens.search(text)
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.group())

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?		# Area code
	(\s|-|\.)?				# Separator
	(\d{3})					# First 3 numbers
	(\s|-|\.)?				# Separator
	(\d{4})					# Last 4 numbers
	)''', re.X)
match = phoneRegex.search(text)
print(match.group())