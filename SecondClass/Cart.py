import pygame
import os
from random import randint

if __name__ == '__main__':
	pygame.init()

	pantalla = pygame.display.set_mode([600, 480])
	
	pygame.display.flip()
	
	fin = False

	con = 0
	x = 20
	y = 20
	reloj  = pygame.time.Clock()
	punto = [x,100]
	limitx = 1000
	bajando = True

	listaPuntos = []

	pygame.draw.line(pantalla, [0,0,255], [0, 240], [960, 240]) #X
	pygame.draw.line(pantalla, [255,0,0], [300, 0], [300, 960]) #Y
	pygame.display.flip()	

	#LOOP INFINITO
	while not fin:
		if y < 480 and bajando:
			y+=1

		punto[1] = y
		reloj.tick(250)
		randomColor = [randint(0, 255), randint(0, 255), randint(0, 255)]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print "Quitting ..."
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				listaPuntos.append(event.pos)
				print listaPuntos
				
		for p in listaPuntos:
			print p
			 	

		pantalla.fill([0,0,0])
		pygame.draw.circle(pantalla, [250, 0, 0], punto, 20, 0)
		pygame.display.flip()	