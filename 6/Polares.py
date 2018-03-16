import pygame
import os
import math


def ToPantalla(centro, p):
	x = centro[0] + p[0]
	y = - p[1] + centro[1]
	return (int(x), int(y))

def ToCart(r, angle):
	x = r * math.cos(angle)
	y = r * math.sin(angle)
	return (x, y)

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
	centro = (ancho/2, alto/2)
	lp = []
	angle = 0
	clock = 1
	a = 200
	n = 4
	b = 5
	
	pygame.draw.line(pantalla, [0,0,255], [0, 240], [960, 240]) #X
	pygame.draw.line(pantalla, [255,0,0], [300, 0], [300, 960]) #Y
	
	#Dibujar los puntos polares 
	# p1 = ToCart(100, 45)
	# print p1
	# p1 = ToPantalla(centro, p1)
	# print p1
	# p2 = ToCart(100, 120)
	# p2 = ToPantalla(centro, p2)

	# p3 = ToCart(100, 210)
	# p3 = ToPantalla(centro, p3)

	# p4 = ToCart(100, 300)
	# p4 = ToPantalla(centro, p4)

	# p5 = ToCart(100, 0)
	# p5 = ToPantalla(centro, p5)

	
	# pygame.draw.circle(pantalla, Verde, p1, radio, 1)
	# pygame.draw.circle(pantalla, Verde, p2, radio, 1)
	# pygame.draw.circle(pantalla, Verde, p3, radio, 1)
	# pygame.draw.circle(pantalla, Verde, p4, radio, 1)
	# pygame.draw.circle(pantalla, Verde, p5, radio, 1)

	
	# listaPuntosPantalla = []
	# for p in listaPuntos:
	# 	np = ToPantalla(centro, p)
	# 	listaPuntosPantalla.append(np)
	

	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				print "click"
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_UP:
					print "key up"
		r = a * math.cos(n*angle)+b	
		p = ToCart(r, angle)
		p = ToPantalla(centro, p)
		angle += 1
		pygame.draw.circle(pantalla, Verde, p, radio-3, 1)
		pygame.display.flip()
				
		reloj.tick(clock)		
