#types
x = 5
y = 5.7
z = 2+3j
print(type(x))
print(type(y))
print(type(z))


x="24"
print(type(x))
x=int(x)
print(type(x))
print(x*3)

x=3.14
print(int(x))

x=3
print(float(x))

x="3"
print(float(x))


x = 3 #real
y = 4 #imaginary
print(complex(x,y))


#math opertion
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2) #floor division
print(3 % 2)
print(3**2)


#shorthand assignment
x = 2
#x = x + 3
x += 3
print(x)


#Measure distance
print(abs(2-10))


import math
#rounding numbers
price = 35.54879865
print(round(price))
print(round(price,2))
print(round(price,1))
print(math.ceil(price))
print(math.floor(price))
print(math.trunc(price))
print(int(price))

