# Note: Never put input inside loop block.

# Break statements are used to end while loop prematurely. The execution will exit the while loop clause when it
# reaches the break statement. Keyword used is "break"
while True:
    print("Please type your name")
    name = input()
    if name == "your name":
        break
print("Thank you!")

# Continue statement
# Whenever program execution reaches the continue statement, it will jump back to the start of
# loop (Even after the execution reaches the end of the loop).

while True:
    print("Who are you?")
    name = input()
    if name != "kevin":
        continue
    print(f"Hello {name}. What is the password? (Hint: it is a fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access granted.")