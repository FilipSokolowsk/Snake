import pygame
import time
from random import randrange

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Snake")
icon = pygame.image.load("C:/Users/Lenovo/Desktop/Python Projects/test/Snake/Head.jpg")
pygame.display.set_icon(icon)
HeadImg = pygame.image.load("C:/Users/Lenovo/Desktop/Python Projects/test/Snake/Head.jpg")
AppleImg = pygame.image.load("C:/Users/Lenovo/Desktop/Python Projects/test/Snake/Apple.png")
BodyImg = pygame.image.load("C:/Users/Lenovo/Desktop/Python Projects/test/Snake/Body.jpg")
GAME_OVER = pygame.image.load("C:/Users/Lenovo/Desktop/Python Projects/test/Snake/game_over.jpg")
pygame.mixer.music.load("C:/Users/Lenovo/Desktop/Python Projects/test/Snake/Mario_Bros.mp3")
czcionka = pygame.font.SysFont("dejavusans", 30)
czcionka1 = pygame.font.SysFont("dejavusans", 200)
pygame.mixer.music.play (loops = 100, start = 0.0, fade_ms = 0)


class Screen:
	def __init__ (self):
		cube = 20				
		row = 30
		self.screen = pygame.display.set_mode((620, 660))
		self.screen.fill((3, 144, 252))
		x = 0
		y = 0
		size_between = cube
		for l in range(row):
			x += size_between
			y += size_between
			pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, 620))
			pygame.draw.line(self.screen, (0, 0, 0), (0, y), (620, y))
		pygame.draw.rect(self.screen, (162, 255, 233), ((0, 620), (620, 40)))
		pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, 620), width = 3)

class Snake:
	def __init__(self, screen):
		self.screen = screen.screen
		self.headX = 300
		self.headY = 300
		self.possitions = []
		self.location = (self.headX, self.headY)
		self.direction = (0, -20)
	def head(self, screen):
		self.screen.blit(HeadImg, self.location)
	def tail(self, screen):
		#print(self.possitions)
		for tuples in self.possitions[0:]:
			self.screen.blit(BodyImg, tuples)
	def clear(self, screen):
		cube = 20				
		row = 30
		self.screen.fill((3, 144, 252))
		x = 0
		y = 0
		size_between = cube
		for l in range(row):
			x += size_between
			y += size_between
			pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, 620))
			pygame.draw.line(self.screen, (0, 0, 0), (0, y), (620, y))
		pygame.draw.rect(self.screen, (162, 255, 233), ((0, 620), (620, 40)))
		pygame.draw.line(self.screen, (0, 0, 0), (0, 621), (620, 621), width = 4)
	def move(self, screen, apple):
		self.location = (self.headX, self.headY)
		self.possitions.append(self.location)
		
		if self.location == apple.apple_location:
			pass
		else:
			self.possitions.remove(self.possitions[0])

	def edge(self, screen):
		if self.headX < 0:
			self.headX = 600
		elif self.headX > 600:
			self.headX = 0
		if self.headY < 0:
			self.headY = 600
		elif self.headY > 600:
			self.headY = 0
class Apple:
	def __init__(self, screen):

		self.screen = screen.screen
		self.AppleX = (randrange(30)) * 20
		self.AppleY = (randrange(30)) * 20
		self.apple_location = (self.AppleX, self.AppleY)
		screen.screen.blit(AppleImg, self.apple_location)
	def spawn_apple(self, screen):
		self.screen.blit(AppleImg, self.apple_location)
	def draw(self, screen, snake, apple):
		self.AppleX = (randrange(30)) * 20
		self.AppleY = (randrange(30)) * 20
		self.apple_location = (self.AppleX, self.AppleY)
		if self.apple_location in snake.possitions:
			apple.draw(screen, snake, apple)

class Score:
	def __init__(self, screen):
		self.wynik = 0
		self.screen = screen.screen
		self.czcionka = pygame.font.SysFont("dejavusans", 20)

	def show(self, screen):
		self.render = self.czcionka.render("Your score: " + str(self.wynik), 1, (0, 0, 0))
		self.screen.blit(self.render, (10,627))


screen = Screen()
snake = Snake(screen) 
apple = Apple(screen)
score = Score(screen)
running = True
speedX = 0
speedY = -20

while running:

	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and snake.direction != (20, 0):
				speedX = -20
				speedY = 0
				snake.direction = (-20, 0)
			if event.key == pygame.K_RIGHT and snake.direction != (-20, 0):
				speedX = 20
				speedY = 0
				snake.direction = (20, 0)
			if event.key == pygame.K_DOWN and snake.direction != (0, -20):
				speedX = 0
				speedY = 20
				snake.direction = (0, 20)
			if event.key == pygame.K_UP and snake.direction != (0, 20):
				speedX = 0
				speedY = -20
				snake.direction = (0, -20)


	if snake.location == apple.apple_location:
		score.wynik += 1
		apple.draw(screen, snake, apple)
	if snake.location in snake.possitions[:-1]:
		running = False
	
	score.show(screen)
	snake.edge(screen)
	snake.tail(screen)
	snake.move(screen, apple)
	snake.head(screen)
	apple.spawn_apple(screen)
	snake.headX += speedX
	snake.headY += speedY
	pygame.display.update()
	snake.clear(screen)
pygame.mixer.music.stop()
pygame.mixer.music.load("C:/Users/Lenovo/Desktop/Python Projects/test/Snake/Dead.mp3")
pygame.mixer.music.play (start = 01.12, fade_ms = 0)


ending_screen = pygame.display.set_mode((600, 450))
ending_screen.fill((0, 252, 0))
# ending_screen.blit(GAME_OVER, (0, 0))

text_render = czcionka.render("Your score: " + str(score.wynik), 1, (0, 0, 0))
gameover = czcionka1.render("GAME", 1, (0, 0, 0))
gameover1 = czcionka1.render("OVER", 1, (0, 0, 0))
ending_screen.blit(text_render, (10,10))
ending_screen.blit(gameover, (0,20))
ending_screen.blit(gameover1, (20,220))

run = True
while run:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
