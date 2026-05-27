#Function to calculate the mean of a list of numbers
def numbers_mean(numbers):       
    print(len(numbers))
    return sum(numbers) / len(numbers)

mean_val = numbers_mean([10, 20, 30])
print(mean_val)

#Function to add two numbers
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 10)
print(result)


#Function to check even or odd
def even_or_odd(a):
    if a % 2 == 0 :
        return f"{a} is even"
    else:
        return f"{a} is odd"

even = even_or_odd(2)
print(even)
odd = even_or_odd(1)
print(odd)

#Function to clean a string
def clean(text):
    return text.strip().lower().replace(",", "")

cleaned_text = clean(" HaI")   
print(cleaned_text)