import pygame
import random
from pygame.locals import *

class Playeur:

	def __init__(self,typeP):
		if typeP == 1:
			self.y=10
			self.x = 10
			self.sprite = pygame.image.load("yellowPlayeur.png").convert_alpha()
		elif typeP == 2:
			self.y=10
			self.x=845
			self.sprite = pygame.image.load("bluePlayeur.png").convert_alpha()
		self.height = 90
		self.width = 45
		self.bot = False
		self.score=0
		self.sprite = pygame.transform.scale(self.sprite, (self.width,self.height))
	
	def move(self, direction):
		if self.y < direction and self.y + 10 <= 500-self.height:
			self.y = self.y + 10
		elif self.y > direction and self.y - 10 >= 0:
			self.y = self.y - 10
	
	def moveKeyboard(self, key):
		if self.y + key*10 <= 500-self.height and self.y + key*10 >= 0:
			self.y = self.y + key*10

class Ball:

	def __init__(self,x,y):
		global pos, vel
		self.height = 30
		self.width = 30
		self.x = x - self.width/2
		self.y = y - self.height/2
		self.vel_x = random.randrange(-3,3)
		if self.vel_x == 0:
			self.vel_x = 1;
		self.vel_y = -random.randrange(-2,2)
		if self.vel_y == 0:
			self.vel_y = 1;
		self.sprite = pygame.image.load("ball.png").convert_alpha()
		self.sprite = pygame.transform.scale(self.sprite, (self.width,self.height))

	def move(self,playeur1,playeur2):
		if self.y <= 0:
			self.vel_y = - self.vel_y
		if self.y >= 500 - self.height:
			self.vel_y = -self.vel_y

		if playeur1.x < self.x + self.width and playeur1.x + playeur1.width > self.x and playeur1.y < self.y + self.height and playeur1.height + playeur1.y > self.y or playeur2.x < self.x + self.width and playeur2.x + playeur2.width > self.x and playeur2.y < self.y + self.height and playeur2.height + playeur2.y > self.y:
			self.vel_x = -self.vel_x
			self.vel_x *= 1.1
			self.vel_y *= 1.1
		
		if self.x < -self.width:
			return 1
		if self.x > 900:
			return 2

		if self.vel_x > 5:
			self.vel_x = 5;
		if self.vel_x < -5:
			self.vel_x = -5

		if self.vel_y > 5:
			self.vel_y = 5;
		if self.vel_y < -5:
			self.vel_y = -5

		self.x += self.vel_x
		self.y += self.vel_y

		return False