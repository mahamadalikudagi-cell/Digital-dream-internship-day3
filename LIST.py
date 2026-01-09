
students=["md","abhi","raju"]
print(students)


print(students[0])
print(students[-1])
print(students[-3:-1])


students.append("abhi")
students.insert(1,"mahi")
students.remove("abhi")

print(students)

students.sort()
print(students)
students.reverse()
print(students)
len(students)
["abhi",
Somanth
Ravi
['Somanth', 'Raghav']
['Somanth', 'Shankar', 'Raghav', 'Ravi']
['Raghav', 'Ravi', 'Shankar', 'Somanth']
['Somanth', 'Shankar', 'Ravi', 'Raghav']
4

course=("Python",3,12500,12500)

print(course[1])
print(course[-1])
print(course[0:2])

print(course.count(12500))
print(course.index(3))
print(course)

cou=list(course)
cou.pop()
course=tuple(cou)
print(course)
3
12500
('Python', 3)
2
1
('Python', 3, 12500, 12500)
('Python', 3, 12500)