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
	
	#VARIABLES
	Rojo = [255, 0, 0]
	Negro = [0, 0, 0]
	Verde = [0, 255, 0]
	Azul = [0, 0, 255]
	punto = [100 ,100]
	lista = []
	fin = False
	contador = 0
	radio = 5
	listaPuntos = []
	listaPuntosPantalla = []	
	centro = (ancho/2, alto/2)
	lp = []
	angle = 0
	clock = 1
	a = 200
	n = 4
	b = 5
	
	pygame.draw.line(pantalla, [0,0,255], [0, 240], [960, 240]) #X
	pygame.draw.line(pantalla, [255,0,0], [300, 0], [300, 960]) #Y
	
	

	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				print "click"

		
		pygame.draw.circle(pantalla, Verde, p1, radio-3, 1)
		pygame.display.flip()
				
		reloj.tick(clock)		
