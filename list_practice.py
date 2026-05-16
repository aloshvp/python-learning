#Print middle elements using slicing.
items = ['a','b',1,'c','3']
print(items[1:-1])      


#Reverse list using slicing.
items = ['a','b',1,'c','3']
print(items[::-1])  
#items.reverse()
#print(items)
#print(list(reversed(items)))

#Insert value at specific position.
items = ['a','b',1,'c','3']
items.insert(0,"x")
print(items)

#Update second element.
items = ['a','b',1,'c','3']
items[1]='x'
print(items)


#Delete element using: del
items = ['a','b',1,'c','3','b']
del items[0]
print(items)


# Sum only integers
items = ['a', 'b', 1, 'c', '3', 'b']
total = sum(i for i in items if isinstance(i, int))
print(total)


#Find maximum number in list.
items = ['a','b',1,'c','3','b']
print(max(i for i in items if isinstance(i,int)))
items2 = [1,2,5,8,0]
print(max(items2))

#Extract even numbers.(List Comprehension)
items=[1,3,9,5,6,2]
item_even=[
    i
    for i in items
    if i%2==0
]
print(item_even)


#Convert all names to uppercase.(List Comprehension)
items=['abc','xyz']
item_upper=[
    i.upper()
    for i in items
]
print(item_upper)


#Find the largest element in a list
items =[1,5,6,8,2,3,10,4]
print(f"Larget element: {max(items)}")

largest = items[0]
for i in items:
    if i > largest:
        largest = i
print(f"Largest element: {largest}")       

#Find the smallest element in a list
items =[1,5,6,8,2,3,10,4]
print(f"Smallest element: {min(items)}")

smallest = items[0]
for i in items:
    if i < smallest:
        smallest = i
print(f"Smallest element: {smallest}")  


#Find the sum of all elements
items =[1,5,4]
print(f"Sum of all elements: {sum(items)}")

total = 0
for i in items:
    total += i
print(f"Sum of all elements: {total}")   


#Find the average of list elements
items =[1,5,4,2]
print(f"Average of elements: {sum(items)/len(items)}")

total = 0
for i in items:
    total += i
print(f"Average of elements: {total/len(items)}")



#Reverse a list
items =[1,5,4,2]
items.reverse()#reverse original list
print(f"Reverse: {items}")

items =[1,5,4,2]
print(f"Reverse: {items[::-1]}")

reverse_list = []
for i in range(len(items)-1, -1, -1):
    reverse_list.append(items[i])
print(f"Reverse: {reverse_list}")


#Sort a list in ascending order
items =[1,5,4,2]
print(f"Ascending order: {sorted(items)}")

items.sort() 
print(f"Ascending order: {items}") #sort original list

