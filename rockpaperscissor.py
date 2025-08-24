import random

print("Rules of the game are: \n" 
      + "Rock vs Paper ->Paper wins\n"
      + "Rock vs Scissor ->Rock Wins\n"
      + "Paper vs Scissor->Scissor Wins\n")

while True:
    print("Enter your Choice \n 1 - Rock\n 2 - Paper\n 3 - Scissor\n")

    choice = int(input("Enter your choice:"))

    while choice >3 or choice <1 :
        choice = int(input("Enter a valid choice:"))

    if choice ==1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    print("your choice is:",choice_name)
    print("Computer's turn...")

    comp_choice = random.randint(1,3)

    if comp_choice ==1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("Computer's choice is:", comp_choice_name)
    print(choice_name, "vs" , comp_choice_name)

    if choice == comp_choice:
        result = "Draw"
    elif (choice ==1 and comp_choice ==2) or(comp_choice ==1 and choice == 2):
        result = 'Paper'
    elif(choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = "Rock"
    elif(choice == 2 and comp_choice == 3) or (comp_choice ==3 and choice == 3):
        result = 'Scissor'

    if result == "Draw":
        print("its a tie.")
    elif result == choice_name:
        print("you win")
    else:
        print("Computer wins")

    print("do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == "n":
        break

print("thankyou")
