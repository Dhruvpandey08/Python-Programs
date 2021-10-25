no_of_students=int(input())
students_marks={}
for i in range(no_of_students):
    a = input().split()
    name,scores = a[0], a[1:]
    scores = map(float,scores)
    students_marks[name]=scores
query_name=input()
marks=0
for i in students_marks[query_name]:
    marks=marks+i
avg=marks/3
print("%.2f"%avg)
