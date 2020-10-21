print("Hello world")
userInput = []
userInput.append(input("What is your name? "))
userInput.append(input("What is your favorite color? "))
print("Hello {}, your favorite color is {}.".format(*(userInput)))