import random

def game(comp,you):
    if comp==you:
        print("IT'S A TIE!")


    if comp=="snake" and you=="water":
        print("HURRAY!!! YOU WON")
    elif comp=="water" and you=="snake":
        print("YOU LOSE!")
    
    if comp=="gun" and you=="water":
        print("HURRAY!!! YOU WON")
    elif comp=="water" and you=="gun":
        print("YOU LOSE!")

    if comp=="snake" and you=="gun":
        print("HURRAY!!! YOU WON")
    elif comp=="gun" and you=="snake":
        print("YOU LOSE!")
        
        
        


print('''Here is an interesting game for you!!!!
In this game you are competing against the computr by choosing an option from snake,water or gun
\n
\nrules:
1. If you choose water and the computer chooses snake then the water drowns the snake and you WIN and vice versa
2.  If you choose snake and comp choose gun you LOSE and vice versa\n GOOD LUCK...''')
print("\n")
print("Computer's turn: Choose snake, water, gun :")
print("\n")
print("Comp is done choosing! now its your turn")
rm=random.randint(1,3)
if rm==1:
    comp="snake"
if rm==2:
    comp="water"
if rm==3:
    comp="gun"
print("\n")
you= input("Your turn: Choose snake, water, gun :")
a=game(comp,you)

print(f"Comp chose: {comp}")
print(f"you chose: {you}")
