


price = "1234,56"
print(price.replace(",","."))
phone = "176-1234-56"
print(phone.replace("-","/"))
print(phone.replace("-",""))

price="$1,2999.99"
print(price.replace("$","").replace(",",""))


phone ="+49 (176) 123-4567"
print(phone.replace("+","00").replace(" ","").replace("(","").replace(")","").replace("-",""))


#Transformation
first_name = "Michael"
last_name="Scott"
last_name = first_name +" "+ last_name
print(last_name)

folder = "C:/Users/Baraa/"
file = "report.csv"
file_path=folder+file
print(file_path)

#f-string
name= "alosh"
age=24
print("My name is "+ name + ", I am "+ str(age) +" years old.")
print(f"My name is {name}, I am {age} years old.") #datatype conversion not required


print(f"2 + 3={2+3}")


print(f'"This is me"')
print(f"\"This is me\"")
print(f'{{This is me}}')

#split
name="Adam-24-USA"
name.split('-')
stamp = '2026-09-20 14:30'
stamp.split(" ")
stamp = '2026-09-20'
stamp.split("-")
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))

#string repition
print("ha" *3)
print("=" *10)

#indexing & slicing
text = "Python"

#extract yhe first  character
print(text[0])
print(text[-6])

#extract last character
print(text[5])
print(text[-1])

#extract h
print(text[3])
print(text[-3])

date = "2026-09-20"

#extract the Year
print(date[0:4])
print(date[:4])

#Extract the month
print(date[5:7])

#extract the day
print(date[8:])
print(date[-2:])

#remove whitespaces
name = " Max "
print(len(name))
print(name.lstrip())
print(len(name.lstrip()))
print(name.strip())
print(len(name.strip()))
print(name.rstrip())

text = "@abc"
print(text.strip('@'))

#case conversion
text ="python PROGRAMMING"
print(text.lower())
print(text.upper())

search=" Email".lower().strip()
data="email".lower().strip()
print(search == data)


#clean string
text="968-Maria, ( D@t@ Engineer ) ;; 27y  "
#print(text.split)
clean_text =(
    text.lower()
    .replace("968-","name: ")
    .replace("@","a")
    .replace(","," |")
    .replace(";;","| age:")
    .replace("(","role:")
    .replace(")","")
    .strip()
)
print(clean_text)

text = "968-Maria, ( D@t@ Engineer ) ;; 27y"

clean_text = (
    text.lower()
    .replace("968-", "name: ")
    .replace("@", "a")
    .replace(",", " |")
    .replace(";;", "| age:")
    .replace("(", "role:")
    .replace(")", "")
    .strip()
)

print(clean_text)

#search
phone="+49-176-12345"
print(phone.startswith("+49"))
print(phone.endswith("12345"))

email="abc@sample.com"
print(email.endswith('@test.com'))
print("email validation", "@" in email)

file="data_backup.csv"
print(file.endswith('.pdf'))


#find
phone1 = "+48-176-12345"
phone2 = "48-654-98745"
print(phone1.find('-'))

print(phone1[phone1.find('-')+1:])
print(phone2[phone2.find('-')+1:])



#validation
country="USA"
print(country.isalpha())
print(country.isnumeric())
