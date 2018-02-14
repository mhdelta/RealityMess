import pygame
import os
from random import randint

if __name__ == '__main__':
	pygame.init()

	pantalla = pygame.display.set_mode([600, 480])
	
	pygame.display.flip()
	
	fin = False
	puntos = []
	con = 0
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print "Quitting ..."
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				print "Click"
				if(con <= 3):
					puntos.append((event.pos))
					con += 1
					if con == 3:
						pygame.draw.polygon(pantalla, [0, 0, 255], puntos, 1)	
						pygame.display.flip()
						con = 0
						puntos = []
