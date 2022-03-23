if (4 < 5) and (5 < 6):
    print("That was true")
else:
    print("Well, it was worth it.")

if ((4 < 5) or (5 > 6)):
    print("At least one condition is right")
else:
    print("Both conditions were wrong")


# Pass statement
# pass is a null operation. When it executes, noting will happen. Consider it as placeholder statement.
# usage scenario: statement is required syntactically, but no code needs to be executed.

def thepassdemofunc(arg):
    pass  # a function that does nothing (not yet)


# return statement
# used to return a value from a function when its called

def thereturndemofunc(num1, num2):
    return num1 + num2  # return the sum of two numbers


# call the function
result = thereturndemofunc(100, 50)
print(result)


# del statement
# del statement is used to delete objects/variables

a = 10
b = 30
print(a, b)

# delete a and b
del a, b

# verify that a, and b are deleted
print(a, b)