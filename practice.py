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


#Create a list, tuple, set, and dictionary with sample values.
sample_list = [1,2,1,3,5,4]
sample_tuple = (1,2,1,3,5,4)
sample_set = {1,2,3,4,5}
sample_dic = {"id1":1,"id2":2,"id3":3}
print(sample_list)
print(sample_tuple)
print(sample_set)
print(sample_dic)


#Convert "500" into integer.
num_str = "500"
int_str = int(num_str)
print(int_str,type(int_str))


#Convert 25 into float.
num = 25
num_float = float(num)
print(num_float,type(num_float))


#Convert 99.99 into integer.
float_num = 99.99
float_to_int = int(float_num)
print(float_to_int,type(float_to_int))


#Take age input from user and convert to integer.
age = int(input("Enter age"))
print("age:",age)


#Add two numbers entered by user.
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("sum is:",num1 + num2)

#Take user name and print greeting.
user_name = input("Enter your name: ")
print("Hi, welcome",user_name)

#Calculate area of rectangle.
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print(f"Area of rectangle {area}")

#Calculate remainder using modulus.
dividend = int(input("Enter a dividend"))
divisor = int(input("Enter a divisor")) 
remainder = dividend % divisor
print(f"remainder :{remainder}")

#Find square and cube of number.
num = int(input("Enter a number: "))
square_of_num = num**2
cube_of_num = num**3
print(f"Square of number: {square_of_num}")
print(f"Cube of number: {cube_of_num}")

#Check whether character is vowel or consonant.
letter = input("Enter an alphabet: ").lower()
if len(letter) == 1 and letter.isalpha():

    if letter in "aeiou":
        print("Alphabet is a vowel")
    else:
        print("Alphabet is a consonant")

else:
    print("Invalid input")


#Create electricity bill condition.
unit = float(input("Enter units: "))

if unit < 0:
    print("Invalid unit")

elif unit > 1000:
    bill = unit * 5

elif unit > 500:
    bill = unit * 4

else:
    bill = unit * 3

if unit >= 0:
    print(f"Electricity bill: {bill}")    


#ATM withdrawal validation.
balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= 0:
    print("Invalid withdrawal amount")

elif withdraw > balance:
    print("Insufficient balance")

else:
    remaining_balance = balance - withdraw

    print("Withdrawal successful")
    print(f"Remaining balance: {remaining_balance}")


#Safe division using exception handling
try:
    num = int(input("Enter number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Division by zero")

else:
    print("Program executed successfully")