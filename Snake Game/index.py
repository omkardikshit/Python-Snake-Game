import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,53,45)
green = (255,255,255)

screen_width = 600
screen_height = 400
game_Name = "Snake Game !"
Display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(game_Name)
#surface = pygame.image.load('download.jpg')
#pygame.display.set_icon(surface)
clock = pygame.time.Clock()
block_size = 20
FPS = 18

font = pygame.font.SysFont(None,22)

def snake(block_size,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(Display,white,[XnY[0],XnY[1],block_size,block_size])

def message(msg,color):
    screen_text = font.render(msg,True,color)
    Display.blit(screen_text,[screen_height/2,screen_height/2]);


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = screen_width/2
    lead_y = screen_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0,screen_width-block_size)/20.0)*20.0
    randAppleY = round(random.randrange(0,screen_height-block_size)/20.0)*20.0

    while not gameExit:

        while gameOver == True:
            Display.fill(black)
            message("Game Over, Press C to Continue or Press Q to Quit" , red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        lead_x = (lead_x + lead_x_change) % screen_width
        lead_y = (lead_y + lead_y_change) % screen_height
        #if lead_x <= 0+2 or lead_x >= screen_width+2 or lead_y <= 0+2 or lead_y >= screen_height+2:
            #gameOver = True

        Display.fill(black)
        pygame.draw.rect(Display,red,[randAppleX,randAppleY,block_size,block_size])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size,snakeList)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0,screen_width-block_size)/20.0)*20.0
            randAppleY = round(random.randrange(0,screen_height-block_size)/20.0)*20.0
            snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()
gameLoop()
