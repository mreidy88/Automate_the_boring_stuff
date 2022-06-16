import re

message = 'Call me aat 415-555-1011 tomorrow, or at 415-555-9999 for my office number.'

# \d is for the individual digits in the phone number
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo  stands for match object
mo = phoneNumRegex.search(message)
print(mo.group())
