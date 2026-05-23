#Create tuple with student data.
student = ("John",18,"Data Engg","student")
print(type(student))


#Access tuple elements.
student = ("John",18,"Data Engg","student")
print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Course: {student[2]}")
print(f"isStudent: {student[3]}")


#Convert tuple to list.
student = ("John",18,"Data Engg","student")
student_list = [
    stud
    for stud in student
]
student_lst = list(student)
print(student_list)
print(student_lst)

#Remove duplicates from tuple.
items = (1,2,'a','b',1,'c','a')
items_unique = tuple(set(items))
print(items_unique)



#Create tuple with student data
student = ('alosh','diploma','software engg')
print(student)
print(type(student))



