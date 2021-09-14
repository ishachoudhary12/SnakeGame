import random
print("Welcome! in Snake Gun Water Game\n")
name=str(input("Enter your name:"))
v=int(input("Enter 1 for play game and 2 for rules of the game:"))
a=0 #intialising a with zero
computer_p=player_p=0 #initialising computer and player score with zero
if v==2:
    print(" 1.The snake drinks water\n 2.The gun shoots snake\n 3.Gun was drowning in the water")
print("Game start!")
while a<10: 
    computer=random.choice("S,G,W")
    player=str(input("Enter S,G,W:"))
    if computer=="S" or computer=="s" and player=="W" or player=="w":
        print("Computer won")
        computer_p+=1
    elif computer=="W" or computer=="w" and player=="S" or player=="s":
        print("You Win")
        player_p+=1
    elif computer=="G" or computer=="g" and player=="W" or player=="w":
        print("You Win")
        player_p+=1
    elif computer=="W" or computer=="w" and player=="G" or player=="g":
        print("Computer won")
        computer_p+=1
    elif computer=="G" or computer=="g" and player=="S" or player=="s":
        print("Computer won")
        computer_p+=1
    elif computer=="S" or computer=="s" and player=="G" or player=="g":
        print("You Win")
        player_p+=1
    a+=1
if computer_p>player_p:
    print("Computer is The Winner!")
else:
    print(f"{name} is The Winner!")
print(f"{name} won{player_p}times\n")
print(f"computer won{computer_p}times")
print("Game Over!")    
