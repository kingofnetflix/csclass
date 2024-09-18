## This is our notes but in Python. You can use this for coding references if you want!
## Made by kingofnetflix 

## Python Basics

# Printing
"""
\t (tab) 
\r (reset) 
\n (new line) 
\\ (displays one backslash when printed)
\” (displays one double quote when printed
\’ (displays one single quote when printed
"""
print("Look I can go down here!\nWooo!")
# Integer variable
x = 5
# Float variable
y = 5.02
# String variable - A series of characters, this can be letters, words, or numbers
z = "5"
# Lists - A list is a collection of items, that can be of any type
list = [x, y, z]
# Tuples - An unchangeable list (ex(21,hi,false)
my_tuple = (1, 2, 3, 'a', 'b', 'c') 
print(my_tuple[0]) # This code prints the first value of the list, which is 1
print(my_tuple[5]) # This code prints the 6th value, which is ‘c’
# Boolean - A boolean is a data type that can only be True or False
bool = True
if bool == True:
    print("The boolean is true")
# Identifiers - Being specific with variable names
name = "Sidster"
if name == "Sidster": # Make sure to remember, its Name not name
    print("Sidster")
    # Commas allow you to print multiple things on the same line
    print(name, "is", "awesome!")
# Casting - Numbers in Strings need to cast to an int or float
numString = "56"
print(4 + int(numString)) # This will change the string to a integer (due to the int() void)
# Input - Sometimes we want the user to give us information. We can store it in a variable
name = input("What is your name? ")
print("Your name is", name)
num = int(input("Pick a number: "))
print("Your number is", num) # We can use the var instantly since it is already casted
floater = float(input("Enter a decimal value: "))
print("You inputted", floater) # We can use the var instantly since it is already casted

# Math Operators

# Addition
result = 5 + 3
print("Addition:", result)

# Subtraction
result = 10 - 4
print("Subtraction:", result)

# Multiplication
result = 6 * 2
print("Multiplication:", result)

# Division
result = 15 / 3
print("Division:", result)

# Floor Division
result = 15 // 4
print("Floor Division:", result)

# Modulus (Getting the remainder)
result = 15 % 4
print("Modulo:", result)

# Exponential
result = 5 ** 2
print("Exponentiation:", result)

# Functions
def Skibidi_Function():
    ip = "mc.240hz.tech"
    if ip == "mc.240hz.tech":
        print("you got the right ip!")

# Parameters
def sayHello(parameter): # if parameter is not a string this wont work (this can be checked)
	print("Hello", parameter);   # this code says hello to a name passed with a parameter 