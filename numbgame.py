import random

startgame = input("Welcome to the numbers game! \n Try to guess the number between 1 and 100! \n Do you want to play? y/n - ")
if startgame == "y":
    print("Ok, lets start then!\n Tell a number between 1 and 100 \n I'll tell you if the number i'm thinking is higher lower or the match of your choice!")
    x = random.randint(1,100)
while True:
    frstinpu = input("Give me a number:")
    frstinpu = int(frstinpu)
    if frstinpu > x:
        print("Lower")
    if frstinpu < x:
        print("Higher")
    if frstinpu == x:
        print("That's right!")
        break