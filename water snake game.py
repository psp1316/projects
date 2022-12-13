import random

opt=["stone","paper","scissor"]

write=False

def cpu():
    return random.choice(opt)

def game():
    score=0 
    print("Chose any one from here: ",opt)
    
    for i in range(0,3):
        uc=input("Enter your choice here: ") 
        cc=cpu()
        if uc=="stone":
         if cc=="stone":
             print("Computer chose: ",cc,"\nIts's a draw!")
         elif cc=="paper":
             print("CPU chose: ",cc,"\n You Lost!")
         elif cc=="scissor":
             print("CPU chose: ",cc,"\n You Won! Congrats ;)")
             score+=1

        if uc=="paper":
         if cc=="paper":
             print("Computer chose: ",cc,"\nIts's a draw!")
         elif cc=="scissor":
             print("CPU chose: ",cc,"\n You Lost!")
         elif cc=="stone":
             print("CPU chose: ",cc,"\n You Won! Congrats ;)")
             score+=1

        if uc=="scissor":
         if cc=="scissor":
             print("Computer chose: ",cc,"\nIts's a draw!")
         elif cc=="stone":
             print("CPU chose: ",cc,"\n You Lost!")
         elif cc=="paper":
             print("CPU chose: ",cc,"\n You Won! Congrats ;)")
             score+=1
    
    return score

def fappend(score):
    with open("hiscore.txt","r") as f:
        s=int(f.read())
    
    if s<score:
        with open("highscore.txt","w") as f:
            f.write(str(score))
         
def fread():
    with open("Chapter 9/highscore.txt") as f:
        hiscore=f.read()
    return hiscore


# with open("Highscore.txt") as f:



print("\n\n       -----< Hi, Let's Begin the Game >-----     ")
score=game()
print("Your score was: ",score)
fappend(score)
hiscore=fread()
print("\nHigh Score is: ",hiscore)