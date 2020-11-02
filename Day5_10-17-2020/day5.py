# studentsname = ['Alma, Bea, Cathy, Dory, Emma']
# studentstotal = [350, 360, 370, 390, 395]
# studentsave = [50, 51, 52, 53, 54, 55]
# studentsgrade = ['c, c, b, b, a']
# print(studentsname)
# print(studentstotal)
# print(studentsave)
# print(studentsgrade)
# finale = []
# finale.append(studentsname)
# finale.append(studentstotal)
# finale.append(studentsave)
# finale.append(studentsgrade)

n = eval(input('Enter the number of students:'))
students = []
for i in range(n):
    name = input('Enter the student name:')
    m1, m2, m3, m4, m5 = eval(input('Enter the students mark:'))
    total = m1 + m2 + m3 + m4 + m5
    avg = total / 5
    st = [i+1, name, total, avg]
    students.append(st)

print(students)
