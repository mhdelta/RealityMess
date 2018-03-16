import pygame
import os
import math


if __name__ == '__main__':
	alto = 480
	ancho = 600
	pygame.init()
	pantalla = pygame.display.set_mode([ancho, alto])
	pygame.display.flip()
	reloj  = pygame.time.Clock()
	vader = pygame.image.load(os.path.join('../images', 'vader.png'))
	fondo = pygame.image.load(os.path.join('../images', 'back.jpg'))


	
	#VARIABLES
	Rojo = [255, 0, 0]
	Negro = [0, 0, 0]
	Verde = [0, 255, 0]
	Azul = [0, 0, 255]
	Negro = [0, 0, 0]
	Gris = [191, 189, 191]
	Blanco = [255, 255, 255]
	punto = [100 ,100]
	lista = []
	fin = False
	contador = 0
	radio = 5
	listaPuntos = []
	centro = (ancho/2, alto/2)
	
	clock = 300
	posx = 2	
	correr = False
	posy = 0

	der = True
	posvader = [190, 300]

	pantalla.blit(fondo, [posvader[0],-1400 - posvader[1]])
	pygame.display.flip()
	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				print "click"

			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_UP:
					vel_y = -1
				if event.key == pygame.K_DOWN:
					vel_y = 1
				if event.key == pygame.K_LEFT:
					posvader[0] += -10
				if event.key == pygame.K_RIGHT:
					posvader[0] += 10	




		pantalla.blit(vader, posvader)
		pygame.display.flip()

		if posvader[0] > 400:
			pantalla.blit(fondo, [posx,-1400 - posy])
			pygame.display.flip()
			posx += -3
			print pygame.mouse.get_pos()
		elif posvader[0] < 100:
			pantalla.blit(fondo, [posx,-1400 -posy])
			pygame.display.flip()
			posx += 3
		elif posvader[1] < 100:
			pantalla.blit(fondo, [posx,-1400 - posy])
			pygame.display.flip()
			posy += -3 
		elif posvader[1] > 380:
			pantalla.blit(fondo, [posx,-1400 - posy])
			pygame.display.flip()
			posy += 3 

		pygame.display.flip()
		reloj.tick(clock)		
