"This code is all about Dictionaries and working with key-value pairs"
STUDENT = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(STUDENT)

print(STUDENT['name'])
print(STUDENT['age'])
print(STUDENT['courses'])

print("\n\n")
STUDENT = {1: 'John', 2: 25, 3: ['Math', 'CompSci']}
print(STUDENT)
print(STUDENT[1])
print(STUDENT[2])
print(STUDENT[3])

print("\n\n")
STUDENT = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(STUDENT)

print(STUDENT.get('name'))
print(STUDENT.get('age'))
print(STUDENT.get('courses'))
print(STUDENT.get('phone'))
print(STUDENT.get('phone', 'Not Found'))

print("\n add a key and defualt value to existing dictionary")
STUDENT['phone'] = "555-5555"
print(STUDENT)
print(STUDENT.get('phone', 'Not Found'))

print("\n update a few values and add a key and defualt value to existing dictionary")
STUDENT = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(STUDENT)
STUDENT.update({'name': "Masoud", 'age': 26, 'phone': "555-5555"})
print(STUDENT)

print("\n delete a key and its value with del method")
STUDENT = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(STUDENT)
del STUDENT['age']
print(STUDENT)


print("\n delete a key and its value with pop method")
STUDENT = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(STUDENT)
COURSES = STUDENT.pop('courses')
print(STUDENT)
print(COURSES)


print("\n count number of keys")
STUDENT = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(STUDENT)
print(len(STUDENT))
print(STUDENT.keys())
print(STUDENT.values())
print(STUDENT.items())

print("\n for loop in dictionary")
STUDENT = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(STUDENT)
for key in STUDENT:
    print(key)

for key in STUDENT.keys():
    print(key)

for value in STUDENT.values():
    print(value)

for key, value in STUDENT.items():
    print(f"{key}: {value}")
