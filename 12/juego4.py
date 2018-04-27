import pygame
import random



#Variables y definiciones

Rojo = [255, 0, 0]
Negro = [0, 0, 0]
Verde = [0, 255, 0]
Azul = [0, 0, 255]
Negro = [0, 0, 0]
Gris = [191, 189, 191]
Blanco = [255, 255, 255]
fin = 0
clock = 10

# clases


class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([30,30])
		self.image.fill(Verde)
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 150

		self.vel_x = 0
		self.vel_y = 0

	def update(self):
		# self.rect.x += self.vel_x

		self.rect.x += self.vel_x
		self.rect.y += self.vel_y




if __name__ == '__main__':
	alto = 480
	ancho = 600
	pygame.init()
	pantalla = pygame.display.set_mode([1000, 1000])
	pygame.display.flip()
	reloj  = pygame.time.Clock()

	
	centro = (ancho/2, alto/2)
	imagen = pygame.image.load('animals.png')


	fondo = pygame.image.load('../images/mapas_tiled.png')

	info = imagen.get_rect()
	ancho_img = info[2]
	alto_img = info[3]

	ancho_corte = int(ancho_img/12)
	alto_corte = int(alto_img/8)

	x = 0
	y = 0	

	casillas_ancho = 1
	casillas_alto = 1

	derecha = []
	izquierda = []
	arriba = []
	abajo = []

	for x in range(3):
		cuadro = imagen.subsurface(x*ancho_corte, y*alto_corte, ancho_corte*casillas_ancho, alto_corte*casillas_alto)
		abajo.append(cuadro)

		cuadro = imagen.subsurface(x*ancho_corte, (y+1)*alto_corte, ancho_corte*casillas_ancho, alto_corte*casillas_alto)
		izquierda.append(cuadro)

		cuadro = imagen.subsurface(x*ancho_corte, (y+2)*alto_corte, ancho_corte*casillas_ancho, alto_corte*casillas_alto)
		derecha.append(cuadro)

		cuadro = imagen.subsurface(x*ancho_corte, (y+3)*alto_corte, ancho_corte*casillas_ancho, alto_corte*casillas_alto)
		arriba.append(cuadro)


	#Grupos

	jugadores = pygame.sprite.Group()
	muros = pygame.sprite.Group()
	enemigos = pygame.sprite.Group()
	todos = pygame.sprite.Group()


	# Objetos

	jugador = Jugador()
	jugadores.add(jugador)
	todos.add(jugador)


	indice_caminar = 0
	px = 0
	py = 0


	#CICLO PRINCIPAL
	while not fin:
		pantalla.blit(fondo, [0,0])

		#Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_RIGHT:
					pantalla.blit(derecha[indice_caminar], [px, py])
					indice_caminar += 1
					px += 10
				if event.key == pygame.K_DOWN:
					pantalla.blit(abajo[indice_caminar], [px, py])
					indice_caminar += 1
					py += 10
				if event.key == pygame.K_UP:
					pantalla.blit(arriba[indice_caminar], [px, py])
					indice_caminar += 1
					py += -10
				if event.key == pygame.K_LEFT:
					pantalla.blit(izquierda[indice_caminar], [px, py])
					indice_caminar += 1
					px += -10
					
			


		#Logica del juego

		if indice_caminar >= 3:
			indice_caminar = 0


		pygame.display.flip()	
		reloj.tick(clock)		
