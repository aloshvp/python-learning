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



#Sort a list in descending order
items =[1,5,4,2]
print(f"Descending order: {sorted(items,reverse=True)}")

items.sort(reverse=True) 
print(f"Descending order: {items}") #sort original list


#Remove duplicates from a list
items =[1,5,4,2,1,5,'a','b','a']
print(f"Unique items: {list(set(items))}")

items =[1,5,4,2,1,5,'a','b','a']
items_new=[]
for i in items:
    if i not in items_new:        
            items_new.append(i)
print(f"Unique items: {items_new}") 



# Count even and odd numbers
items = [1,5,4,2,1,5]
even_count = 0
odd_count = 0
for i in items:

    if i % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}") 


#Merge two lists
items1 = [1,5,4,2,1,5]
items2 = ['a','a','b',2,10,]
items3 = items1 +items2
print(items3)


#Convert string into list
name = "alosh"
print(list(name))

name_list = []
for i in name:    
    name_list.append(i)
print(name_list)    


#Extract even numbers using list comprehension
numbers = [1,2,3,5,10,12,15,14,16,7,9]
even_numbers = [
    i
    for i in numbers
    if i % 2 == 0
]
print(even_numbers)