# This is our notes but in Python. You can use this for coding references if you want!
# Made with love by kingofnetflix <3


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
Name = "Sidster"
if Name is "Sidster": # Make sure to remember, its Name not name
    print("Sidster")
    # Commas allow you to print multiple things on the same line
    print(Name, "is", "awesome!")
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
