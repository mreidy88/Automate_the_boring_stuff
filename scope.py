
# global scope
def spam():
    # local variables
    global eggs
    eggs = 'Hello'
    print(eggs)


#
eggs = 15
spam()
print(eggs)
