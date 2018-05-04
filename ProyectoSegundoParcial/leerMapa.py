import pygame
import random
import ConfigParser


#Variables y definiciones

Rojo = [255, 0, 0]
Negro = [0, 0, 0]
Verde = [0, 255, 0]
Azul = [0, 0, 255]
Negro = [0, 0, 0]
Gris = [191, 189, 191]
Blanco = [255, 255, 255]
fin = 0
clock = 20

def RecortarMatriz (sprites, nombre_img, limites):
	imagen = pygame.image.load(nombre_img)
	info = imagen.get_rect()
	ancho_img = info[2]
	alto_img = info[3]

	ancho_corte = int(ancho_img/sprites[0])
	alto_corte = int(alto_img/sprites[1])
	x = 0
	y = 0	

	casillas_ancho = 1
	casillas_alto = 1
	m = []
	for i in range(len(limites)):
		fila = []
		for x in range(limites[i]):
			cuadro = imagen.subsurface(x*ancho_corte, y*alto_corte, ancho_corte*casillas_ancho, alto_corte*casillas_alto)
			fila.append(cuadro)
		m.append(fila)
		y += 1
	return m



if __name__ == '__main__':
	alto = 480
	ancho = 600
	pygame.init()
	pantalla = pygame.display.set_mode([1000, 1000])
	pygame.display.flip()
	reloj  = pygame.time.Clock()

	
	centro = (ancho/2, alto/2)
	
	limites = []
	
	interprete = ConfigParser.ConfigParser()
	interprete.read('mapa1.map')
	archivo = interprete.get('nivel', 'origen')
	alto = int(interprete.get('nivel', 'alto'))
	ancho = int(interprete.get('nivel', 'ancho'))

	for i in range(11):
		limites.append(32)


	infomapa = interprete.get('nivel', 'mapa')
	lt = infomapa.split('\n')
	print lt
	m = RecortarMatriz([32,12], 'terrenogen.png', limites)
	for fila in range(len(lt)):
		for col in range(len(lt[0])):
			x = interprete.get(lt[fila][col], 'x')
			y = interprete.get(lt[fila][col], 'y')
			pantalla.blit(m[int(y)][int(x)], [32*col,32*fila])
	pygame.display.flip()


	#Grupos


	# Objetos

	px = 0
	py = 0
	i=0
	ls_col = []

	#CICLO PRINCIPAL
	while not fin:

		#Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		#Logica del juegO




		#REFRESCO DE PANTALLA


		pygame.display.flip()	
		reloj.tick(clock)		
