import art
from replit import clear
import random
while 1:
  print(art.logo)
  print("Welcome to the number guessing game")
  print("I'm thinking of a number between 1- 100")
  computer_guess = random.choice(range(1,100))
  level = input("Choose the level of difficulty you want, easy or hard : ")
  if level.lower() == "easy":
    game_chance = 10
  elif level.lower() == "hard":
    game_chance =5
  while game_chance:
    user_guess = int(input(f"You have {game_chance} attempt left\nMake a guess :"))
    if user_guess > computer_guess:
      game_chance-=1
      if game_chance ==0:
        break
      print("Too high\nMake a Low guess")
    elif user_guess < computer_guess:
      game_chance-=1
      if game_chance ==0:
        break
      print("Too low\nMake a High Guess")
    elif user_guess == computer_guess:
      print(f"{art.won}\nthe number is {computer_guess}")
      break
  if user_guess!=computer_guess:
      print(f"{art.lost}\nthe computer stimulated no is : {computer_guess}")
  want_to_play = input("Wanna play again, Y (or) N : ")
  if want_to_play.lower() == "y":
      clear()
      continue
  elif want_to_play.lower() == "n":
      print("Thanks for playing the game")
      break
