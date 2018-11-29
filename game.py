import pygame,sys
import pygame.gfxdraw
import pygame.draw
import page2
pygame.font.init()


size = width, height = 1050, 1020
screen = pygame.display.set_mode(size)


star_str="star.png"
star=pygame.image.load(star_str)
safePoint=[(150,500),(400,150),(750,400),(500,750),(500,100),(100,400),(800,500),(400,800)]


neon=(0,0,0)
black=(0,0,0)
brown=(102,51,0)
lightBrown=(153,76,0)
purple=(100,0,100)
l_red=(153,0,0)
l_green=(0,153,0)
l_blue=(0,0,153)
skyBlue=(0,255,255)
l_yellow=(204,204,0)
dirtyWhite=(200,200,200)
white =(255,255,255)
x=(180,180,0)
b_red=(200,0,0)
b_green=(0,200,0)
b_purple=(153,0,153)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
yellow=(255,255,0)


boundry_size=30
board_squ_x=50
board_squ_y=50
block_size=50
squ_size=350
board_size = squ_size*2 +block_size*3



board_boundry  = pygame.Rect(board_squ_x - boundry_size , board_squ_y - boundry_size , board_size + boundry_size*2, board_size + boundry_size*2)
size = width, height = 1050, 1020
screen = pygame.display.set_mode(size)
board_play  = pygame.Rect(board_squ_x , board_squ_y , board_size , board_size)
box1 = pygame.Rect(board_squ_x , board_squ_y , squ_size , squ_size)
box2 = pygame.Rect(board_squ_x +block_size*3 +squ_size ,board_squ_y ,squ_size ,squ_size)
box3 = pygame.Rect(board_squ_x , board_squ_y +block_size*3 +squ_size , squ_size , squ_size)
box4 = pygame.Rect(board_squ_x +block_size*3 +squ_size , board_squ_y +block_size*3 +squ_size , squ_size , squ_size)




def draw_grid(start_x,start_y,board_squ_x):
	i = board_squ_x
	while(i<board_squ_x + board_size):
		pygame.gfxdraw.hline(screen,start_x,start_x + board_size,i,black)
		pygame.gfxdraw.vline(screen,i,start_y,start_y + board_size,black)
		i+=board_squ_x

def draw_circles(X,Y,r):
	x=X+100
	y=Y+100
	pygame.gfxdraw.filled_circle(screen,x,y,r+2,black)
	pygame.gfxdraw.filled_circle(screen,x+150,y,r+2,black)
	pygame.gfxdraw.filled_circle(screen,x,y+150,r+2,black)
	pygame.gfxdraw.filled_circle(screen,x+150,y+150,r+2,black)

	pygame.gfxdraw.filled_circle(screen,x,y,r,dirtyWhite)
	pygame.gfxdraw.filled_circle(screen,x+150,y,r,dirtyWhite)
	pygame.gfxdraw.filled_circle(screen,x,y+150,r,dirtyWhite)
	pygame.gfxdraw.filled_circle(screen,x+150,y+150,r,dirtyWhite)

def addstar():
	for i in range(len(safePoint)):
		screen.blit(star,safePoint[i])


def board():
	screen.fill(black)
	pygame.gfxdraw.box(screen,board_boundry,brown)
	pygame.gfxdraw.box(screen,board_play,dirtyWhite)
	pygame.draw.polygon(screen,l_red,((100,400),(150,400),(150,450),(400,450),(400,500),(100,500)),0)
	pygame.draw.polygon(screen,l_blue,((550,100),(450,100),(450,400),(500,400),(500,150),(550,150)),0)
	pygame.draw.polygon(screen,l_green,((450,800),(450,550),(500,550),(500,850),(400,850),(400,800)),0)
	pygame.draw.polygon(screen,l_yellow,((550,450),(850,450),(850,550),(800,550),(800,500),(550,500)),0)
	draw_grid(board_squ_x,board_squ_y,board_squ_x)
	pygame.gfxdraw.box(screen,box1,l_red)
	pygame.gfxdraw.box(screen,box2,l_blue)
	pygame.gfxdraw.box(screen,box3,l_green)
	pygame.gfxdraw.box(screen,box4,l_yellow)
	pygame.draw.polygon(screen,l_red,((400,400),(475,475),(400,550)),0)
	pygame.draw.polygon(screen,l_blue,((400,400),(475,475),(550,400)),0)
	pygame.draw.polygon(screen,l_green,((400,550),(475,475),(550,550)),0)
	pygame.draw.polygon(screen,l_yellow,((550,400),(475,475),(550,550)),0)
	pygame.draw.rect(screen, black, [board_squ_x , board_squ_y , squ_size , squ_size], 2)
	pygame.draw.rect(screen, black, [board_squ_x +block_size*3 +squ_size ,board_squ_y ,squ_size ,squ_size], 2)
	pygame.draw.rect(screen, black, [board_squ_x , board_squ_y +block_size*3 +squ_size , squ_size , squ_size], 2)
	pygame.draw.rect(screen, black, [board_squ_x +block_size*3 +squ_size , board_squ_y +block_size*3 +squ_size , squ_size , squ_size], 2)
	pygame.draw.rect(screen, black, [400,400,150,150], 2)
	draw_circles(board_squ_x , board_squ_y,30)
	draw_circles(board_squ_x +block_size*3 +squ_size ,board_squ_y,30 )
	draw_circles(board_squ_x , board_squ_y +block_size*3 +squ_size,30)
	draw_circles(board_squ_x +block_size*3 +squ_size , board_squ_y +block_size*3 +squ_size,30)
	addstar()

	




#############################################################################################  TOKEN CLASS  #########################################################################################

board_places=[(100,400),(150,400),(200,400),(250,400),(300,400),(350,400),(400,350),(400,300),(400,250),(400,200),(400,150),(400,100),(400,50),(450,50),(500,50),(500,100),(500,150),(500,200),(500,250),(500,300),(500,350),(550,400),(600,400,),(650,400),(700,400),(750,400),(800,400),(850,400),(850,450),(850,500),(800,500),(750,500),(700,500),(650,500),(600,500),(550,500),(500,550),(500,600),(500,650),(500,700),(500,750),(500,800),(500,850),(450,850),(400,850),(400,800),(400,750),(400,700),(400,650),(400,600),(400,550),(350,500),(300,500),(250,500),(200,500),(150,500),(100,500),(50,500),(50,450),(50,400)]

red_home = [(i,450) for i in range(100,400,50)]
blue_home = [(450,i) for i in range(100,400,50)]
yellow_home = [(i,450) for i in range(800,500,-50)]
green_home = [(450,i) for i in range(800,500,-50)]
safePoint=[(150,500),(400,150),(750,400),(500,750),(500,100),(100,400),(800,500),(400,800)]
default_red = [(150-25,150-25),(300-25,150-25),(300-25,300-25),(150-25,300-25)]
default_blue =[(650-25,150-25),(650-25,300-25),(800-25,150-25),(800-25,300-25)]
default_green =[(150-25,650-25),(300-25,650-25),(150-25,800-25),(300-25,800-25)]
default_yellow =[(650-25,650-25),(800-25,650-25),(800-25,800-25),(650-25,800-25)]
home_base=[(450,450)]

active_tokens=[]
inactive_red=[]
inactive_blue=[]
inactive_green=[]
inactive_yellow=[]

active_red=[]
active_blue=[]
active_green=[]
active_yellow=[]

playtokens=[]
players=[]


def set_default(color):
	if color==red:
		l=inactive_red
		q=default_red
	elif color==blue:
		l=inactive_blue
		q=default_blue
	elif color==green:
		l=inactive_green
		q=default_green
	elif color==yellow:
		l=inactive_yellow
		q=default_yellow

	for i in range(len(l)):
		l[i].position=q[i]


def make_the_board():
	board={}
	for i in board_places:
		board[i]=[]
	for i in blue_home:
		board[i]=[]
	for i in red_home:
		board[i]=[]
	for i in green_home:
		board[i]=[]
	for i in yellow_home:
		board[i]=[]

	for i in default_red:
		board[i]=[]
	for i in default_blue:
		board[i]=[]
	for i in default_yellow:
		board[i]=[]
	for i in default_green:
		board[i]=[]
	for i in home_base:
		board[i]=[]


	return board	

theBoard=make_the_board()


class token:
	def __init__(self, color):
		self.color=color
		if self.color==red:
			self.pos_pointer=0
			self.position=board_places[self.pos_pointer]

		elif self.color==blue:
			self.pos_pointer=15
			self.position=board_places[self.pos_pointer]

		elif self.color==green:
			self.pos_pointer=45
			self.position=board_places[self.pos_pointer]

		elif self.color==yellow:
			self.pos_pointer=30
			self.position=board_places[self.pos_pointer]
		self.deactivate()



	def get_roll(self,dice):
		for i in theBoard[self.position]:                                    # we need to pop the token from the old position before appending it to the new location  theBoard[pos] 
			if i==self:
				theBoard[self.position].remove(i)
		if self not in active_tokens:
			if self.color==red:
				self.pos_pointer=0
	
			elif self.color==blue:
				self.pos_pointer=15
	
			elif self.color==green:
				self.pos_pointer=45
	
			elif self.color==yellow:
				self.pos_pointer=30

			self.activate()
		else:
			self.pos_pointer+=dice
			
		self.update_pos()
		self.place_token()



	def update_pos(self):
		if self.color==red:
			if self.pos_pointer>=len(board_places)-1:
				if self.pos_pointer<len(board_places)-1+len(red_home):
					self.position=red_home[self.pos_pointer-len(board_places)+1]
				else :
					self.position=home_base[0]
					active_red.remove(self)
			else:
				self.position=board_places[self.pos_pointer]

		elif self.color==blue:
			if self.pos_pointer>=len(board_places):
				if self.pos_pointer<len(board_places)+15-1:
					self.position=board_places[self.pos_pointer-len(board_places)]
				else:					
					if self.pos_pointer<len(board_places)+15-1+len(blue_home):
						self.position=blue_home[self.pos_pointer-len(board_places)-15+1]
					else:
						self.position=home_base[0]
						active_blue.remove(self)
			else:
				self.position=board_places[self.pos_pointer]

		elif self.color==green:
			if self.pos_pointer>=len(board_places):
				if self.pos_pointer<len(board_places)+45-1:
					self.position=board_places[self.pos_pointer-len(board_places)]
				else:
					if self.pos_pointer<len(board_places)+45-1+len(green_home):
						self.position=green_home[self.pos_pointer-len(board_places)-45+1]
					else:
						self.position=home_base[0]
						active_green.remove(self)
			else:
				self.position=board_places[self.pos_pointer]

		elif self.color==yellow:
			if self.pos_pointer>=len(board_places):
				if self.pos_pointer<len(board_places)+30-1:
					self.position=board_places[self.pos_pointer-len(board_places)]
				else:					
					if self.pos_pointer<len(board_places)+30-1+len(yellow_home):
						self.position=yellow_home[self.pos_pointer-len(board_places)-30+1]
					else:
						self.position=home_base[0]
						active_yellow.remove(self)
			else:
				self.position=board_places[self.pos_pointer]

	def display_token(self):
		x=self.position[0]
		y=self.position[1]
		pygame.gfxdraw.filled_circle(screen,x+25,y+25,25,self.color)

	def click_token(self ,die):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		x = self.position[0]
		y = self.position[1]
		w = 50
		h =50
		pygame.gfxdraw.filled_circle(screen,x+25,y+25,25,black)
		pygame.gfxdraw.filled_circle(screen,x+25,y+25,20,self.color)

		if x+w>mouse[0]>x and y+h>mouse[1]>y:
			if(click[0]==1):
				self.get_roll(die)
				return False
			else:
				return True
		else:
			return True



	def place_token(self):
		X=self.what_is_there()
		if X[0]:
			if X[1]:
				theBoard[self.position].append(self)
			else:
				self.reset_pos()                                #some reset function for theBoard[pos] that-is the whole list (not theBoard dictionary) 
				theBoard[self.position]=[self]
		else:
			theBoard[self.position].append(self)


	def what_is_there(self):
		if theBoard[self.position]==[] or self.position in safePoint or self.position==home_base[0]:
			return (False,True)
		else:
			if theBoard[self.position][0].color==self.color:
				return (True,True)
			else:
				return (True,False)



	def deactivate(self):
		for i in active_tokens:
			if i==self:
				active_tokens.remove(i)
		if self.color==red:
			inactive_red.append(self)
			if len(active_red)!=0:
				active_red.remove(self)
		elif self.color==blue:
			inactive_blue.append(self)
			if len(active_blue)!=0:
				active_blue.remove(self)
		elif self.color==green:
			inactive_green.append(self)
			if len(active_green)!=0:
				active_green.remove(self)
		elif self.color==yellow:
			inactive_yellow.append(self)
			if len(active_yellow)!=0:
				active_yellow.remove(self)


	def activate(self):
		active_tokens.append(self)
		if self.color==red:
			active_red.append(self)
			for i in inactive_red:
				if i==self:
					inactive_red.remove(i)
		elif self.color==blue:
			active_blue.append(self)
			for i in inactive_blue:
				if i==self:
					inactive_blue.remove(i)
		elif self.color==green:
			active_green.append(self)
			for i in inactive_green:
				if i==self:
					inactive_green.remove(i)
		elif self.color==yellow:
			active_yellow.append(self)
			for i in inactive_yellow:
				if i==self:
					inactive_yellow.remove(i)


	def reset_pos(self):
		for i in theBoard[self.position]:
			i.deactivate()
			color=i.color
		set_default(color)



'''
we can make a global dictionary of positions as key values and empty list as the value 
and each of the tokens has its own position_ variable as well
and we check in the dictionary if there is any thing there 

if it is of the same color then  append 
or if the position is a safe house then append

else the old will reset and the new will be added 
 
 
'''
#############################################################################################    TOKEN CLASS END  #########################################################################################

import page1

import random


page1.initial()
namelist=page2.page2()

if namelist[0]!="NONE":
	r1 = token(red)
	r2 = token(red)
	r3 = token(red)
	r4 = token(red)
	playtokens.append(r1)
	playtokens.append(r2)
	playtokens.append(r3)
	playtokens.append(r4)
	players.append((red,namelist[0]))

if namelist[1]!="NONE":
	g1 = token(green)
	g2 = token(green)
	g3 = token(green)
	g4 = token(green)
	playtokens.append(g1)
	playtokens.append(g2)
	playtokens.append(g3)
	playtokens.append(g4)
	players.append((green,namelist[1]))

if namelist[2]!="NONE":
	b1 = token(blue)
	b2 = token(blue)
	b3 = token(blue)
	b4 = token(blue)
	playtokens.append(b1)
	playtokens.append(b2)
	playtokens.append(b3)
	playtokens.append(b4)
	players.append((blue,namelist[2]))

if namelist[3]!="NONE":
	y1 = token(yellow)
	y2 = token(yellow)
	y3 = token(yellow)
	y4 = token(yellow)
	playtokens.append(y1)
	playtokens.append(y2)
	playtokens.append(y3)
	playtokens.append(y4)
	players.append((yellow,namelist[3]))

def message(x,y,w,h,msg,font_color,font_size,rect_color):
	pygame.draw.rect(screen,rect_color,[x,y,w,h])
	font = pygame.font.Font('freesansbold.ttf',font_size)
	text = font.render(msg,True,font_color)
	screen.blit(text,[x+20,y+20])

		

def gameloop():
	game=True
	for i in players:
		set_default(i[0])
	while game:
		for j in range(len(players)):
			space = True
			board()		
			for i in playtokens:
				if i.position==home_base[0]:
					playtokens.remove(i)
				i.display_token()
			message(150,940,650,80,players[j][1]+"'s Turn",black,50,players[j][0])
			pygame.display.update()
			pygame.display.flip()
			while space:
				for evt in pygame.event.get():
					if evt.type==pygame.QUIT:
						pygame.quit()
						quit()

					if evt.type == pygame.KEYDOWN:
						if evt.key == pygame.K_SPACE:
							space = False 
			die = random.randint(1,6)
			flag = True
			message(940,425,100,100,str(die),black,80,players[j][0])
			pygame.display.update()
			pygame.display.flip()
			pygame.time.delay(1000)

			while flag:
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						pygame.quit()
						quit()

				if(die>=6):
					for i in playtokens:
						if(i.color==players[j][0] and flag):
							x=i.click_token(die)
							flag=flag and x
				else:
					for i in playtokens:
						if(i.color==players[j][0] and flag):
							if i.color==red:
								if len(inactive_red)==4 or len(active_red)==0:
									flag=False
							elif i.color==blue:
								if len(inactive_blue)==4 or len(active_blue)==0:
									flag=False
							elif i.color==green:
								if len(inactive_green)==4 or len(active_green)==0:
									flag=False
							elif i.color==yellow:
								if len(inactive_yellow)==4 or len(active_yellow)==0:
									flag=False


							if i in active_tokens:
								x=i.click_token(die)
								flag=flag and x

				if (len(inactive_red)==0 and len(active_red)==0 and players[j][0]==red):
					screen.fill(red)
					page2.message(players[j][1]+" WINS",black,80,100,400)
					game=False
					flag=False
					pygame.display.update()
					pygame.display.flip()
					pygame.time.delay(5000)
					sys.exit()

				if (len(inactive_blue)==0 and len(active_blue)==0 and players[j][0]==blue):
					screen.fill(blue)
					page2.message(players[j][1]+" WINS",black,80,100,400)
					game=False
					flag=False
					pygame.display.update()
					pygame.display.flip()
					pygame.time.delay(5000)
					sys.exit()

				if (len(inactive_green)==0 and len(active_green)==0 and players[j][0]==green):
					screen.fill(green)
					page2.message(players[j][1]+" WINS",black,80,100,400)
					game=False
					flag=False
					pygame.display.update()
					pygame.display.flip()
					pygame.time.delay(5000)
					sys.exit()

				if (len(inactive_yellow)==0 and len(active_yellow)==0 and players[j][0]==yellow):
					screen.fill(yellow)
					page2.message(players[j][1]+" WINS",black,80,100,400)
					game=False
					flag=False
					pygame.display.update()
					pygame.display.flip()
					pygame.time.delay(5000)
					sys.exit()

				pygame.display.update()
				pygame.display.flip()


if __name__=="__main__":

	gameloop()




