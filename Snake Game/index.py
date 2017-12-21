import pygame
import time
import random

pygame.init()
#vars
width = 600
height = 400
title = 'Snake Game'
FPS = 20
black = (52, 73, 94)
white = (236, 240, 241)
red = (231, 76, 60)
blue = (52, 152, 219)
green = (46, 204, 113)
yellow = (241, 196, 15)
gray = (149, 165, 166)
size = 20

#end vars
snake_load = pygame.image.load('Snake.png')
apple_load = pygame.image.load('Apple.png')
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()

def player(size,snakelist):
	for XnY in snakelist:
		Snake = pygame.transform.scale(snake_load, (size, size))
		screen.blit(Snake,(XnY[0],XnY[1]))
		#pygame.draw.rect(screen,green,[XnY[0],XnY[1],size,size])	

def apple(ranx,rany,size):
	Apple = pygame.transform.scale(apple_load, (size, size))
	#pygame.draw.rect(screen,red,[ranx,rany,size,size])
	screen.blit(Apple,(ranx,rany))
font = pygame.font.Font('Ubuntu.ttf',50)
def message(msg,color):
	text = font.render(msg,True,color)
	screen.blit(text,[height/2,width/2])
	
def gameLoop():	
	lead_x = width/2
	lead_y = height/2
	x_change = 0
	y_change = 0
	Exit = False
	gameOver = False
	snakeList = []
	length = 1
	screen.fill(white)
	ranx = round(random.randrange(0,width-size)/20.0)*20.0
	rany = round(random.randrange(0,height-size)/20.0)*20.0
	while not Exit:
		screen.fill(white)
		apple(ranx,rany,size)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Exit = True
			if event.type == pygame.KEYDOWN:
				if  event.key == pygame.K_UP:
					y_change = -size
					x_change = 0
				if  event.key == pygame.K_DOWN:
					y_change = size
					x_change = 0
				if  event.key == pygame.K_LEFT:
					x_change = -size
					y_change = 0
				if  event.key == pygame.K_RIGHT:
					x_change = size
					y_change = 0
				if  event.key == pygame.K_a:
					length += 1
		lead_y = (lead_y + y_change) % height
		lead_x = (lead_x + x_change) % width
		while gameOver == True:
			screen.fill(white)
			message("You Lose",red)
			pygame.display.update()
			time.sleep(2)
			gameLoop()
		for eachseg in snakeList[:-1]:
			if eachseg == snakeHead:
				gameOver = True
		if lead_x == ranx and lead_y == rany:
			ranx = round(random.randrange(0,width-size)/20.0)*20.0
			rany = round(random.randrange(0,height-size)/20.0)*20.0
			length += 1
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		if len(snakeList) > length:
			del snakeList[0]
			
		player(size, snakeList)
		snakeH_load = pygame.image.load('Snake Head.png')
		Snake_Head = pygame.transform.scale(snakeH_load, (size, size))
		screen.blit(Snake_Head,(lead_x,lead_y))
		#pygame.draw.rect(screen,green,[lead_x,lead_y,size,size])	
		pygame.display.update()
		clock.tick(FPS)

	pygame.quit()
	quit()

gameLoop()
