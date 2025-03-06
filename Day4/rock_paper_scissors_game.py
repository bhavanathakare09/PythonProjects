import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
'''

user_input = input("Enter your choice as Rock, Paper, Scissors \n").lower()
if user_input == "rock":
    user_input = 0
elif user_input == "paper":
    user_input = 1
elif user_input == "scissors":
    user_input = 2

r_p_s = [rock,paper,scissors]
# computer_choice = random.choice(r_p_s)
# print(f"Computer choice: {computer_choice}")
computer_choice = random.randint(0,2)
print(computer_choice)

if user_input == 0 and computer_choice == 0:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("Play again")
elif user_input == 1 and computer_choice == 1:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("Play again")
elif user_input == 2 and computer_choice == 2:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("Play again")




# r_p_s = [rock,paper,scissors]
elif user_input == 0 and computer_choice == 1:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("Computer beats you!!, You are loss!!")
elif user_input == 0 and computer_choice == 2:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("You beat computer, You are win!!")


elif user_input == 1 and computer_choice == 0:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("You beat computer, You are win!!")
elif user_input == 1 and computer_choice == 2:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("Computer beats you!!, You are loss")

elif user_input == 2 and computer_choice == 0:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("Computer beats you!!, You are loss")
elif user_input == 2 and computer_choice == 1:
    print(f"user_input is : {r_p_s[user_input]}")
    print(f"computer_choice is: {r_p_s[computer_choice]}")
    print("You beat computer, You are win!!")



