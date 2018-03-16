import pygame
import os
from random import randint

if __name__ == '__main__':

	alto = 480
	ancho = 600
	pygame.init()
	pantalla = pygame.display.set_mode([ancho, alto])
	pygame.display.flip()
	reloj  = pygame.time.Clock()
	
	#VARIABLES
	Rojo = [255, 0, 0]
	Negro = [0, 0, 0]
	Verde = [0, 255, 0]
	Azul = [0, 0, 255]
	punto = [100 ,100]
	lista = []
	limite = 300
	fin = False
	contador = 0
	clock = 300
	vel_y = 0
	vel_x = 0
	radio = 10
	listaPuntos = []
	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if contador == 3:
					contador = 0
					del listaPuntos[:]
				contador+=1
				listaPuntos.append(list(event.pos))

		pantalla.fill(Negro)

		if(contador == 3):
			for p in listaPuntos:
				pygame.draw.polygon(pantalla, Rojo, listaPuntos, radio)
				p[0] += 1			
		pygame.display.flip()
		reloj.tick(clock)		

