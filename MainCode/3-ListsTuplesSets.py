"This code is all about Lists[], Tuples(), and Sets{}"

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
popped = COURSES.pop()
print(COURSES)
print(popped)

print('\n reverse method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
COURSES.reverse()
print(COURSES)

print('\n sort Ascending method:')
NUMS = [1, 5, 2, 4, 3]
print(NUMS)
NUMS.sort()
print(NUMS)

print('\n sort Decending method:')
NUMS = [1, 5, 2, 4, 3]
print(NUMS)
NUMS.sort(reverse=True)
print(NUMS)

print('\n sort Ascending method withouth changing the original:')
NUMS = [1, 5, 2, 4, 3]
print(NUMS)
SORTEDNUMS = sorted(NUMS)
print(NUMS)
print(SORTEDNUMS)

print('\n min max sum Method:')
NUMS = [1, 5, 2, 4, 3]
print(NUMS)
print(min(NUMS))
print(max(NUMS))
print(sum(NUMS))

print('\n index method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
print(COURSES.index('CompSci'))


print('\n find if Art is in the list method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
print('Art' in COURSES)

print('\n for loop:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
for item in COURSES:
    print(f"{item} is Math: {'Math' in item}")

print('\n for loop and figure out the index and the value,  numerate:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
for index, CO in enumerate(COURSES):
    print(index, CO)
    print(f"index {index} is Math? {'Math' in CO}")


print('\n for loop and figure out the index and the value,  numerate (if we want to strat the enumarator from 1 instead of 0):')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
for index, CO in enumerate(COURSES, start=1):
    print(index, CO)
    print(f"enum {index} is Math? {'Math' in CO}")


print('\n Join and Split method:')
COURSES = ['History', 'Math', 'Physics', 'CompSci']
print(COURSES)
COURSE_STR = ' - '.join(COURSES)
print(COURSE_STR)
NEW_List = COURSE_STR.split(' - ')
print(NEW_List)


print("\nTuples")
print("\n\nList mutable")
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)

print("\nTuples Immutable")
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)

print("\nSet - bigg difference is Set does not care about the order")
cs_COURSES = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_COURSES = {'History', 'Math', 'Art', 'Design'}
print(cs_COURSES)
print(art_COURSES)
print("\n intersection method for set")
print(cs_COURSES.intersection(art_COURSES))
print("\n difference method for set")
print(cs_COURSES.difference(art_COURSES))
print("\n union method for set")
print(cs_COURSES.union(art_COURSES))

print("\n\nempty list, tuple, set")
empty_list = []
empty_list = list()
print(empty_list)

empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)

empty_set = {}  # this is not right!, this is dictionary
empty_set = set()
print(empty_set)
