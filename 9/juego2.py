import pygame
import random



class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([30,30])
		self.image.fill(Verde)
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 150

		#self.vel_x = 0
		self.vel_y = 0

	def update(self):
		# self.rect.x += self.vel_x
		self.rect.y += self.vel_y


class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([30,30])
		self.image.fill(Rojo)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.vel_x = - random.randrange(5,10)
		#self.vel_y = 0

		self.espera = random.randrange(50)

	def update(self):
		#self.rect.y += self.vel_y

		if self.espera > 0:
			self.espera -= 1
		else:
			self.rect.x += self.vel_x
				
class Bala(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([15,15])
		self.image.fill(Azul)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.vel_x = 10
		#self.vel_y = 0
	def update(self):
		self.rect.x += self.vel_x


if __name__ == '__main__':
	alto = 480
	ancho = 600
	pygame.init()
	pantalla = pygame.display.set_mode([ancho, alto])
	pygame.display.flip()
	reloj  = pygame.time.Clock()

	
	#Variables y definiciones

	Rojo = [255, 0, 0]
	Negro = [0, 0, 0]
	Verde = [0, 255, 0]
	Azul = [0, 0, 255]
	Negro = [0, 0, 0]
	Gris = [191, 189, 191]
	Blanco = [255, 255, 255]
	fin = 0
	centro = (ancho/2, alto/2)
	clock = 50
	posx = 2	
	correr = False
	posy = 0
	der = True
	posvader = [190, 300]

	#Objeto
	todos = pygame.sprite.Group()
	jugadores = pygame.sprite.Group()
	enemigos = pygame.sprite.Group()
	balas = pygame.sprite.Group()

	jugador = Jugador()
	jugadores.add(jugador)
	todos.add(jugador)



	num_enemigos = 30

	for i in range(num_enemigos):
		e = Enemigo()
		e.rect.x = random.randrange(ancho, ancho + 500)
		e.rect.y = random.randrange(alto - e.rect.height)
		enemigos.add(e)
		todos.add(e)

	puntos = 0

	#CICLO PRINCIPAL
	while not fin:

		#Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.KEYDOWN:
				# if event.key == pygame.K_RIGHT:
				# 	jugador.vel_x = 5
				# 	jugador.vel_y = 0
				# if event.key == pygame.K_LEFT:
				# 	jugador.vel_x = -5
				# 	jugador.vel_y = 0
				if event.key == pygame.K_DOWN:
					jugador.vel_y = 5
					jugador.vel_x = 0
				if event.key == pygame.K_UP:
					jugador.vel_y = -5
					jugador.vel_x = 0
				if event.key == pygame.K_SPACE:
					b = Bala()
					b.rect.x = jugador.rect.x
					b.rect.y = jugador.rect.y
					Bala.add(b)
					todos.add(b)



		#Logica del juego
		lista_colision = pygame.sprite.spritecollide(jugador, enemigos, True)

		for e in lista_colision:
			puntos += 1
			print "Puntos: " , puntos
		#Refresco de pantalla

		todos.update()
		pantalla.fill(Negro)
		todos.draw(pantalla)
		pygame.display.flip()	
		reloj.tick(clock)		
