"This code is all about String type"
MESSAGE = 'Hello World'
MESSAGE_IN_MULTILINE = "Hello World from\nKhoy\n"
MESSAGE_IN_MULTILINE2 = """"Hello World from
Khoy
"""


print(MESSAGE_IN_MULTILINE)
print(MESSAGE_IN_MULTILINE2)
print(MESSAGE)
print("length of the message: " + str(len(MESSAGE)))
print("the first character is:  " + MESSAGE[0])
print("the eleventh character is: " + MESSAGE[10])
print("the sixth character: " + MESSAGE[5])
print("string from first characgter to fifth(exclusive): " + MESSAGE[0:5])
print("string from first sixth to end: " + MESSAGE[6:])
print(MESSAGE.lower())
print(MESSAGE.upper())
print(MESSAGE.count('Hello'))
print(MESSAGE.count('l'))
print("find the first index of the text: " + str(MESSAGE.find('World')))
print(MESSAGE.find("Universe"))
MESSAGE.replace('World', 'Universe')
print(MESSAGE)
NEW_MESSAGE = MESSAGE.replace('World', 'Universe')
print(NEW_MESSAGE)
GREETING = 'Hello'
NAME = 'Michael'
MESSAGE = GREETING + NAME
print(MESSAGE)
MESSAGE = GREETING + ', ' + NAME + '. Welcome!'
print(MESSAGE)
MESSAGE = '{}, {}. Welcome!'.format(GREETING, NAME)
print(MESSAGE)
MESSAGE = f'{GREETING}, {NAME}. Welcome!'
print(MESSAGE)
MESSAGE = f'{GREETING}, {NAME.upper()}. Welcome!'
print(MESSAGE)
print(dir(NAME))
print(help(str))
print(help(str.lower))
