#Create variables
Name = 'Alosh'
Age = 24
Salary = 25000
Is_student = True
print(type(Name))
print(type(Age))
print(type(Salary))
print(type(Is_student))

#swapping 2 numbers
num1=5
num2=10
temp=None
print("before swapping",num1,num2)
temp=num1
num1=num2
num2=temp
print("before swapping",num1,num2)

#Convert:
#string → int
str_val = '123'
print("before conversion",type(str_val))
str_int = int(str_val)
print("after conversion",type(str_int))

#int → float
int_val = 123
print("before conversion",type(int_val))
int_float_val = float(int_val)
print("after conversion",type(int_float_val))

#float → string
float_val= 23.22
print("before conversion",type(float_val))
float_str_val = str(float_val)
print("after conversion",type(float_str_val))

