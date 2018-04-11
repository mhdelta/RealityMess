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
clock = 50

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


class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([30,30])
		self.image.fill(Rojo)
		self.rect = self.image.get_rect()
		self.rect.x = ancho-30
		self.rect.y = alto-30
		self.vel_x = -5
		self.vel_y = 0

	def update(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y


class Muro(pygame.sprite.Sprite,):
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
	pantalla = pygame.display.set_mode([1000, 1000])
	pygame.display.flip()
	reloj  = pygame.time.Clock()

	
	centro = (ancho/2, alto/2)


	#Grupos

	jugadores = pygame.sprite.Group()
	muros = pygame.sprite.Group()
	enemigos = pygame.sprite.Group()
	todos = pygame.sprite.Group()


	# Objetos

	jugador = Jugador()
	jugadores.add(jugador)
	todos.add(jugador)

	enemigo = Enemigo()
	enemigos.add(enemigo)
	todos.add(enemigo)

	#Muros del borde
	m1 = Muro(ancho, 10, [0,-10])
	m2 = Muro(10, alto, [-10,0])
	m3 = Muro(10, alto, [ancho,0])
	m4 = Muro(ancho, 10, [0,alto])
	muros.add(m1, m2, m3, m4)

	#Muros del laberinto

	ml1 = Muro(100, 300, [100, 100])
	ml2 = Muro(500, 30, [200, 300])
	ml3 = Muro(100, 200, [400, 20])
	muros.add(ml1, ml2, ml3)
	


	todos.add(muros)

	#Enemigo softbot




	#CICLO PRINCIPAL
	while not fin:

		#Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					jugador.vel_x = 5
					jugador.vel_y = 0
				if event.key == pygame.K_LEFT:
					jugador.vel_x = -5
					jugador.vel_y = 0
				if event.key == pygame.K_DOWN:
					jugador.vel_y = 5
					jugador.vel_x = 0
				if event.key == pygame.K_UP:
					jugador.vel_y = -5
					jugador.vel_x = 0
					
			if event.type == pygame.KEYUP:
				jugador.vel_x = 0
				jugador.vel_y = 0


		#Logica del juego




		#Colisiones con los muros
		ls_col = pygame.sprite.spritecollide(jugador, muros, False)
		for m in ls_col:
			if  (jugador.vel_x > 0) and jugador.rect.right >= m.rect.left:
				jugador.vel_x = 0
				jugador.rect.right = m.rect.left

			if  (jugador.vel_x < 0) and jugador.rect.left <= m.rect.right:
				jugador.vel_x = 0
				jugador.rect.left = m.rect.right

			if  (jugador.vel_y > 0) and jugador.rect.bottom >= m.rect.top:
				jugador.vel_y = 0
				jugador.rect.bottom = m.rect.top
				
			if  (jugador.vel_y < 0) and jugador.rect.top <= m.rect.bottom:
				jugador.vel_y = 0
				jugador.rect.top = m.rect.bottom

		ls_col_enemigo = pygame.sprite.spritecollide(enemigo, muros, False)
		for m in ls_col_enemigo:
			if  (enemigo.vel_x > 0) and enemigo.rect.right >= m.rect.left:
				enemigo.vel_x = 0
				enemigo.vel_y = 5
				enemigo.rect.right = m.rect.left

			elif  (enemigo.vel_x < 0) and enemigo.rect.left <= m.rect.right:
				enemigo.vel_x = 0
				enemigo.vel_y = -5
				enemigo.rect.left = m.rect.right

			elif  (enemigo.vel_y > 0) and enemigo.rect.bottom >= m.rect.top:
				enemigo.vel_y = 0
				enemigo.vel_x = -5
				enemigo.rect.bottom = m.rect.top
				
			elif  (enemigo.vel_y < 0) and enemigo.rect.top <= m.rect.bottom:
				enemigo.vel_y = 0
				enemigo.vel_x = 5
				enemigo.rect.top = m.rect.bottom

		#Refresco de pantalla
		todos.update()
		pantalla.fill(Negro)

		todos.draw(pantalla)

		pygame.display.flip()	
		reloj.tick(clock)		
