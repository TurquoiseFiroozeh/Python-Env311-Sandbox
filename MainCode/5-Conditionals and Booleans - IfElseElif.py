"""This code is all about Conditionals and Booleans, If, Else and Elif Statements"""

# Comparison
# Equql:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object identity:      is

# boolean operation
# and
# or
# not

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. for example, {}.

if True:
    print("Conditional was True")

if False:
    print("Conditional was True")
else:
    print("Conditional was false")

LANGUAGE = 'Python'
if LANGUAGE == 'Python':
    print("Language is Python")
else:
    print("no match")

LANGUAGE = 'Java'
if LANGUAGE == 'Python':
    print("Language is Python")
else:
    print("no match")


print("\n swichcase or els if")
if LANGUAGE == 'Python':
    print("Language is Python")
elif LANGUAGE == "Java":
    print("Language is Java")
elif LANGUAGE == "Java Script":
    print("Language is JavaScript")
else:
    print("no match")


print("\n\n boolan operation")

print("\nand")
USER = 'Admin'
LOGGED_IN = "True"

if USER == 'Admin' and LOGGED_IN:
    print("Admin Page")
else:
    print("Bad Cred")

print("\nor")
USER = 'Admin'
LOGGED_IN = "False"

if USER == 'Admin' or LOGGED_IN:
    print("Admin Page")
else:
    print("Bad Cred")

print("\nnot")
if not LOGGED_IN:
    print("Please Log In")
else:
    print("Welcome")


print("\n differnce between == and is")
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)


print("\n\n")
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))
print(a is b)


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. for example, {}.

print("\n\n False Value")
CONDITION = False
if CONDITION:
    print("Evaluated to True")
else:
    print("Evaluated to False")


print("\n\n None Value")
CONDITION = None
if CONDITION:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("\n\n Zero Value")
CONDITION = 0
if CONDITION:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("\n\n Any empty sequence Value")
CONDITION = ""
if CONDITION:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("\n\n Any empty mapping Value")
CONDITION = {}
if CONDITION:
    print("Evaluated to True")
else:
    print("Evaluated to False")
