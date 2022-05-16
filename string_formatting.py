'hello ' + 'world'

name = 'Alice'
place = 'Main Street'
time = '6pm'
food = 'turnips'
'Hello ' + name + ', you are invited to a party at ' + \
    place + ' at' + '. Please bring ' + food + '.'

'Hello %s, you are invited to a party %s at %s. Please bring %s' % (
    name, place, time, food)
# %s are conversion specifiers
