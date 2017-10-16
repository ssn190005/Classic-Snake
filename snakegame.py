# Snake Game!
# To run on cmd type py G:\\Android\\pythonpentest-master\\python.py
#Use pyinstaller to create executables

import pygame #graphics, sounds etc
import sys
import random #randomize items 
import time #sleep function


#check for initialization errors, if any
check_errors = pygame.init() #returns successful operations count and error count #(x,y) - Return a tuple
if check_errors[1] > 0:
	print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
	sys.exit(-1)
else:
	print("(+) PyGame successfully initialized!")


# Play arena
playSurface = pygame.display.set_mode((720,460)) #accepts a tuple
pygame.display.set_caption('Snake Game!!!')
#time.sleep(5)

# Colors
red = pygame.Color(255,0,0) #gameover #rgb values, 0-255 each
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #bg
brown = pygame.Color(165,42,42) #food - search brown rgb code

# Game variables properties

#Frames per second controller
fpsController = pygame.time.Clock() # time tracker per frame 

# Snake
snakePos = [100,50] #coordinates of snake head
snakeBody = [[100,50],[90,50],[80,50]] #3 block size snake

#Food properties
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10] #random positioning with 10 unit sizes
foodSpawn = True #boolean check for whether or not food has been spawned

#Direction
direction = 'RIGHT'
changeto = direction

#Scoring
score = 0

#Gameover function
def gameOver():
	myFont = pygame.font.SysFont('monaco',72)
	GOsurface = myFont.render('Game Over!!!',True,red) #2nd argument is about aliasing
	GOrect = GOsurface.get_rect()
	GOrect.midtop = (360,15)
	playSurface.blit(GOsurface,GOrect)
	showScore(0)
	pygame.display.flip()
	time.sleep(4)
	pygame.quit() # For game surface
	sys.exit() # For console


def showScore(choice = 1):
	sFont = pygame.font.SysFont('monaco',24)
	Ssurf = sFont.render('Score : {0}'.format(score),True,black)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (80,10)
	else:
		Srect.midtop = (360,120)
	playSurface.blit(Ssurf,Srect)


#Events - Main game logic

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type ==pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'): #wasd also available
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'): #wasd also available
				changeto = 'LEFT'
			if event.key == pygame.K_DOWN or event.key == ord('s'): #wasd also available
				changeto = 'DOWN'
			if event.key == pygame.K_UP or event.key == ord('w'): #wasd also available
				changeto = 'UP'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))


	# Validation of direction
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	#Altering direction of snake based on validation
	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10
	if direction == 'UP':
		snakePos[1] -= 10

	#Snake body mechanisms
	snakeBody.insert(0,list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		foodSpawn = False
		score += 1
	else:
		snakeBody.pop()

	if foodSpawn == False:
		foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
	foodSpawn = True


	#Drawing Graphics
	playSurface.fill(white) #color
	for pos in snakeBody:
		pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))

	#Draw food
	pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))

	#Check walls
	if snakePos[0] > 710 or snakePos[0] < 0:
		gameOver()
	if snakePos[1] > 450 or snakePos[1] < 0:
		gameOver()

	#Check hitting snake body
	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]:
			gameOver()



	pygame.display.flip()
	showScore()
	pygame.display.flip()
	fpsController.tick(15)