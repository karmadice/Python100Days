print("Hello there, What is your name?")
myName = input("My name is: ")
print(f"Its a pleasure meeting you {myName}.")
print(f"The length of your name is {len(myName)}")
print("What is your age?")
while True:
  try:
    myAge = int(input("My age is: "))
    break
  except ValueError:
    print("Please enter input only.")
    continue
print(f"You will be {int(myAge) + 1} next year")