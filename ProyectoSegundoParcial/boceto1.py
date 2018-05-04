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

# clases

class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.image.load('soldier160x205.png')
		self.image = pygame.transform.scale(self.image, (50,50))
		self.rect = self.image.get_rect()
		self.i = 0
		self.rect.x = 100
		self.rect.y = 200
		self.dir = 0
		self.tmp = self.image
		self.vel_x = 0
		self.vel_y = 0

	def update(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y

		if self.dir == 1:
			self.image = pygame.transform.rotate(self.tmp, -90)
		if self.dir == 2:
			self.image = pygame.transform.rotate(self.tmp, 90)
		if self.dir == 3:
			self.image = pygame.transform.rotate(self.tmp, -180)
		if self.dir == 4:
			self.image = pygame.transform.rotate(self.tmp, 0)
		if self.dir == 5:
			self.image = pygame.transform.rotate(self.tmp, -45)
		if self.dir == 6:
			self.image = pygame.transform.rotate(self.tmp, 45)
		if self.dir == 7:
			self.image = pygame.transform.rotate(self.tmp, -135)
		if self.dir == 8:
			self.image = pygame.transform.rotate(self.tmp, 135)
		#control de accion

		# if self.accion == 2:
		# 	self.i += 1
		# 	if self.i >= len(self.m[self.accion]):
		# 		self.i = 0
		# 		self.accion = 1
		# else:
		# 	self.i += 1
		# 	if self.i >= len(self.m[self.accion]):
		# 		self.i = 0
		# self.image = self.m[self.accion][self.i]

class Barril(pygame.sprite.Sprite,):
	def __init__(self, anchoM, altoM, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([anchoM, altoM])
		self.image.fill(Blanco)
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

if __name__ == '__main__':
	alto = 480
	ancho = 600
	pygame.init()
	pantalla = pygame.display.set_mode([700, 500])
	reloj  = pygame.time.Clock()
	fondo = pygame.image.load('background.png')

	
	centro = (ancho/2, alto/2)
	limites = [1,1]
	# m = RecortarMatriz([20, 20], 'soldier160x205.png', limites)

	pygame.display.flip()

	accion = 0

	

	#Grupos

	jugadores = pygame.sprite.Group()
	barriles = pygame.sprite.Group()
	todos = pygame.sprite.Group()


	# Objetos

	barril = Barril(30, 80, [200,200])
	barriles.add(barril)
	todos.add(barril)
	jugador = Jugador()
	jugadores.add(jugador)
	todos.add(jugador)

	px = 0
	py = 0
	i=0
	ls_col = []

	#Direcciones
	Dir = [0,0,0,0]
	right = False
	up = False

	#CICLO PRINCIPAL
	while not fin:
		if Dir == [1,0,0,0]:
			jugador.dir = 1
		if Dir == [0,1,0,0]:
			jugador.dir = 2
		if Dir == [0,0,1,0]:
			jugador.dir = 3
		if Dir == [0,0,0,1]:
			jugador.dir = 4
		if Dir == [1,0,0,1]:
			jugador.dir = 5
		if Dir == [0,1,0,1]:
			jugador.dir = 6
		if Dir == [1,0,1,0]:
			jugador.dir = 7
		if Dir == [0,1,1,0]:
			jugador.dir = 8									
		#Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_RIGHT:
					jugador.vel_x = 10
					Dir[0] = 1
				if event.key == pygame.K_LEFT:
					jugador.vel_x = -10
					Dir[1] = 1
				if event.key == pygame.K_DOWN:
					jugador.vel_y = 10
					Dir[2] = 1
				if event.key == pygame.K_UP:
					jugador.vel_y = -10
					Dir[3] = 1
				if event.key == pygame.K_q:
					fin = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					Dir[3] = 0
				if event.key == pygame.K_DOWN:
					Dir[2] = 0
				if event.key == pygame.K_RIGHT:
					Dir[0] = 0
				if event.key == pygame.K_LEFT:
					Dir[1] = 0
				jugador.vel_x = 0
				jugador.vel_y = 0


		#Logica del juegO

		if jugador.accion == 2:
			ls_col = pygame.sprite.spritecollide(jugador, barriles, False)
			for b in ls_col:
				b.rect.x += 10

		#REFRESCO DE PANTALLA
		

		todos.update()
		pantalla.blit(fondo, (0,0))
		todos.draw(pantalla)

		pygame.display.flip()	
		reloj.tick(clock)		
