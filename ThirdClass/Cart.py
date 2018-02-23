import pygame
import os
from random import randint

if __name__ == '__main__':

	pygame.init()
	pantalla = pygame.display.set_mode([600, 480])
	pygame.display.flip()
	reloj  = pygame.time.Clock()
	

	Rojo = [255, 0, 0]
	Negro = [0, 0, 0]

	v1 = [280, 10]
	v2 = [320, 10]

	lista = []

	#lista.append(v1)
	#lista.append(v2)
	limite = 300
	fin = False
	contador = 0

	clock = 20

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				p = list(event.pos)
				lista.append(p)
				pygame.draw.circle(pantalla, Rojo, p, 4)
				contador += 1

		
		if contador == 3:
			pantalla.fill(Negro)
			for v in lista:
				if v[1] < limite:
					v[1]+= 1
				pygame.draw.circle(pantalla, Rojo, v, 4)
			


		print contador
		pygame.display.flip()
		reloj.tick(clock)		

