import time
from time import sleep

name = input("Enter Your Name:")

print("Hello"+ name)
print("Get Ready!!")

print("")

time.sleep(1)

print("Let us play hangman!!")
time.sleep(0.5)

word = "FLOWER"

wrd = ""

chance = 10

while chance > 0:
    failed = 0
    for char in word:
        if char in wrd:
            print(char)
        else:

            print("_")
            failed+=1


    if failed == 0:
        print("WELL DONE YOU WON!!!")

        break
    guess = input("Guess a letter!")

    wrd = wrd+guess

    if guess not in word:
        chance-=1

        print("Wrong Guess! Try Again")
        print("You Have", + chance, "MORE TURN")

        if chance == 0:
            print("You Lose Better Luck Next Time!")
