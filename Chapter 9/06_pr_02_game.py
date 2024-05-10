def game():
    return 9251

score = game()
with open ("hiscore.txt") as f:
    highscore = f.read()

if highscore == "":
    with open ("hiscore.txt", "w") as a:
        a.write(str(score)) 
    print ("The high score is beaten and new high score is: ", score)
    
elif score>int(highscore) :
    with open ("hiscore.txt", "w") as a:
        a.write(str(score)) 
    print ("The high score is beaten and new high score is: ", score)


else:
    print ("The high score is not beaten which is: ", highscore)



