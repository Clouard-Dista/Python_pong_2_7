import pygame
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
		self.sprite = pygame.transform.scale(self.sprite, (self.width,self.height))
	
	def move(self, direction):
		if self.y < direction and self.y + 10 <= 500-self.height:
			self.y = self.y + 10
		elif self.y > direction and self.y - 10 >= 0:
			self.y = self.y - 10
	
	def moveKeyboard(self, key):
		if self.y + key*10 <= 500-self.height and self.y + key*10 >= 0:
			self.y = self.y + key*10
		print(self.x,self.y)
