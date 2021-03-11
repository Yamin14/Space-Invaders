import pygame
import random
pygame.init()

width, height = 600, 900
screen = pygame.display.set_mode((width, height))
running = True

#colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 200, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)
cyan = (0, 255, 255)

#spaceship characteristics
rect_width, rect_height = 150, 100
x = 300
y = height - rect_height - 10
radius = rect_height / 2
direction = 0
speed = 1.4
firing = False
flag = True
fire_speed = 4
fire_count = 0
fire_x, fire_y = [], []
fire_rect = []
score = 0

#enemies
invading = False
flag2 = True
en_speed = 1
en_count = 0
en_x, en_y = [], []
en_rect = []
en_w, en_h= 100, 50
en_blacklisted = []

#time
counter = 0
constant = 200

while running:
	screen.fill(black)
	font = pygame.font.Font('freesansbold.ttf', 30)
	text = font.render(f"Score: {score}", True, white, black)
	textRect = text.get_rect()
	textRect.center = (70, 20)
	screen.blit(text, textRect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				direction = 1
			elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
				direction = -1
			if event.key == pygame.K_w:
				firing = True
				flag = True
				fire_count += 1
		
		if event.type == pygame.MOUSEBUTTONUP:
			firing = True
			flag = True
			fire_count += 1
				
		if event.type == pygame.KEYUP:
			direction = 0
			
	#move
	if direction == 1:
		if x + rect_width < width:
			x += speed
	elif direction == -1:
		if x > 10:
			x -= speed

	#firing
	if firing == True:
		if flag == True:
			fire_x.append(x + (rect_width/2) - 5)
			fire_y.append(y-100)
			fire_rect.append("")
			flag = False
		
		for i in range(fire_count):
			if fire_y[i] >= 10:
				fire_rect[i] = pygame.draw.rect(screen, orange, (fire_x[i], fire_y[i], 10, 40))
				fire_y[i] -= fire_speed
				
			for j in range(en_count):
				if fire_x[i] >= en_x[j] and fire_x[i] <= en_x[j] + en_w and fire_y[i] <= en_y[j]+en_h and fire_y[i] >= en_y[j] and j not in en_blacklisted:
					en_blacklisted.append(j)
					score += 1
				
	#enemies
	if counter % constant == 0:
		invading = True
		flag2 = True
		en_count += 1
	
	if invading == True:
		if flag2 == True:
			en_x.append(random.randint(50, 650))
			en_y.append(-100)
			en_rect.append("")
			flag2 = False

		for i in range(en_count):
			if en_y[i]+en_h <= y and i not in en_blacklisted:
				en_rect[i] = pygame.draw.rect(screen, black, (en_x[i], en_y[i], en_w, en_h))
				pygame.draw.polygon(screen, magenta, [(en_x[i], en_y[i]), (en_x[i]+en_w, en_y[i]), (en_x[i]+(en_w/2), en_y[i]+en_h)])
				en_y[i] += en_speed
				
			elif en_y[i]+en_h > y:
				while running:
					screen.fill(black)
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
					font = pygame.font.Font('freesansbold.ttf', 70)
					text = font.render("Game Over", True, red, black)
					textRect = text.get_rect()
					textRect.center = (350, 400)
					screen.blit(text, textRect)
					font = pygame.font.Font('freesansbold.ttf', 70)
					text = font.render(f"Score: {score}", True, red, black)
					textRect = text.get_rect()
					textRect.center = (350, 470)
					screen.blit(text, textRect)
					pygame.display.flip()
				
				
	#spaceship
	pygame.draw.rect(screen, green, (x, y, rect_width, rect_height))
	pygame.draw.circle(screen, green, (x, y + (rect_height/2)), radius)
	pygame.draw.circle(screen, green, (x+rect_width, y + (rect_height/2)), radius)
	pygame.draw.rect(screen, grey, (x+(rect_width/2)-10, y-20, 20, 60))
	pygame.draw.polygon(screen, blue, [(x, y+rect_height), (x+25, y+rect_height/2), (x+50, y+rect_height)])
	pygame.draw.polygon(screen, blue, [(x+rect_width, y+rect_height), (x+rect_width-25, y+rect_height/2), (x+rect_width-50, y+rect_height)])
	
	counter += 1
	pygame.display.flip()

pygame.quit()
