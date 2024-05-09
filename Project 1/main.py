import random
def check (comp,user):
    if (user == comp):
        return 0
    if (comp == 0 and user==-1):
        return 1
    if (comp == 1 and user == 0):
        return 1
    if (comp == -1 and user==1):
        return 1
    else:
        return -1
    

comp =  (random.randint(-1,1))
user = int(input("Players turn: 0 for snake, 1 for water and -1 for gun: "))
print ("You Choose: ", user)
print ("Computer Choosed: ", comp)
print ("Result: \n", end="")



a = check(comp,user)
if a == 0:
    print ("Its a draw. Play again")
elif a == 1:
    print ("User Wins")
elif a == -1:
    print ("Computer Wins")

