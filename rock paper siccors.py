import random
options=["Rock","Paper","Sciccors"]
user_choice=input("Choose Rock,Paper or Scissor")
computer_choice=random.choice(options)
print("You chose",user_choice)
print("Computer chose",computer_choice)
if user_choice == computer_choice:
    print("Its a tie")
elif user_choice =="Rock" and computer_choice =="Siccors":
    print("Rock smashes sciccors. You win")
elif user_choice =="Paper" and computer_choice == "Rock":
    print("You won paper beats rock")
elif user_choice=="Scissors" and computer_choice=="Paper":
    print("Sciccors beats paper . You win ")
else:
    print("You lose")