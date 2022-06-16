import re

# phoneNumRegex = re.compile(r'/d/d/d-/d/d/d-/d/d/d/d')
# mo = phoneNumRegex.search('My number is 555-555-5555')
# mo.group()

#
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group(1)
