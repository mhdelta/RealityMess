import pygame
import random
import math
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
	def __init__(self, nom_imagen):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.image.load(nom_imagen)
		self.image = pygame.transform.scale(self.image, (50,50))
		self.rect = self.image.get_rect()
		self.i = 0
		self.rect.x = 100
		self.rect.y = 200
		self.dir = 0
		self.tmp = self.image
		self.vel_x = 0
		self.vel_y = 0
		self.salud = 20
		self.sonido_bala = pygame.mixer.Sound('fire.ogg')
		self.sonido_golpe = pygame.mixer.Sound('theircoming3.ogg')
		self.sonido_golpe.set_volume(0.5)
		self.sonido_muerte = pygame.mixer.Sound('die.wav')
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
	def disparar(self):
		if self.salud > 0:
			b = Bala()
			self.sonido_bala.play()
			b.rect.x = self.rect.x + 25 
			b.rect.y = self.rect.y + 25
			if self.dir == 5:
				b.rect.y += 20
			if self.dir == 3:
				b.rect.x -= 10
			if self.dir == 2:
				b.rect.y -= 10
			b.dire = self.dir
			balas.add(b)
			todos.add(b)


class Juger(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.image.load('space2.png')
		self.image = pygame.transform.scale(self.image, (40,40))
		self.rect = self.image.get_rect()
		self.i = 0
		self.rect.x = 0
		self.rect.y = 0
		self.dir = 0
		self.tmp = self.image
		self.vel_x = -10
		self.vel_y = -10
		self.cont = 0
		self.sonido = pygame.mixer.Sound('Explosion7.wav')
		
	def update(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		if self.cont > 50:
			self.disparar()
			self.cont = 0
		self.cont += 1
	def disparar(self):
		for i in range(1, 8):
			b = Bala_enemiga()
			b.rect.x = self.rect.x 
			b.rect.y = self.rect.y
			b.dire = i
			balas_enemigas.add(b)
			todos.add(b)

class Persecutor(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.image.load('spaceship.png')
		self.image = pygame.transform.scale(self.image, (150,150))
		self.rect = self.image.get_rect()
		self.i = 0
		self.rect.x = 4000
		self.rect.y = 0
		self.dir = 0
		self.tmp = self.image
		self.vel_x = -12
		self.vel_y = -12
		self.sonido = pygame.mixer.Sound('explosion.ogg')
		self.sonido.set_volume(0.5)
		self.cont = 0
	def perseguir(self, player):
		#Setting Alpha
		self.image.set_alpha(random.randint(0, 254))
		#Set colorkey To Eliminate Background Color
		# find normalized direction vector (dx, dy) between enemy and player
		dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
		dist = math.hypot(dx, dy)
		if dist > 0:
			dx, dy = dx / dist, dy / dist
		# move along this normalized vector towards the player at current speed			
		self.rect.x += dx * self.vel_x
		self.rect.y += dy * self.vel_y


class Barril(pygame.sprite.Sprite,):
	def __init__(self, anchoM, altoM, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([anchoM, altoM])
		self.image.fill(Blanco)
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

class Bala(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([5, 5])
		self.image.fill(Azul)
		self.rect = self.image.get_rect()
		self.vel_x = 0
		self.vel_y = 0
		self.dire = 0
	def update(self):
		if self.dire == 1:
			self.vel_x = 25
			self.vel_y = 0
		if self.dire == 2:
			self.vel_x = -25
			self.vel_y = 0
		if self.dire == 3:
			self.vel_x = 0
			self.vel_y = 25 
		if self.dire == 4:
			self.vel_x = 0
			self.vel_y = -25
		if self.dire == 5:
			self.vel_x = 25
			self.vel_y = -25
		if self.dire == 6:
			self.vel_x = -25
			self.vel_y = -25
		if self.dire == 7:
			self.vel_x = 25
			self.vel_y = 25
		if self.dire == 8:
			self.vel_x = -25
			self.vel_y = 25
		self.rect.x += self.vel_x	
		self.rect.y += self.vel_y


class Bala_enemiga(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([5, 5])
		self.image.fill(Rojo)
		self.rect = self.image.get_rect()
		self.vel_x = 0
		self.vel_y = 0
		self.speed = 20
		self.dire = 0
	def update(self):
		if self.dire == 1:
			self.vel_x = self.speed
			self.vel_y = 0
		if self.dire == 2:
			self.vel_x = -self.speed
			self.vel_y = 0
		if self.dire == 3:
			self.vel_x = 0
			self.vel_y = self.speed 
		if self.dire == 4:
			self.vel_x = 0
			self.vel_y = -self.speed
		if self.dire == 5:
			self.vel_x = self.speed
			self.vel_y = -self.speed
		if self.dire == 6:
			self.vel_x = -self.speed
			self.vel_y = -self.speed
		if self.dire == 7:
			self.vel_x = self.speed
			self.vel_y = self.speed
		if self.dire == 8:
			self.vel_x = -self.speed
			self.vel_y = self.speed
		self.rect.x += self.vel_x	
		self.rect.y += self.vel_y	


if __name__ == '__main__':
	alto = 500
	ancho = 700
	pygame.init()
	pantalla = pygame.display.set_mode([700, 500])
	reloj  = pygame.time.Clock()
	fondo = pygame.image.load('background.png')
	pygame.mixer.music.load('Orbital.mp3')
	pygame.mixer.music.play(start=0.0)
	pygame.mixer.music.set_volume(0.3)
	fuente = pygame.font.Font(None, 32)
	centro = (ancho/2, alto/2)
	limites = [1,1]
	# m = RecortarMatriz([20, 20], 'soldier160x205.png', limites)

	pygame.display.flip()

	accion = 0

	

	#Grupos
	balas = pygame.sprite.Group()
	balas_enemigas = pygame.sprite.Group()
	jugadores = pygame.sprite.Group()
	barriles = pygame.sprite.Group()
	enemigos = pygame.sprite.Group()
	jugers = pygame.sprite.Group()
	perseguidores = pygame.sprite.Group()
	todos = pygame.sprite.Group()


	# Objetos

	# barril = Barril(30, 80, [200,200])
	# barriles.add(barril)
	# todos.add(barril)
	nom_imagen = 'soldier160x205.png'
	jugador = Jugador(nom_imagen)
	nom_imagen = 'soldier2160x205.png'	
	jugador2 = Jugador(nom_imagen)
	jugadores.add(jugador, jugador2)
	todos.add(jugador, jugador2)

	for i in range(30):
		juger = Juger()
		juger.rect.x = random.randint(2000, 2500)
		juger.rect.y = random.randint(2000, 3000)
		juger.vel_x = random.randint(-10,10)
		juger.vel_y = random.randint(-10, 10)
		enemigos.add(juger)
		jugers.add(juger)
		todos.add(juger)
	for i in range(15):
		per = Persecutor()
		per.rect.x = random.randint(-1000, 3500)
		per.rect.y = random.randint(-1500, 3500)
		per.vel_x = random.randint(-5, -2)
		per.vel_y = random.randint(-5, 5)
		perseguidores.add(per)
		enemigos.add(per)
		todos.add(per)
	persecutor = Persecutor()
	perseguidores.add(persecutor)
	todos.add(persecutor)


	px = 0
	py = 0
	i=0
	ls_col = []

	#Direcciones
	Dir = [0,0,0,0]
	Dir2 = [0,0,0,0]
	right = False
	up = False

	fondox = 0
	fondoy = -2485
	cont1 = 0
	mov_jug1 = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
	mov_jug2 = [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a]
	

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
		if Dir2 == [1,0,0,0]:
			jugador2.dir = 1
		if Dir2 == [0,1,0,0]:
			jugador2.dir = 2
		if Dir2 == [0,0,1,0]:
			jugador2.dir = 3
		if Dir2 == [0,0,0,1]:
			jugador2.dir = 4
		if Dir2 == [1,0,0,1]:
			jugador2.dir = 5
		if Dir2 == [0,1,0,1]:
			jugador2.dir = 6
		if Dir2 == [1,0,1,0]:
			jugador2.dir = 7
		if Dir2 == [0,1,1,0]:
			jugador2.dir = 8									
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
				#--------------------------- jugador 2
				if event.key == pygame.K_d:
					jugador2.vel_x = 10
					Dir2[0] = 1
				if event.key == pygame.K_a:
					jugador2.vel_x = -10
					Dir2[1] = 1
				if event.key == pygame.K_s:
					jugador2.vel_y = 10
					Dir2[2] = 1
				if event.key == pygame.K_w:
					jugador2.vel_y = -10
					Dir2[3] = 1
				if event.key == pygame.K_q:
					fin = True
				###########################

				if event.key == pygame.K_SPACE:
					jugador.disparar()

				if event.key == pygame.K_f:
					jugador2.disparar()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					Dir[3] = 0
				if event.key == pygame.K_DOWN:
					Dir[2] = 0
				if event.key == pygame.K_RIGHT:
					Dir[0] = 0
				if event.key == pygame.K_LEFT:
					Dir[1] = 0
				if event.key != pygame.K_SPACE and event.key in mov_jug1:
					jugador.vel_x = 0
					jugador.vel_y = 0
				if event.key == pygame.K_w:
					Dir2[3] = 0
				if event.key == pygame.K_s:
					Dir2[2] = 0
				if event.key == pygame.K_d:
					Dir2[0] = 0
				if event.key == pygame.K_a:
					Dir2[1] = 0
				if event.key != pygame.K_f and event.key in mov_jug2:
					jugador2.vel_x = 0
					jugador2.vel_y = 0
					
		#Logica del juegO

		if jugador.accion == 2:
			ls_col = pygame.sprite.spritecollide(jugador, barriles, False)
			for b in ls_col:
				b.rect.x += 10

		for b in balas:		
			if b.rect.x > ancho + 4000 or b.rect.x < - 4000:
				balas.remove(b)
				todos.remove(b)
			if b.rect.y > alto + 4000 or b.rect.y < -4000:
				balas.remove(b)
				todos.remove(b)
			col = pygame.sprite.spritecollide(b, enemigos, False)
			for e in enemigos:
				if e in col:
					e.sonido.play()
					enemigos.remove(e)
					todos.remove(e)
					balas.remove(b)
					todos.remove(b)
			col_per = pygame.sprite.spritecollide(b, perseguidores, False)
			for e in perseguidores:
				if e in col_per:
					e.sonido.play()
					perseguidores.remove(e)
					todos.remove(e)
					balas.remove(b)
					todos.remove(b)
			
		
		for b in balas_enemigas:
			ls_col_ebalas = pygame.sprite.spritecollide(b, jugadores, False)
			for j in jugadores:
				if j in ls_col_ebalas:
					j.sonido_golpe.play()
					balas_enemigas.remove(b)
					todos.remove(b)
					j.salud -= 1
		
		for e in perseguidores:
			cont1 += 1
			if cont1 % 2 == 0:
				e.perseguir(jugador)
			else:
				e.perseguir(jugador2)
			if cont1 >= 10:
				cont1 = 0
			ls_col_persecutor = pygame.sprite.spritecollide(e, jugadores, False)
			if jugador in ls_col_persecutor:
				jugador.salud -= 20
				jugador.sonido_muerte.play()
				jugadores.remove(jugador)
				todos.remove(jugador)
			if jugador2 in ls_col_persecutor:
				jugador2.salud -= 20
				jugador2.sonido_muerte.play()
				jugadores.remove(jugador2)
				todos.remove(jugador2)

		for j in jugers:
			if j.rect.x > 4000 or j.rect.x < -4000:
				j.rect.x = 0
			if j.rect.y > 4000 or j.rect.y < -4000:
				j.rect.y = 0
		


		#REFRESCO DE PANTALLA
		if jugador.salud > 0 or jugador2.salud > 0:
			todos.update()
			if fondox >= 0:
				fondox = 0
			if fondoy >= -10:
				fondoy = -10
			if fondox <= -3270:
				fondox = -3270
			if fondoy <= -2485:
				fondoy = -2485
			if jugador.salud > 1:
				pantalla.blit(fondo,(fondox,fondoy))
				texto = fuente.render("Salud Jugador 1:", False, Blanco)
				txt_valor = fuente.render(str(jugador.salud), False, Blanco)	
				pantalla.blit(texto, [50, 10])
				pantalla.blit(txt_valor, [250, 10])
			else:
				pantalla.blit(fondo,(fondox,fondoy))
				texto = fuente.render("MUERTO", False, Rojo)
				pantalla.blit(texto, [200, 10])
			if jugador2.salud > 1:
				texto = fuente.render("Salud Jugador 2:", False, Blanco)
				txt_valor = fuente.render(str(jugador2.salud), False, Blanco)	
				pantalla.blit(texto, [300, 10])
				pantalla.blit(txt_valor, [500, 10])	
			else:
				pantalla.blit(fondo,(fondox,fondoy))
				texto = fuente.render("MUERTO", False, Rojo)
				pantalla.blit(texto, [500, 10])

			if jugador.rect.x < 150 and jugador2.rect.x < 150:
				fondox += 15
				for e in enemigos:
					if fondox <= -100:
						e.rect.x += 15
				jugador.rect.x = 150
				jugador2.rect.x = 150
			if jugador.rect.x > 550 and jugador2.rect.x > 550:
				fondox -= 15
				for e in enemigos:
					if fondox >= -3265:
						e.rect.x -= 15
				jugador.rect.x = 550
				jugador2.rect.x = 550
			if jugador.rect.y < 150 and jugador2.rect.y < 150:
				fondoy += 15
				for e in enemigos:
					if fondoy <= -100:
						e.rect.y += 15
				jugador.rect.y = 150			
				jugador2.rect.y = 150			
			if jugador.rect.y > 350 and jugador2.rect.y > 350:
				fondoy -= 15
				for e in enemigos:
					if fondoy >= -2480:
						e.rect.y -= 15	
				jugador.rect.y = 350
				jugador2.rect.y = 350
			# solo 1 jugador
			if jugador.rect.x < 150:
				jugador.rect.x = 150
			if jugador.rect.x > 550:
				jugador.rect.x = 550
			if jugador.rect.y < 150:
				jugador.rect.y = 150			
			if jugador.rect.y > 350:	
				jugador.rect.y = 350
			if jugador2.rect.x < 150:
				jugador2.rect.x = 150
			if jugador2.rect.x > 550:
				jugador2.rect.x = 550
			if jugador2.rect.y < 150:
				jugador2.rect.y = 150			
			if jugador2.rect.y > 350:	
				jugador2.rect.y = 350			
			todos.draw(pantalla)
		else:
			pantalla.fill(Negro)
			fuente2 = pygame.font.Font(None, 50)
			texto = fuente2.render("HAS MUERTO", False, Rojo)
			jugador.sonido_muerte.fadeout(5000)
			pantalla.blit(texto, [ancho/2 - 100, alto/2 - 50])
		pygame.display.flip()	
		reloj.tick(clock)		
