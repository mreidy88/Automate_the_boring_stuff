# upper() and lower() return an uppercase or lowercase string.
# isupper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle() returns True or False if the string is that uppercase, lowercase, alphabetical letters, and so on.
# startswith() and endswith() also return bools.
# ‘,'.join([‘cat', ‘dog']) returns a string that combines the strings in the given list.
# ‘Hello world'.split() returns a list of strings split from the string it's called on.
# rjust() ,ljust(), center() returns a string padded with spaces.
# strip(), rstrip(), lstrip() returns a string with whitespace stripped off the sides.
# replace() will replace all occurrences of the first string argument with the second string argument.
# Pyperclip has copy() and paste() functions for getting and putting strings on the clipboard.

spam = 'Hello World!'
spam.islower()
spam.upper()

answer = input()


'hello'.isalpha()
'hello123'.isalnum()
'123'.isdecimal()
'Hello World'.isspace()
'This Is TitleCase'.istitle()
'hello world'.title()

# Justify
'Hello'.rjust(10)
'Hello'.ljust(20)
'Hello'.rjust(20, '*')
'Hello'.ljust(25, '-')
'hello'.center(20, '=')

# Strip
spam1 = 'Hello'.rjust(20, '*')
spam1.strip()
