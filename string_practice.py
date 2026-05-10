#Replace unwanted characters.
text = "Hello, World!"
print(text.replace(",","").replace("!",""))


#Count spaces in sentence.
text = " Hello, World! "
print(text.count(" "))


#Reverse string.
text = "Hello, World!"
print(text[::-1])

#Print alternate characters.
text = "Hello, World!"
print(text[::2])


#Count vowels in string.
text = "Hello, World!"
count = sum(1 for ch in text if ch in 'aeiouAEIOU')
print(count)

#Check palindrome.
text = input("Enter a text")
text_reverse = text[::-1]
if text == text_reverse:
    print(f"{text} is palindrome")
else:
    print(f"{text} is not palindrome")

    