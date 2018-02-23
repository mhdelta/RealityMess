import pygame
import os
from random import randint

if __name__ == '__main__':

	alto = 600
	ancho = 480
	pygame.init()
	pantalla = pygame.display.set_mode([alto, ancho])
	pygame.display.flip()
	reloj  = pygame.time.Clock()
	
	#VARIABLES
	Rojo = [255, 0, 0]
	Negro = [0, 0, 0]
	Verde = [0, 255, 0]
	Azul = [0, 0, 255]
	punto = [0 ,0]
	lista = []
	limite = 300
	fin = False
	contador = 0
	clock = 20

	pygame.draw.line(pantalla, Rojo, [300, 100], [300, 400], 10 )
	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				punto = event.pos	

		pygame.draw.circle(pantalla, Verde, punto, 4)
		pygame.draw.line(pantalla, Azul, [300, 100], punto, 10 )
		pygame.draw.line(pantalla, Azul, [300, 400], punto, 10 )
		pygame.display.flip()
		reloj.tick(clock)		

