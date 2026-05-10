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


