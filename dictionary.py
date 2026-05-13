#Create student dictionary.
student = {
    "name":"Alosh",
    "age":25,
    "Job":"Data Analyst",
    "isStudent":True,
}
print(student)


#Access values using key.
student = {
    "name":"Alosh",
    "age":25,
    "Job":"Data Analyst",
    "isStudent":True,
}
print(student["name"])
print(student["age"])
print(student["Job"])
print(student["isStudent"])


#Update marks.
student = {
    "name":"Alosh",
    "age":25,
    "Job":"Data Analyst",
    "isStudent":True,
    "mark":85
}
print(student)
student["mark"]=88
print(student)