import pygame.gfxdraw
import pygame , sys
import pygame.draw
pygame.font.init()

size = width, height = 1050, 1020
screen = pygame.display.set_mode(size)
black=(0,0,0)
brown=(102,51,0)
lightBrown=(153,76,0)
purple=(100,0,100)
red=(153,0,0)
green=(0,153,0)
blue=(0,0,153)
skyBlue=(0,255,255)
yellow=(204,204,0)
dirtyWhite=(200,200,200)
x=(180,180,0)
b_red=(200,0,0)
b_green=(0,200,0)
b_purple=(153,0,153)
def button(text,x,y,w,h,c1,c2,objective=None):
	m = pygame.mouse.get_pos()
	c = pygame.mouse.get_pressed()
	if x < m[0] < x+w and y < m[1] < y+h:
		pygame.draw.rect(screen,c2,(x,y,w,h))
		if c[0]==1 and objective != None:

			objective()
			return False


	else:
		pygame.draw.rect(screen,c1,(x,y,w,h))
	font=pygame.font.Font('freesansbold.ttf',25)
	m = font.render(text, True, black)
	screen.blit(m,(x+(w/5),y+(h/3)))
	return True

def t_obj(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message(msg,color,font_size,display_width,display_height):
	font = pygame.font.Font('freesansbold.ttf',font_size)
	text = font.render(msg,True,color)
	screen.blit(text,[display_width,display_height])

def quitgame():
	pygame.quit()
def bekar():
	pass
def instructions():
	screen.fill(green)
	message("Instructions",black,115,200,100)
	message("1. There will be a label below the board which will dislay which ",black,30,50,300)
	message("   player's turn it is.",black,30,50,350)
	message("2. Press the space bar to roll dice. The number rolled will be ",black,30,50,430)
	message(" displayed on the screen.",black,30,50,480)
	message("3. Select the token to be moved by left clicking that token.",black,30,50,550)
	message("NOTE : You won't get an extra turn for rolling a six nor for ",red,30,50,610)
	message("   killing other players.",red,30,50,660)
	pygame.display.update()
	pygame.time.delay(7000)
	
def initial():
	page = True
	while page:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		screen.fill(x)
		message("LUDO",black,115,350,100)
		X=button("Play",400,250,200,60,green,b_green,bekar)
		Y=button("Instructions",400,350,200,60,purple,b_purple,instructions)
		Z=button("Quit",400,450,200,60,red,b_red,quitgame)
		pygame.display.update()
		if (X and Z)==False:
			page=False

if __name__=="__main__":

        initial()
