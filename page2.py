import pygame,sys
import pygame.gfxdraw
import pygame.draw
import random
pygame.init()

black=(0,0,0)
grey = (100,100,100)
white = (255,255,255)
brown=(102,51,0)
lightBrown=(153,76,0)
purple=(100,0,100)
red=(153,0,0)
green=(0,153,0)
blue=(0,0,153)
skyBlue=(0,255,255)
yellow=(204,204,0)
dirtyWhite=(200,200,200)
b_red=(200,0,0)
b_green=(0,200,0)
b_purple=(153,0,153)

size = width, height = 1050, 1020
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LUDO")
screen.fill(skyBlue)
	
player_list = []

#font = pygame.font.SysFont(None,50)
def message(msg,color,font_size,display_width,display_height):
	font = pygame.font.Font('freesansbold.ttf',font_size)
	text = font.render(msg,True,color)
	screen.blit(text,[display_width,display_height])

def mouse_click(x,y,w,h,ic,ac,text,text_size,text_color):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	#print("inmouse",mouse)
	if x+w>mouse[0]>x and y+h>mouse[1]>y:
		pygame.draw.rect(screen,ac,[x,y,w,h])
		message(text,text_color,text_size,x+10,y+10)
		if(click[0]==1):
			return True
		else:
			return False
	else:
		pygame.draw.rect(screen,ic,[x,y,w,h])
		message(text,text_color,text_size,x+10,y+10)
		return False
			

def name(color,wdt,ht,n):
	name = "NONE"
	bla = True
	text = "PLAYER_" + str(n)
	font = pygame.font.Font(None, 50)
	pygame.draw.rect(screen,color,[width/6 ,ht,200,50])
	message(text,black,30,width/6+25,ht+10)
	pygame.draw.rect(screen,white,[width/2,ht,225,50])
	
	pygame.draw.rect(screen,black,[width-200,ht+10,100,30])
	message("SUBMIT",white,20,width-200+10,ht+20)
	
	#mouse_click(width-200,ht+10,100,30,black,grey)
	while bla:
		#pygame.draw.rect(screen,purple,[350,height-200,100,50])
		#message("BACK",dirtyWhite,30,350+10,height-200+10)
		#mouse_click(350,height-200,100,50,purple,b_purple,"BACK",30,dirtyWhite)
		for evt in pygame.event.get():
			if evt.type == pygame.KEYDOWN:
				if evt.unicode.isalpha():
					name += evt.unicode
				elif evt.key == pygame.K_BACKSPACE:
					name = name[:-1]
			if evt.type == pygame.QUIT: sys.exit()
		if mouse_click(width-200,ht+10,100,30,black,grey,"SUBMIT",20,white) == True:
			bla = False
                
		pygame.draw.rect(screen,white,[width/2,ht,225,50])
		block = font.render(name,True,color)
		screen.blit(block, [width/2+25,ht+10])
		pygame.display.update()
	return name
def page2():
	flag = True
	page2 = True	
	screen.fill(skyBlue)
	while page2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		message("ENTER PLAYER NAMES",black,50,width/4,height/8)
		#pygame.draw.rect(screen,purple,[350,height-200,100,50])
		#message("BACK",dirtyWhite,30,350+10,height-200+10)
		#mouse_click(350,height-200,100,50,purple,b_purple,"BACK",30,dirtyWhite)
		if(flag):
			player_list.append(name(b_red,width,height/4,1))
			player_list.append(name(b_green,width,3*height/8,2))
			player_list.append(name(blue,width,height/2,3))
			player_list.append(name(yellow,width,5*height/8,4))
			flag = False
		pygame.draw.rect(screen,purple,[width-350,height-200,100,50])
		message("PLAY",dirtyWhite,30,width-350+10,height-200+10)
		if(mouse_click(width-350,height-200,100,50,purple,b_purple,"PLAY",30,dirtyWhite)==True):
			page2 = False
		pygame.display.update()	
		if(page2 == False):
			return player_list


if __name__ =="__main__":
	page2()




