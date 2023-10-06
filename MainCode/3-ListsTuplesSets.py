"This code is all about Lists, Tuples, and Sets"

COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
print(len(COURSES))
print(COURSES[0])
print(COURSES[3])
print(COURSES[-1])
print(COURSES[-2])
print(COURSES[0:2])
print(COURSES[:2])
print(COURSES[2:])

# Slicing
print('\n append method:')
print(COURSES)
COURSES.append('Art')
print(COURSES)


print('\n insert method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
COURSES.insert(0, 'Art')
print(COURSES)
print('\n insert method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
COURSES_2 = ['Art', 'Education']
COURSES.insert(0, COURSES_2)
print(COURSES)
print(COURSES[0])


print('\n extend method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
COURSES.extend(COURSES_2)
print(COURSES)

print('\n remove method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
COURSES.remove('Math')
print(COURSES)

print('\n pop method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
COURSES.pop()
print(COURSES)
