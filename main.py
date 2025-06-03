import  random

randomNumber = random.randrange(1, 10)



userInput = int(input("Guese the number:"))

if userInput > randomNumber :
    print(randomNumber)
    print("The number is to high")
elif userInput < randomNumber :
    print(randomNumber)
    print("the number is to low")
else:
    print(randomNumber)
    print("yes, you have matched the number")