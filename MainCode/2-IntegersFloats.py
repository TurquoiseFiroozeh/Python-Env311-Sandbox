"This code is all about Integer and Float"

# Arithmetic operations:
# Addition:       2+3
# Substractopm:   2-3
# Multiplication: 3*2
# Division:       3/2
# Floor Division: 3//2
# Exponent:       3**2
# Moduls:         3%2

# Comparison
# Equql:                3==2
# Not Equal:            3!=2
# Greater Than:         3>2
# Less Than:            3<2
# Greater or Equal:     3>=2
# Less or Equal:        3<=2


NUM = 3
print(f'{NUM} : {type(NUM)}')
NUM = 3.14
print(f'{NUM} : {type(NUM)}')

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)
print(3**2)
print(3 % 2)

NUM = NUM+1
print(NUM)
NUM += 1
print(NUM)
NUM *= -1
print(NUM)
print(abs(NUM))
print(round(NUM))
print(round(NUM, 1))

NUM_1 = 3
NUM_2 = 2

print(NUM_1 == NUM_2)
print(NUM_1 != NUM_2)
print(NUM_1 > NUM_2)
print(NUM_1 < NUM_2)
print(NUM_1 >= NUM_2)
print(NUM_1 <= NUM_2)

NUM_1 = '100.1'
NUM_2 = '200.1'
print(NUM_1+NUM_2)

# casting
NUM_1 = float(NUM_1)
NUM_2 = float(NUM_2)
print(NUM_1+NUM_2)
