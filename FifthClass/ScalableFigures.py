import pygame
import os
from random import randint

def ToPantalla(centro, p):
	x = centro[0] + p[0]
	y = - p[1] + centro[1]
	return (x, y)

def Escala(p, escala):
	xp = p[0] * escala[0]
	yp = p[1] * escala[1]
	return (xp, yp)

def EscalarUp(listaPuntos, escala):
	listaPuntosEscala = []
	for p in listaPuntos:
		np = Escala(p, escala)
		listaPuntosEscala.append(np)
	listaPuntos = [] 
	for p in listaPuntosEscala:
		pantalla.fill([0,0,0])
		pygame.draw.polygon(pantalla, Rojo, listaPuntosEscala, radio)
		pygame.display.flip()
		listaPuntos.append(p)
	listaPuntosEscala = []
	return listaPuntos


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
	radio = 5
	listaPuntos = []
	centro = (ancho/2, alto/2)
	
	# pygame.draw.line(pantalla, [0,0,255], [0, 240], [960, 240]) #X
	# pygame.draw.line(pantalla, [255,0,0], [300, 0], [300, 960]) #Y
	
	# listaPuntosPantalla = []
	# for p in listaPuntos:
	# 	np = ToPantalla(centro, p)
	# 	listaPuntosPantalla.append(np)
	
	# pygame.draw.polygon(pantalla, [255,255,255], listaPuntosPantalla, radio)


	# #ESCALAMIENTO

	listaPuntosEscala = []
	# for p in listaPuntos:
	# 	np = Escala(p, (1.5,1.5))
	# 	listaPuntosEscala.append(np)


	listaPuntosPantalla = []

	# for p in listaPuntosEscala:
	# 	np = ToPantalla(centro, p)
	# 	listaPuntosPantalla.append(np)

	# pygame.draw.polygon(pantalla, Rojo, listaPuntosPantalla, radio)

	# pygame.display.flip()





	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				contador += 1
				listaPuntos.append(event.pos)
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_UP:
					listaPuntos = EscalarUp(listaPuntos, (0.5, 0.5))
				if event.key == pygame.K_DOWN	:
					listaPuntos = EscalarUp(listaPuntos, (-0.5, -0.5))
			if contador == 3:
				pygame.draw.polygon(pantalla, [255, 255, 255], listaPuntos, radio)
				pygame.display.flip()
				contador = 0
		reloj.tick(clock)		
