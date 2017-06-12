
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

#Chargement et affichage de l'écran d'accueil
accueil = pygame.image.load(image_fond).convert()
accueil = pygame.transform.scale(accueil, (900,500))
while continuer:	

	#Rafraichissement
	pygame.display.flip()

	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(120)

	for event in pygame.event.get():
		#Si l'utilisateur quitte variable générale à 0 pour fermer la fenêtre
		if event.type == QUIT:
			continuer_jeu = 0
			continuer = 0
		elif event.type == KEYDOWN:
			#Si l'utilisateur presse Echap ici, on revient seulement au menu
			if event.key == K_ESCAPE:
				continuer_jeu = 0
				continuer = 0
			#Touches de déplacement
			elif event.key == K_UP:
				playeur1.moveKeyboard(1)
			elif event.key == K_DOWN:
				playeur1.moveKeyboard(-1)


	fenetre.blit(accueil, (0,0))
	fenetre.blit(playeur1.sprite, (playeur1.x, playeur1.y))
	fenetre.blit(playeur2.sprite, (playeur2.x, playeur2.y))
