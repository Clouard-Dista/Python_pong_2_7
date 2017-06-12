import pygame
from pygame.locals import *

class Playeur:

	def __init__(self,typeP):
		if typeP == 1:
			self.x=10
			self.y = 10
			self.sprite = pygame.image.load("bluePlayeur.png").convert_alpha()
		elif typeP == 2:
			self.x=10
			self.y=860
			self.sprite = pygame.image.load("yellowPlayeur.png").convert_alpha()
		self.sprite = pygame.transform.scale(self.sprite, (30,60))
	
	def move(self, direction):
		if self.x < direction:
			self.x = self.x + 1
		elif self.x > direction:
			self.x = self.x - 1
	
	def moveKeyboard(self, key):
		self.x = self.x + key
		print(self.x,self.y)
