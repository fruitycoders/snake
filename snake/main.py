#SNAKE MENU
import pygame
import time

ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def snake_print(position):
  snake = ["                     ____", "                    / . .\ ", "                    \   ---<", "   _________________/ /", "  \__________________/"]
  print(ANSI_HOME_CURSOR)
  print(RESET_COLOR)
  sp = " " * position
  for line in snake:
    print("\033[1;33;93m" + sp +  line)
  print(RESET_COLOR)

def snake():
 
  start = 0        
  end = 50 
  step = 2
  
  for position in range(start, end, step):    
    snake_print(position)
    time.sleep(0.3)

#main menu
def main():
  snake()
  print(" ")
  print("SNAKE REMAKE!")
  print(" ")
  print("1: Tutorial")
  print("2: Play")
  print("0: Exit")
  
  try:
    answer = int(input("SELECT A NUMBER: "))
    if answer >= 4:
      print("INVALID NUMBER:", answer)
      return
    
    while answer < 4:
      if answer == 1:
        print("Tutorial: Control the snake using your arrow keys. Eat the fruit, and avoid moving off the screen or bumping into yourself. Get the as many fruits as you can!")
        answer = int(input("SELECT A NUMBER TO CONTINUE: "))
      elif answer == 2:
        print(" ")
        print("E: Easy")
        print("M: Medium")
        print("H: Hard")
        leveltype = input("SELECT A LEVEL: ")
        setlevel(leveltype)
        return
      elif answer == 0:
        return
      else:
        print("INVALID NUMBER: {answer}")
        return
  except ValueError:
    print("NOT A NUMBER")

def easy():
  import easy
  pygame.init()
def medium():
  import medium
  pygame.init()
def hard():
  import hard
  pygame.init()

def setlevel(leveltype):
  if leveltype == "E":
    print("Welcome to Easy Mode!")
    easy()
  elif leveltype == "M":
    print("Welcome to Medium Mode!")
    medium()
  elif leveltype == "H":
    print("Welcome to Hard Mode!")
    hard()
  else:
    print("INVALID INPUT:", leveltype)


main()