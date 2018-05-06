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
		self.salud = 5
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



class Juger(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.image.load('soldier160x205.png')
		self.image = pygame.transform.scale(self.image, (60,60))
		self.rect = self.image.get_rect()
		self.i = 0
		self.rect.x = 10
		self.rect.y = - 2000
		self.dir = 0
		self.tmp = self.image
		self.vel_x = 7
		self.vel_y = 7
		self.cont = 0
	def update(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		if self.cont > 25:
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
		self.image.fill(Verde)
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


if __name__ == '__main__':
	alto = 500
	ancho = 700
	pygame.init()
	pantalla = pygame.display.set_mode([700, 500])
	reloj  = pygame.time.Clock()
	fondo = pygame.image.load('backgroundConMuros.png')

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
	todos = pygame.sprite.Group()


	# Objetos

	# barril = Barril(30, 80, [200,200])
	# barriles.add(barril)
	# todos.add(barril)
	jugador = Jugador()
	jugadores.add(jugador)
	todos.add(jugador)

	juger = Juger()
	enemigos.add(juger)
	todos.add(juger)

	px = 0
	py = 0
	i=0
	ls_col = []

	#Direcciones
	Dir = [0,0,0,0]
	right = False
	up = False

	fondox = 0
	fondoy = -2485

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
				###########################

				if event.key == pygame.K_SPACE:
					b = Bala()
					b.rect.x = jugador.rect.x + 25 
					b.rect.y = jugador.rect.y + 25
					if jugador.dir == 5:
						b.rect.y += 20
					if jugador.dir == 3:
						b.rect.x -= 10
					if jugador.dir == 2:
						b.rect.y -= 10
					b.dire = jugador.dir
					balas.add(b)
					todos.add(b)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					Dir[3] = 0
				if event.key == pygame.K_DOWN:
					Dir[2] = 0
				if event.key == pygame.K_RIGHT:
					Dir[0] = 0
				if event.key == pygame.K_LEFT:
					Dir[1] = 0
				if event.key != pygame.K_SPACE:
					jugador.vel_x = 0
					jugador.vel_y = 0
					
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

		for e in enemigos:
			if e.rect.x > ancho + 4000 or e.rect.x < - 4000:
				enemigos.remove(e)
				todos.remove(e)
			if e.rect.y > alto + 4000 or e.rect.y < -4000:
				enemigos.remove(e)
				todos.remove(e)
		
		for b in balas:
			col = pygame.sprite.spritecollide(b, enemigos, True)
		
		for b in balas_enemigas:
			ls_col_ebalas = pygame.sprite.spritecollide(b, jugadores, False)

			if jugador in ls_col_ebalas:
				balas_enemigas.remove(b)
				todos.remove(b)
				jugador.salud -= 1
				print "Salud: ", jugador.salud

		#REFRESCO DE PANTALLA
		if jugador.salud > 0:
			todos.update()
			if fondox >= 0:
				fondox = 0
			if fondoy >= -10:
				fondoy = -10
			if fondox <= -3270:
				fondox = -3270
			if fondoy <= -2485:
				fondoy = -2485
			
			pantalla.blit(fondo,(fondox,fondoy))
			texto = fuente.render("Salud Jugador 1:", False, Blanco)
			txt_valor = fuente.render(str(jugador.salud), False, Blanco)	
			pantalla.blit(texto, [50, 10])
			pantalla.blit(txt_valor, [250, 10])
			print fondox , ",", fondoy
			if jugador.rect.x < 150:
				fondox += 15
				for e in enemigos:
					if fondox <= -100:
						e.rect.x += 15
				jugador.rect.x = 150
			if jugador.rect.x > 550:
				fondox -= 15
				for e in enemigos:
					if fondox >= -3265:
						e.rect.x -= 15
				jugador.rect.x = 550
			if jugador.rect.y < 150:
				fondoy += 15
				for e in enemigos:
					if fondoy <= -100:
						e.rect.y += 15
				jugador.rect.y = 150			
			if jugador.rect.y > 350:
				fondoy -= 15
				for e in enemigos:
					if fondoy >= -2480:
						e.rect.y -= 15	
				jugador.rect.y = 350			
			todos.draw(pantalla)
		else:
			pantalla.fill(Negro)
			fuente2 = pygame.font.Font(None, 50)
			texto = fuente2.render("HAS MUERTO", False, Rojo)
			pantalla.blit(texto, [ancho/2 - 100, alto/2 - 50])
		pygame.display.flip()	
		reloj.tick(clock)		
