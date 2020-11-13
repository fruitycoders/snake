import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))

horizontal = random.randint(0, 780)
vertical = random.randint(0,580)

speed = 6

# snake starting point
x = 400
y = 300

# snake size
width = 20
height = 20

# colors
red = (242, 103, 74)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (55, 118, 171)
green = (0, 201, 87)

# snake movement
run = True
last_key = pygame.key.get_pressed()

while run:
  pygame.time.delay(10)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
      x -= speed 
      last_key = keys
    elif keys[pygame.K_RIGHT] and x<800-width:
      x += speed
      last_key = keys
    elif keys[pygame.K_UP] and y>0:
      y -= speed
      last_key = keys
    elif keys[pygame.K_DOWN] and y<600-height:
      y += speed
      last_key = keys

  if last_key[pygame.K_LEFT] and x>0:
    x -= speed 
  if last_key[pygame.K_RIGHT] and x<800-width:
    x += speed
  if last_key[pygame.K_UP] and y>0:
    y -= speed
  if last_key[pygame.K_DOWN] and y<600-height:
    y += speed


  screen.fill((black))
  pygame.draw.ellipse(screen, red, (horizontal, vertical, 20, 20))
  pygame.draw.ellipse(screen, (blue), (x, y, width, height))
  pygame.display.update()
  
  if x == 765 or x < 10 or y < 10 or y == 570:
    pygame.quit()

  if (x-horizontal) < 10 and (y-vertical) < 10:
    horizontal = random.randint(0, 780)
    vertical = random.randint(0,580)

# end of game
pygame.quit()