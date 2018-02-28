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
	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_UP:
					vel_y = -1
				if event.key == pygame.K_DOWN:
					vel_y = 1
				if event.key == pygame.K_LEFT:
					vel_x = -1
				if event.key == pygame.K_RIGHT:
					vel_x = 1
		
		if punto[1] > alto:
			punto[1] = punto[1] - radio
			vel_y = 0
			print punto[1]
		if punto[1] < 10:
			punto[1] = punto[1] + radio
			vel_y = 0
			print punto[1]
		if punto[0] > ancho:
			punto[0] = punto[0] - radio
			vel_x = 0
			print punto[0]
		if punto[0] < 10:
			punto[0] = punto[0] + radio
			vel_x = 0
			print punto[0]
		else:
			punto[0]+=vel_x						
			punto[1]+=vel_y;
		
		pantalla.fill(Negro)			
		pygame.draw.circle(pantalla, Verde, punto, radio)
		pygame.display.flip()
		reloj.tick(clock)		

