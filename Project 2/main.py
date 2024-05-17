import random

randNo = random.randint(1,100)
guess = None
guessTimes = 0
while (guess!= randNo):
    guess = int(input("Enter you guess. Choose number from 1 to 100: "))
    guessTimes = guessTimes +1
    if guess == randNo:
        print ("You guessed the correct number")
    else:
        if guess> randNo:
            print ("Wrong! The num you guessed is higher than actual number")
        else:
            print ("Wrong! The number you have guessed is lower than actual number")

print (f"You have guessed {guessTimes} number of times")


with open ("Highscore.txt") as f:
    a = int(f.read())

if guessTimes<a:
    print ("You have set the highscore mate")
    with open ("Highscore.txt", "w") as f:
        f.write(str(guessTimes))






