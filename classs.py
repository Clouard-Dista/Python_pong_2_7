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
		self.score = 0
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

	def addScore(self):
		self.score = self.score + 1;

	def resetScore(self):
		self.score = 0

	def getScore(self):
		return self.score


class Ball:

	def __init__(self):
		self.y=10
		self.x = 10
		self.height = 90
		self.width = 45
		self.sprite = pygame.transform.scale(self.sprite, (self.width,self.height))

	def move(self):
		print(self.x,self.y)

	def colli(self,PlayeurA,PlayeurB):
		self.move(PlayeurA,PlayeurB);

	def resetBall(self):

	def modifScore(self,PlayeurA,PlayeurB):
		if self.x < -self.width:
			PlayeurA.addScore();
		elif self.x > 900:
			PlayeurB.addScore();

	