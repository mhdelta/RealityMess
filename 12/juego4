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
	imagen = pygame.image.load('hero.png')
	#pantalla.blit(imagen, [0, 0]) 

	info = imagen.get_rect()
	ancho_img = info[2]
	alto_img = info[3]

	ancho_corte = int(ancho_img/8)
	alto_corte = int(alto_img/5)

	x = 0
	y = 2

	casillas_ancho = 1
	casillas_alto = 1

	caminar = []

	for x in range(6):
		cuadro = imagen.subsurface(x*ancho_corte, y*alto_corte, ancho_corte*casillas_ancho, alto_corte*casillas_alto)
		caminar.append(cuadro)


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
	vel_x = 5

	#CICLO PRINCIPAL
	while not fin:

		#Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			


		#Logica del juego
		pantalla.fill(Negro)
		pantalla.blit(caminar[indice_caminar], [px, 0])
		indice_caminar += 1

		if indice_caminar >= 6:
			indice_caminar = 0
		px += vel_x 

		pygame.display.flip()	
		reloj.tick(clock)		
