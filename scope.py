
# global scope
def spam():
    # local variables
    global eggs
    eggs = 'Hello'
    print(eggs)


# Eggs is already assigned
eggs = 15
spam()
print(eggs)
