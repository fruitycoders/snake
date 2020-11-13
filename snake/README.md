# SNAKE GAME
A classic spinoff of the game SNAKE that we designed with features such as: a variety of difficulties, and a tutorial.

## Main Menu Code Instructions
1. When you run the code, a brief ascii snake animation will run. It is a yellow snake moving across the screen, left to right.
2. Then, you will be prompted to choose from the main menu. Your choices are: tutorial, play, and exit.
3. If you choose “tutorial”, you will be given printed instructions on how to play the game. Then you will be prompted to choose another choice on the main menu.
4. If you choose “play”, you will be able to choose your level of difficulty. Your choices are easy, medium, and hard. The the game will start in the pygame screen.
5. If you choose “exit”, then you will exit the code.

## Snake PyGame Code Instructions
1. Click on the pygame screen and any of the arrow keys to start moving the snake.
2. Use the arrow keys to move the snake around the screen. The "snake" is a blue dot.
3. The object of the game is to collect as many "fruits," the red dots, as possible and not touch the borders.
4. As you collect the fruits, they will reappear in random places

## Log
* Oct 3-5
  - Made finished touches on the project and finished the actual game.
  - added detection of food and random reappearance of fruit.
* Oct 2
  - game window was not appearing; we figured out that commands in () could not be used to replace [], so we changed that.
  - snake was not moving to the top and right parts of the screen > fixed a bug in the width and height movement code
  - arrow key codes were not working > made some direction commands capitalized (for example, k_left should have been K_LEFT for the code to work)
  - made speed delay 8 for the easiest level, 10 for medium, and 12 for hard (not sure if this works)
* Oct 1
  - moved code form python to pygame on repl.it
  - turned off code for main menu for now
  - wrote simple code to move object (snake) with arrow keys
* Sept 29
  - updated "readme" file
  - incorportated lists and arrays into code for printing the snake
  - used iteration for printing the snake
  - refined and removed unnecessary or dead code
* Sept 25
  - main menu with functions and "try" statements
  - incorportated other files using "import"
  - created animation with ascii art
  - used iterations for animation function
  - added a "readme" file
* Sept 18
  - main menu using "if" statements and "print" statements
  - added color codes for changing snake color


## Overview Of Provided Code
- Main.py : Menu for our game where it shows 5 different items, the title for our game, the tutorial for our game, the play button, and the option to choose what you want to do.
- Easy.py : The easy mode for our game where the game is speed is slow. Shows all the code for that option.
- Medium.py : Shows all the code for the hard mode of our game. Game speed is faster.
- Hard.py : Shows all the code for the hard version of our game. Game speed is fastest.

## Algos and Programming
- Strings, Numbers : Strings and numbers were heavily used in the menu, specifically for the user input. They input an integer for the main menu, and input a string for the submenus. Many strings are also printed as well.
- Variables and Assignments : While creating the menu and the snake itself, we used many variables. For example, the main menu input variable is called "answer." In the snake code, to move the snake across the screen, we had to assign a couple variables at the beginning before we could move forward with out animation. Variable were assigned all throughout the code, even in the pygame code.
- Lists, Dictionaries : We used a list for the snake animation. Originally, it was print statements lined up in a row, but now it is much more condensed after making each print line into a value in a list. Now to print every line, we simple use the "for" loop.
- Iteration : Iteration is used in the animation to print the snake multiple times so that it looks like it is moving. We also used the "for" loop to print the snake intially too because each line of the snake is in a list. The "while" loop was also used in the pygame code too in order to move the snake forward without having to constantly press the arrow keys.
- Functions : Functions were used heavily in the menu. They were used to call other files as well. "Pygame.init()" is an example of how the "easy" "medium" and "hard" files are called in the menu.

## Purpose
- Foundation in social media using Slack, Padlet and Zoom.
- Establishing (a digital) relationship with our Pair/Trio team member(s), project team, and teacher.
- Foundation in Python coding using Repl.it.
- Using and Understanding AP CSP Course Requirements
- Installing future foundational technical tools for class, namely: IntelliJ IDE. GitHub Version Control.
- Establishing assesment and grading practices. Learning about Sprints and Deliberables.

## Project
- Critical Thinking, Program, Design, Logic, Implementation - CaTP 1, 2, 3: design, documentation of goals prior to implementaton, coding, algorithms, and meeting technical goals. 25%
- Communication and Presentation, Testing - CaTP 4, 5: Evidence showing completenes according to design and goals. Ability of Teacher to understand procedures, ability of Teacher to understand instructions or videos, showing how to run and execute. Code organization, comments, documentation are all part of communication. 25%
- Collaboration, CaTP 6: Collabortive in the development of a solution, acknowledging contribution of others, appropriate behaviors and employing ethics (ie no copying). Performing peer evaluations as requested by Teacher. 25%
- Creativity and Intangibles: The intagibles are participation, active learning, being proactive, genuine effort, positve attitude, inside-outside-the-box efforts. Creativity is running with an idea, being exited about that idea, and attempting a techncial design and solution (note: sometimes it is ok if that idea does not completely work) 25%
- Note: Grading will be highly influenced by Scrum team and individuals assesment.

## Map of provided Code to AP CSA requirements
| Unit | Percentage | Hello Series usage |
| ------------- | ----------- | ----------- |
|  Big Idea 1: Creative Computing | 10-13% | The comments of this project are full of exploration ideas, Zoom, Cavas and Slack will promote collaboration |
|  Big Idea 2: Data | 17-22% | Easy, Medium, and Hard are programs that illustrate data use and extraction |
|  Big Idea 3: Algorithms and Programming | 30-35% | Main uses conditionals and recursion.  Gridlines and Fruit uses iteration. |
|  Big Idea 4: Computer Systems and Network | 11-15% | Repl.it is a group of computer systems that provide our Python coding learning environment  |
|  Big Idea 5: Impact of Computing | 21-26% |  Distance Learning is made possible to us today via the impacts of computing |

### Authors
Adam Holbel, Linda Long, Wenshi Bao, Sophie Lee, and Maggie Killada