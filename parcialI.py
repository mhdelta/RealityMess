import pygame
import os
import math


def ToPantalla(centro, p):
	x = centro[0] + p[0]
	y = - p[1] + centro[1]
	return (int(x), int(y))

#From polar
def PolarToCart(r, angle):
	x = r * math.cos(angle)
	y = r * math.sin(angle)
	return (x, y)

def PantallaToCart(centro, punto):
	x = punto[0] - centro[0]  
	y = -punto[1] + centro[1]
	return (int(x), int(y))	

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
	print lpt
	return lpt


def PosOriginal(lp):
	lpo = []
	for i in lp:
		i = list(i)
		i[0] += pf[0]
		i[1] += pf[1]
		lpo.append(i)
	return lpo
def Rotar(lp, angle):
	lpr = []
	angle = math.radians(angle)
	for i in lp:
		i = list(i)
		i[0] = i[0] * math.cos(angle) - i[1] * math.sin(angle) 
		i[1] = i[0] * math.sin(angle) + i[1] * math.cos(angle)
		lpr.append(i)
	return (lpr)

def dibujarPlanoCartesiano(pantalla, centro):
	pygame.draw.line(pantalla, [0,0,255], [0, centro[1]], [960, centro[1]]) #X
	pygame.draw.line(pantalla, [255,0,0], [centro[0], 0], [centro[0], 960]) #Y
	pygame.display.flip()

def MostrarLP(lp, pantalla, centro):
   	listaPuntosPantalla = []
	for p in lp:
   		np = ToPantalla(centro, p)
   		listaPuntosPantalla.append(np)
   	pantalla.fill([0,0,0])
   	dibujarPlanoCartesiano(pantalla, centro)	
	pygame.draw.polygon(pantalla, [255,0,0], listaPuntosPantalla, radio-2)
	pygame.display.flip()



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
	Negro = [0, 0, 0]
	Gris = [191, 189, 191]
	Blanco = [255, 255, 255]
	punto = [100 ,100]
	lista = []
	listaPuntosPantalla = []
	listapuntosCart = []
	fin = False
	contador = 0
	radio = 5
	listaPuntos = []
	centro = (ancho/2, alto/2)
	
	clock = 300
	posx = 2	
	correr = False
	posy = 0

	der = True
	posvader = [190, 300]


	#Ahora a rotar el triangulo



	#CICLO PRINCIPAL
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				contador += 1
				if(contador == 1):
					dibujarPlanoCartesiano(pantalla, event.pos)
					centro = event.pos
				if(contador > 1 and contador < 5):
					listaPuntos.append(event.pos)
					listapuntosCart.append(PantallaToCart(centro, event.pos))
					print listapuntosCart
				if(contador == 4):
					triangulo = pygame.draw.polygon(pantalla, Rojo, listaPuntos, radio)
									
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_UP:
					print "a rotar"
					listapuntosCart = AlOrigen(listapuntosCart)
					listapuntosCart = Rotar(listapuntosCart, 30)
					listapuntosCart = PosOriginal(listapuntosCart)
					MostrarLP(listapuntosCart, pantalla, centro)
					#MostrarLP(listapuntosCart, pantalla, centro)	
			#if event.type == pygame.KEYDOWN:	
			#	if event.key == pygame.K_UP:


		pygame.display.flip()
		reloj.tick(clock)		
