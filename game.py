import random

list = ["rock", "paper", "scissors"]

user_score = 0
prog_score = 0

while user_score < 3 and prog_score < 3:
   # User choice
   user_choice = input("What do you choose: ")
   if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
      # Program choice
      for i in list:
         prog_choice = random.choice(list)

      print("I choose ", prog_choice)

      if prog_choice == user_choice:
         print("Draw, score is: "+str(prog_score)+" : "+str(user_score))
      elif (prog_choice == "paper" and user_choice == "rock") or (prog_choice == "scissors" and user_choice == "paper") or (prog_choice == "rock" and user_choice == "scissors"):
         prog_score += 1
         if prog_score == 3:
            print("I win, Final score is: "+str(prog_score)+" : "+str(user_score))
         else:
            print("I win, score is: "+str(prog_score)+" : "+str(user_score))
      elif (prog_choice == "rock" and user_choice == "paper") or  (prog_choice == "paper" and user_choice == "scissors") or    (prog_choice == "scissors" and user_choice == "rock"):
         user_score += 1
         if user_score == 3:
            print("You Win, Final score is: "+str(prog_score)+" : "+str(user_score))
         else:
            print("You win, score is: "+str(prog_score)+" : "+str(user_score))
      else:
         print("An error happened")
   else:
      print("You have to choose either rock, paper or scissors")

