import pygame
import os
import math


'''
	HOW THIS WILL WORK


		1 Seleccionar puntos fijos
		2 Trasladar la figura tal que el punto fijo coincida con el origen
		3 Escale la figura al 2,2
		4 Retorne la figura a la posicion original

'''

def DibujarPlanoCart():
	pygame.draw.line(pantalla, [0,0,255], [0, 240], [960, 240]) #X
	pygame.draw.line(pantalla, [255,0,0], [300, 0], [300, 960]) #Y
	pygame.display.flip()
	

def ToPantalla(centro, p):
	x = centro[0] + p[0]
	y = - p[1] + centro[1]
	return (int(x), int(y))

#From polar
def ToCart(r, angle):
	x = r * math.cos(angle)
	y = r * math.sin(angle)
	return (x, y)

#Trasladar al origen
def AlOrigen(lp):
	global pf
	pf = list(lp[0])
	lpt = []
	for i in lp:
		i = list(i)
		i[0] -= pf[0]  
		i[1] -= pf[1]  
		lpt.append(i)
	return lpt

def Escalar(lp, escala):
	lpe = []
	for i in lp:
		i = list(i)
		i[0] *= escala[0]
		i[1] *= escala[1]
		lpe.append(i)
	return lpe

def PosOriginal(lp):
	lpo = []
	for i in lp:
		i = list(i)
		i[0] += pf[0]
		i[1] += pf[1]
		lpo.append(i)
	return lpo

def MostrarLP(lp):
	for p in listaPuntos:
   		np = ToPantalla(centro, p)
   		listaPuntosPantalla.append(np)

	pygame.draw.polygon(pantalla, [255,255,255], listaPuntosPantalla, radio-2)
	pygame.display.flip()

def Rotar(lp, angle):
	lpr = []
	angle = math.radians(angle)
	for i in lp:
		i = list(i)
		i[0] = i[0] * math.cos(angle) - i[1] * math.sin(angle) 
		i[1] = i[0] * math.sin(angle) + i[1] * math.sin(angle)
		lpr.append(i)
	return (lpr)

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
	
	#Dibujar los puntos polares 
	# p1 = ToCart(100, 45)
	# print p1

	# pygame.draw.circle(pantalla, Verde, p5, radio, 1)

	# listaPuntosPantalla = []
	# for p in listaPuntos:
	# 	np = ToPantalla(centro, p)
	# 	listaPuntosPantalla.append(np)

	
	# PONGO LOS PUNTOS en una lista
	p1 = (40,20)
	p2 = (100,20)
	p3 = (100,60)

	listaPuntos.append(p1)
	listaPuntos.append(p2)
	listaPuntos.append(p3)


	# TRASLADAR LOS PUNTOS AL ORIGEN
	#listaPuntos = AlOrigen(listaPuntos)

	# Escalar * 2

	#listaPuntos = Escalar(listaPuntos, (2,2))

	# Regresar al punto original : sumar punto fijo

	#listaPuntos = PosOriginal(listaPuntos)
	
	
	#Ahora a rotar el triangulo

	listaPuntos = AlOrigen(listaPuntos)

	listaPuntos = Rotar(listaPuntos, 0)

	listaPuntos = PosOriginal(listaPuntos)

	MostrarLP(listaPuntos)
	
	


	

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
