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

		self.salud = 5



	def update(self):
		# self.rect.x += self.vel_x

		if self.rect.y >= 75:
			self.rect.y += self.vel_y
		else:
			self.rect.y = 75
			self.vel_y = 0
		if self.rect.y > (alto - self.rect.height):
			self.rect.y = alto - self.rect.height




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
		self.disparar = False
		self.temp = random.randrange(100)

	def update(self):
		#self.rect.y += self.vel_y

		if self.temp > 0:
			self.temp -= 1
		else:
			self.disparar = True

		if self.espera > 0:
			self.espera -= 1
		else:
			self.rect.x += self.vel_x
				
class Bala(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([15,15])
		self.image.fill(Blanco)
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
	puntos = 0


	#Grupos
	todos = pygame.sprite.Group()
	jugadores = pygame.sprite.Group()
	enemigos = pygame.sprite.Group()
	balas = pygame.sprite.Group()
	ebalas = pygame.sprite.Group()

	jugador = Jugador()
	jugadores.add(jugador)
	todos.add(jugador)



	num_enemigos = 10

	for i in range(num_enemigos):
		e = Enemigo()
		e.rect.x = random.randrange(ancho, ancho + 500)
		e.rect.y = random.randrange(75, alto - e.rect.height)
		enemigos.add(e)
		todos.add(e)



	fuente = pygame.font.Font(None, 32)

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
					balas.add(b)
					todos.add(b)
			# if event.type == pygame.KEYUP:
			# 	jugador.vel_y = 0



		#Logica del juego
		cont_eliminados = 0
		lista_colision = pygame.sprite.spritecollide(jugador, enemigos, True)

		for e in lista_colision:
			# puntos += 1
			# print "Puntos: " , puntos
			enemigos.remove(e)
			todos.remove(e)
			cont_eliminados += 1
			jugador.salud -= 1
			print "Salud: ", jugador.salud

		for b in balas:
			ls_col_balas = pygame.sprite.spritecollide(b, enemigos, True)

			for e in ls_col_balas:
				enemigos.remove(e)
				todos.remove(e)
				balas.remove(b)
				todos.remove(b)
				cont_eliminados+=1 

		for b in ebalas:
			ls_col_ebalas = pygame.sprite.spritecollide(b, jugadores, False)

			if jugador in ls_col_ebalas:
				ebalas.remove(b)
				todos.remove(b)
				jugador.salud -= 1
				print "Salud: ", jugador.salud


		for e in enemigos:
			if e.disparar:
				e.temp = random.randrange(100)
				e.disparar = False
				b_enem = Bala()
				b_enem.rect.x = e.rect.x
				b_enem.rect.y = e.rect.y
				b_enem.vel_x = -10
				todos.add(b_enem)
				ebalas.add(b_enem)

			if e.rect.x < 0:
				enemigos.remove(e)
				todos.remove(e)
				cont_eliminados += 1

		for i in range(cont_eliminados):
			e = Enemigo()
			e.rect.x = random.randrange(ancho, ancho + 500)
			e.rect.y = random.randrange(75, alto - e.rect.height)
			enemigos.add(e)
			todos.add(e)

		for b in balas:
			if b.rect.x > ancho:
				balas.remove(b)
				todos.remove(b)

		for b in ebalas:	
			if b.rect.x < 0:
				ebalas.remove(b)
				todos.remove(b)

		#Refresco de pantalla

		todos.update()
		pantalla.fill(Negro)

		texto = fuente.render("Salud ", False, Blanco)
		txt_valor = fuente.render(str(jugador.salud), False, Blanco)	
		pantalla.blit(texto, [30, 10])
		pantalla.blit(txt_valor, [1000, 10])

		todos.draw(pantalla)
		pygame.display.flip()	
		reloj.tick(clock)		
