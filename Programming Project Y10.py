#Rules
#1)If a player rolls an even number (2,4), the player gains 10 points
#2)If a player rolls an odd number (1,3,5), the player loses 5 points
#3)If a player rolls a 6, the player gains 10 points and another turn to roll
#4)Your score cannot go below 0

#There will be 5 rounds
#If both players' scores are tied at the end of the game, there will be a
#continued tie-breaker. The game continues until one player has a higher score
#than the other player.
#The rules above still apply

print("""Rules:
-----
1)If a player rolls an even number (2,4), the player gains 10 points
2)If a player rolls an odd number (1,3,5), the player loses 5 points
3)If a player rolls a 6, the player gains 10 points and another turn to roll
4)Your score cannot go below 0

You will need to type in your username password to start

#There will be 5 rounds\n
If both of the player's scores are tied at the end of the game, there will be a
continued tiebreaker. The game continues until one player has a higher score
than the other player
#The rules above still apply\n""")

userInput = input("Press 'A' to start:\n")
if userInput == "A":
      print("Let's begin!\n")
while userInput != "A":
    userInput = input("Press 'A' to start:\n")
    if userInput == "A":
      print("Let's begin!\n")
      
#Constants
import random
import csv
Total1 = 0
Total2 = 0
rounds = 0
turns = 0
round_array = [0,1,2,3,4,5]
odd_number_array = [1,3,5,7,9,11]
odd_numbers = 1 or 3 or 5 or 7 or 9 or 11
even_number_array = [2,4,6,8,10,12]
even_numbers = 2 or 4 or 6 or 8 or 10 or 12
player1_password = "SMH1V"
player2_password = "FFH?M"

#Username - Player1
username1 = input("Player1, Enter your username:\n")
print("Welcome,", username1, "\n")

#Username - Player2
username2 = input("Player2, Enter your username:\n")
print("Welcome,", username2, "\n")

#Password - Player 1
player1 = input(username1 + ", Enter your password:\n")
while player1 != player1_password:
    player1 = input(username1 + ", Enter your password:\n")
print("\n")
player1_validation = input("Enter your password again:\n")
if player1_validation != player1:
    while player1_validation != player1:
        player1_validation = input("Enter your password again:\n")
else:
    print("")
    print(username1, ", Access granted...")
print("\n")

#Password - Player 2
player2 = input(username2 + ", Enter your password:\n")
while player2 != player2_password:
    player2 = input(username2 + ", Enter your password:\n")
print("\n")
player2_validation = input("Enter your password again:\n")
if player2_validation != player2:
    while player2_validation != player2:
        player2_validation = input("Enter your password again:\n")
else:
    print("")
    print(username2, ", Access granted...")
print("\n")

#Rolling the dice - Rounds
while rounds != 5:
      rounds = rounds + 1
      if rounds == 5:
            print("Round 5 - Final Round")
      else:
            print("Round", round_array[rounds])

#Player1 - die
      for range in (0,1):
          player1_dice = random.randint(1,6)
          dice1 = input(username1 + ", press any key to roll the dice\n")
          if player1_dice == 6:
                while player1_dice == 6:
                      Total1 = Total1 + 10
                      print("Player1: ", player1_dice)
                      player1_dice = random.randint(1,6)
                      dice1 = input(username1 + ", press any key to roll the dice\n")
                      Total1 = Total1 + 10
          elif player1_dice == 5:
                if Total1 < 5:
                      Total1 = 0
                else:
                      Total1 = Total1 - 5
          elif player1_dice == 4:
                Total1 = Total1 + 10
          elif player1_dice == 3:
                if Total1 < 5:
                      Total1 = 0
                else:
                      Total1 = Total1 - 5
          elif player1_dice == 2:
                Total1 = Total1 + 10
          elif player1_dice == 1:
                if Total1 < 5:
                      Total1 = 0
                else:
                      Total1 = Total1 - 5
          print(username1,":", player1_dice, "\n")
      Complete_Total = Total1
      print("\n")
      print(username1, ": 2 roll dice Total Score = ", Complete_Total, "\n")
      print("\n")

#Player 2 - die
      for range in (0,1):
           turns = turns + 1
           player2_dice = random.randint(1,6)
           player2_dice2 = random.randint(1,6)
           dice2 = input("Player2, press any key to roll the dice\n")
           if turns == 1:
                 print(username2,": ", player2_dice, "\n")
           elif turns == 2:
                 print(username2,": ", player2_dice2, "\n")
           Complete_Total2 = player2_dice + player2_dice2
           print("Complete Total for 2 roll dice = ", Complete_Total2)
           if player2_dice == 6:
               while player2_dice == 6:
                   Total12 = Total2 + 10
                   print("Player2: ", player2_dice)
                   player2_dice = random.randint(1,6)
                   dice2 = input("Player2, press any key to roll the dice\n")
               Total12 = Total2 + 10
           elif player2_dice == 5 or 3 or 1:
               if Total2 < 5:
                   Total2 = 0
               else:
                   Total2 = Total2 - 5
           elif player2_dice == 4 or 2:
               Total2 = Total2 + 10
           elif player2_dice == 3:
               if Total2 < 5:
                   Total2 = 0
               else:
                   Total2 = Total2 - 5
           elif player2_dice == 2:
               Total2 = Total2 + 10
           elif player2_dice == 1:
               if Total2 < 5:
                   Total2 = 0
               else:
                   Total2 = Total2 - 5
           """if Complete_Total2  == odd_number_array[1 or 3 or 5 or 7 or 9 or 11]:
                 if Total2 < 5:
                       Total2 = 0
                 else:
                       Total2 = Total2 - 5
           elif Complete_Total2 == even_number_array[2 or 4 or 6 or 8 or 10 or 12]:
                 Total2 = Total2 + 10"""
           print("\n")
           print(username2,": 2 roll dice Total Score = ", Total2, "\n")
           print("\n")
           print("Current Score for ", username1, " = ", Total1)
           print("Current Score for ", username2, " = ", Total2)
           print("\n")

#Totals
print("Score for ", username1, " = ", Total1)
print("Score for ", username2, " = ", Total2)
print("\n")
if Total1 < Total2:
    file = open("testfile.txt","w")
    file.write(username2 + " wins!\n")
    file.write("Well done " + username2 + "!")
    file.close()
    file = open("testfile.txt","r")
    print(file.read())
    with open('scores.csv', 'w') as csvfile:
          scorewriter = csv.writer(csvfile, delimiter=',')
          scorewriter.writerow([username1 , Total1])
          scorewriter.writerow([username2 , Total2, 'Winner!'])
elif Total1 > Total2:
    file = open("testfile.txt","w")
    file.write(username1 + " wins!\n")
    file.write("Well done " + username1 + "!")
    file.close()
    file = open("testfile.txt","r")
    print(file.read())
    with open('scores.csv', 'w') as csvfile:
          scorewriter = csv.writer(csvfile, delimiter=',')
          scorewriter.writerow([username1, Total1, 'Winner!'])
          scorewriter.writerow([username2 , Total2])
elif Total1 == Total2:
    print("TIEBREAKER!")
    print("\n")
    
#Player1 - die - TieBreaker
while Total1 == Total2:
      for range in (0,1):
            player1_dice = random.randint(1,6)
            dice1 = input(username1 + ", press any key to roll the dice\n")
            if player1_dice == 6:
                  while player1_dice == 6:
                      Total1 = Total1 + 10
                      print("Player1: ", player1_dice)
                      player1_dice = random.randint(1,6)
                      dice1 = input(username1 + ", press any key to roll the dice\n")
                      Total1 = Total1 + 10
            elif player1_dice == 5:
                  if Total1 < 5:
                      Total1 = 0
                  else:
                      Total1 = Total1 - 5
            elif player1_dice == 4:
                  Total1 = Total1 + 10
            elif player1_dice == 3:
                  if Total1 < 5:
                      Total1 = 0
                  else:
                      Total1 = Total1 - 5
            elif player1_dice == 2:
                  Total1 = Total1 + 10
            elif player1_dice == 1:
                  if Total1 < 5:
                      Total1 = 0
                  else:
                      Total1 = Total1 - 5
            print(username1,":", player1_dice, "\n")
      Complete_Total = Total1
      print("\n")
      print(username1, ": 2 roll dice Total Score = ", Complete_Total, "\n")
      print("\n")


#Player2 - die - Tiebreaker
      dice2 = input("Player2, press any key to roll the dice\n")
      if player2_dice == 6:
            while player2_dice == 6:
                  Total2 = Total2 + 10
                  print("Player2: ", player2_dice)
                  player2_dice = random.randint(1,6)
                  dice2 = input("Player2, press any key to roll the dice\n")
                  Total2 = Total2 + 10
      elif player2_dice == 5:
            if Total2 < 5:
                Total2 = 0
            else:
                Total2 = Total2 - 5
      elif player2_dice == 4:
            Total2 = Total2 + 10
      elif player2_dice == 3:
            if Total2 < 5:
                Total2 = 0
            else:
                Total2 = Total2 - 5
      elif player2_dice == 2:
            Total2 = Total2 + 10
      elif player2_dice == 1:
            if Total2 < 5:
                Total2 = 0
            else:
                Total2 = Total2 - 5
      print("Player2: ", player2_dice)
      print("\n")
      print("Score for P1 = ", Total1)
      print("Score for P2 = ", Total2)
      print("\n")
    
    #TieBreaker Totals
if Total1 < Total2:
      file = open("testfile.txt","w")
      file.write(username2 + " wins!\n")
      file.write("Well done " + username2 + "!")
      file.close()
      file = open("testfile.txt","r")
      print(file.read())
      with open('scores.csv', 'w') as csvfile:
          scorewriter = csv.writer(csvfile, delimiter=',')
          scorewriter.writerow([username1 , Total1])
          scorewriter.writerow([username2 , Total2, 'Winner!'])
elif Total1 > Total2:
      file = open("testfile.txt","w")
      file.write(username1 + " wins!\n")
      file.write("Well done " + username1 + "!")
      file.close()
      file = open("testfile.txt","r")
      print(file.read())
      with open('scores.csv', 'w') as csvfile:
          scorewriter = csv.writer(csvfile, delimiter=',')
          scorewriter.writerow([username1, Total1, 'Winner!'])
          scorewriter.writerow([username2 , Total2])
