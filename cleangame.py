import pygame
from pygame.locals import *

from classs import *

#Listes des images du jeu
image_ball = "ball.png"
image_fond = "background.png"
titre_fenetre="PongGame"


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((900, 500))
#Icone
icone = pygame.image.load(image_ball)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer = 1

playeur1 = Playeur(1)
playeur2 = Playeur(2)
ball = Ball(450,250)

#Chargement et affichage de l'écran d'accueil
accueil = pygame.image.load(image_fond).convert()
accueil = pygame.transform.scale(accueil, (900,500))

font = pygame.font.SysFont("Comic Sans MS", 20)

while continuer:	

	#Rafraichissement
	pygame.display.flip()

	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(120)

	colliBall=ball.move(playeur1,playeur2)
	if colliBall == 1:
		ball = Ball(450,250)
		playeur2.score += 1
	if colliBall == 2:
		ball = Ball(450,250)
		playeur1.score += 1

	for event in pygame.event.get():
		#Si l'utilisateur quitte variable générale à 0 pour fermer la fenêtre
		if event.type == QUIT:
			continuer_jeu = 0
			continuer = 0
			
	keys = pygame.key.get_pressed()
	#Si l'utilisateur presse Echap ici, on revient seulement au menu
	if keys[pygame.K_ESCAPE]:
		continuer_jeu = 0
		continuer = 0

	if keys[pygame.K_n] or keys[pygame.K_b]or keys[pygame.K_v]:
		playeur1 = Playeur(1)
		playeur2 = Playeur(2)
		ball = Ball(450,250)
		if keys[pygame.K_b] or keys[pygame.K_v]:
			playeur1.bot = True
			if keys[pygame.K_v]:
				playeur2.bot = True
	#Touches de déplacement
	if playeur2.bot == True and ball.x > 700 and ball.x + ball.width < playeur2.x:
		if ball.y > playeur2.y+playeur2.height/2:
			playeur2.moveKeyboard(1)
		if ball.y < playeur2.y+playeur2.height/2:
			playeur2.moveKeyboard(-1)
	else:
		if keys[pygame.K_UP]:
			playeur2.moveKeyboard(-1)
		if keys[pygame.K_DOWN]:
			playeur2.moveKeyboard(1)

	if playeur1.bot == True and ball.x < 200 and ball.x > playeur1.x + playeur1.width:
		if ball.y > playeur1.y+playeur1.height/2:
			playeur1.moveKeyboard(1)
		if ball.y < playeur1.y+playeur1.height/2:
			playeur1.moveKeyboard(-1)
	else:
		if keys[pygame.K_w]:
			playeur1.moveKeyboard(-1)
		if keys[pygame.K_s]:
			playeur1.moveKeyboard(1)

	fenetre.blit(accueil, (0,0))
	if playeur1.bot == True:
		bot = font.render("bot", 1, (0,0,0))
		fenetre.blit(bot, (270,200))
	else:
		playeur1u = font.render("/\\ Z", 1, (0,0,0))
		fenetre.blit(playeur1u, (270,200))
		playeur1d = font.render("\\/ S", 1, (0,0,0))
		fenetre.blit(playeur1d, (270,260))
	score1 = font.render(str(playeur1.score), 1, (0,0,0))
	fenetre.blit(score1, (275,230))
        
	if playeur1.bot == True:
		bot = font.render("bot", 1, (0,0,0))
		fenetre.blit(bot, (575,200))
	else:
		playeur1u = font.render("/\\ up arrow", 1, (0,0,0))
		fenetre.blit(playeur1u, (575,200))
		playeur1d = font.render("\\/ down arrow", 1, (0,0,0))
		fenetre.blit(playeur1d, (575,260))
	score2 = font.render(str(playeur2.score), 1, (0,0,0))
	fenetre.blit(score2, (580, 230))

	info1 = font.render("Press N - New game", 1, (0,0,0))
	fenetre.blit(info1, (350, 380))
	info2 = font.render("Press ecape - Quit the game", 1, (0,0,0))
	fenetre.blit(info2, (350, 410))
	info3 = font.render("Press B - Bot vs Playeur", 1, (0,0,0))
	fenetre.blit(info3, (350, 440))
	info3 = font.render("Press V - Bot vs Bot", 1, (0,0,0))
	fenetre.blit(info3, (350, 470))

	fenetre.blit(playeur1.sprite, (playeur1.x, playeur1.y))
	fenetre.blit(playeur2.sprite, (playeur2.x, playeur2.y))
	fenetre.blit(ball.sprite, (ball.x, ball.y))
