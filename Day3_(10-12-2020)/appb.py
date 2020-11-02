# input('Enter the student name:')
# input('Enter their marks following:')
# Mark_1 = eval(input('Mark_1:'))
# Mark_2 = eval(input('Mark_2:'))
# Mark_3 = eval(input('Mark_3:'))
# Mark_4 = eval(input('Mark_4:'))
# Mark_5 = eval(input('Mark_5:'))
# total = Mark_1+Mark_2+Mark_3+Mark_4+Mark_5
# print(f'{Mark_1} + {Mark_2} + {Mark_3} + {Mark_4} + {Mark_5} = {Mark_1 + Mark_2 + Mark_3 + Mark_4 + Mark_5}')
# average = total/5

# correct
name = input('Enter the student name:')
m1, m2, m3, m4, m5 = eval(input('Enter the students mark:'))
total = m1+m2+m3+m4+m5
average = total / 5
print(f'Name : {name}, Total: {total}, Average: {average}%')
