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
		self.rect.x = 250
		self.rect.y = 350
		self.dir = 0
		self.tmp = self.image
		self.vel_x = 0
		self.vel_y = 0
		self.salud = 20
		self.sonido_bala = pygame.mixer.Sound('fire.ogg')
		self.sonido_golpe = pygame.mixer.Sound('theircoming3.ogg')
		self.sonido_golpe.set_volume(0.5)
		self.sonido_muerte = pygame.mixer.Sound('die.wav')
		self.spd = 10
		self.more_bullets = 0
	def update(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		#  muros
		m_col =  pygame.sprite.spritecollide(self, muros, False)	
		for m in m_col:
			if self.vel_x == 0 and self.vel_y == 0:
				pass
			# up
			if self.vel_y < 0:
				self.rect.y += (self.spd + 1)
			# down
			if self.vel_y > 0 :
				self.rect.y -= (self.spd + 1)
			# left
			if self.vel_x < 0:
				self.rect.x += (self.spd + 1)
			# right
			if self.vel_x > 0:
				self.rect.x -= (self.spd + 1)

		p_col =  pygame.sprite.spritecollide(self, pociones, False)
		for p in p_col:
			if p.tipo == 0:
				self.salud += 10
			if p.tipo == 1:
				self.spd += 5
			if p.tipo == 2:
				self.more_bullets = 1
			if p.tipo == 3:
				for m in minas:
					m.kill()
			pociones.remove(p)
			todos.remove(p)
			

		if self.salud == 0:
			self.kill()
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
			if self.more_bullets == 1:
				for i in range(1, 8):
					b = Bala()
					b.rect.x = self.rect.x 
					b.rect.y = self.rect.y
					b.dire = i
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
		self.sonido = pygame.mixer.Sound('bomb.ogg')
		self.sonido.set_volume(0.3)
		
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
		self.vel_x = 0
		self.vel_y = 0
		self.sonido = pygame.mixer.Sound('explosion.ogg')
		self.sonido.set_volume(0.6)
		self.i = 0
		self.m = RecortarMatriz([4, 4], 'exp.png', [4, 4, 4, 4])
	def perseguir(self, player):
		#Setting Alpha
		self.image.set_alpha(random.randint(0, 254))
		#Set colorkey To Eliminate Background Color
		# find normalized direction vector (dx, dy) between enemy and player
		dx, dy = self.rect.x - player.rect.x,self.rect.y - player.rect.y
		dist = math.hypot(dx, dy)
		if dist > 0:
			dx, dy = dx / dist, dy / dist
		# move along this normalized vector towards the player at current speed
		adx, ady = abs(dx), abs(dy)
		if dx > 0 and dy > 0:
			self.rect.x -= adx * self.vel_x
			self.rect.y -= ady * self.vel_y
		if dx < 0 and dy > 0:
			self.rect.x += adx * self.vel_x
			self.rect.y -= ady * self.vel_y
		if dx > 0 and dy < 0:
			self.rect.x -= adx * self.vel_x
			self.rect.y += ady * self.vel_y
		if dx < 0 and dy < 0:
			self.rect.x += adx * self.vel_x
			self.rect.y += ady * self.vel_y

class Mina(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.image.load('mina.png')
		self.image = pygame.transform.scale(self.image, (100,100))
		self.rect = self.image.get_rect()
		self.i = 0
		self.rect.x = pos[0]
		self.rect.y = pos[1]
	# def update(self):

class Pocion(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([50, 50])
		self.image.fill(Negro)
		self.image = pygame.transform.scale(self.image, (50,50))
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.tipo = 0
	def update(self):
		if self.tipo == 0:
			self.image = pygame.image.load('potiVerde.png')
			self.image = pygame.transform.scale(self.image, (50,50))
		if self.tipo == 1:
			self.image = pygame.image.load('potiAzul.png')
			self.image = pygame.transform.scale(self.image, (50,50))			
		if self.tipo == 2:
			self.image = pygame.image.load('potiRoja.png')
			self.image = pygame.transform.scale(self.image, (50,50))			
		if self.tipo == 3:
			self.image = pygame.image.load('potiamarilla.png')
			self.image = pygame.transform.scale(self.image, (50,50))			

		# Collition


class Muro(pygame.sprite.Sprite,):
	def __init__(self, size, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('muro.png')
		self.image = pygame.transform.scale(self.image, (size[0], size[1]))
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

class explosion(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.Surface([20, 20])
		self.image.fill(Negro)
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]		
		self.sonido = pygame.mixer.Sound('explosion.ogg')
		self.sonido.set_volume(0.7)
		self.m = RecortarMatriz([4, 4], 'exp.png', [4, 4, 4, 4])
		self.fila = 0
		self.col = 0
		self.size = 0
	def update(self):
		if self.fila == 0:	
			self.fila = 3
		else:
			self.fila -=1
		if self.col == 0:
			self.col = 3
		else:
			self.col -=1
		if self.fila == 0 and self.col ==0:
			self.kill() 
		self.image = self.m[self.fila][self.col]
		if self.size == 0:
			self.image = pygame.transform.scale(self.image, (50,50))
		elif self.size == 1:
			self.image = pygame.transform.scale(self.image, (150,150))			
		elif self.size == 2:
			self.image = pygame.transform.scale(self.image, (250,250))
class explosion_sang(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.accion = 1
		self.image = pygame.Surface([20, 20])
		self.image.fill(Negro)
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]		
		self.sonido = pygame.mixer.Sound('explosion.ogg')
		self.sonido.set_volume(0.6)
		self.m = RecortarMatriz([5, 7], 'blood.png', [5, 5, 5, 5, 5, 5, 3])					
		self.i = 0
		self.fila = 0
		self.col = 0
		self.size = 0
	def update(self):
		if self.col == 4:
			self.col = 0
			self.fila += 1
		else:
			self.col += 1
		if self.fila == 6 and self.col == 2:
			self.kill()
			
		self.image = self.m[self.fila][self.col]
		if self.size == 0:
			self.image = pygame.transform.scale(self.image, (50,50))
		elif self.size == 1:
			self.image = pygame.transform.scale(self.image, (150,150))
		elif self.size == 2:
			self.image = pygame.transform.scale(self.image, (250,250))
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
		if self.dire == 4 or self.dire == 0:
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

	juego_fin = False

	#Grupos
	muros = pygame.sprite.Group()
	balas = pygame.sprite.Group()
	balas_enemigas = pygame.sprite.Group()
	jugadores = pygame.sprite.Group()
	barriles = pygame.sprite.Group()
	enemigos = pygame.sprite.Group()
	jugers = pygame.sprite.Group()
	perseguidores = pygame.sprite.Group()
	explosiones = pygame.sprite.Group()
	minas = pygame.sprite.Group()
	pociones = pygame.sprite.Group()
	todos = pygame.sprite.Group()


	# Objetos

	level = [
	"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
	"W  0   0      0   3  0   0   W      W",
	"W     0 m  WWWWWW    0   0   m      W",
	"W   WWWW  2    W     0   W    WW    W",
	"Wm  W   0   m WWWW   0   0     m    W",
	"W   W  WWWW    2     2   2   W W  W W",
	"W 0 W  3  W W  m     W   0          W",
	"W   W     W   WWW WWWWWWWW   W m  m W",
	"W   WWW WWW   W W    m	   1   W     W",
	"W  0  W   W   W W    0   1   m  W   W",
	"WWW   W   WWWWW W    W   0          W",
	"W W  3   WW   1      W   W   W  W W W",
	"W W m WWWW   WWW     W   1  m   m   W",
	"W     W    E   W     0   0          W",
	"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
	]

	# Parse the level string above. W = wall, E = exit
	x = y = 0
	for row in level:
		for col in row:
			if col == "W":
				muro = Muro([100, 100], [x, y])
				muros.add(muro)
				todos.add(muro)
			if col == '0':
				poti = Pocion([x, y])
				poti.tipo = 0
				pociones.add(poti)
				todos.add(poti)
			if col == '1':
				poti = Pocion([x, y])
				poti.tipo = 1
				pociones.add(poti)
				todos.add(poti)
			if col == '2':
				poti = Pocion([x, y])
				poti.tipo = 2
				pociones.add(poti)
				todos.add(poti)
			if col == '3':
				poti = Pocion([x, y])
				poti.tipo = 3
				pociones.add(poti)
				todos.add(poti)
			if col == 'm':
				mina = Mina([x,y])
				minas.add(mina)
				todos.add(mina)
			x += 100
		y += 100
		x = 0

	nom_imagen = 'soldier160x205.png'
	jugador = Jugador(nom_imagen)
	nom_imagen = 'soldier2160x205.png'	
	jugador2 = Jugador(nom_imagen)
	jugador.nombre = "jugador1"
	jugador2.nombre = "jugador2"
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
	for i in range(20):
		per = Persecutor()
		per.rect.x = random.randint(-1000, 3500)
		per.rect.y = random.randint(-1500, 3500)
		per.vel_x = random.randint(0, 5)
		per.vel_y = random.randint(0, 5)
		perseguidores.add(per)
		enemigos.add(per)
		todos.add(per)
	# per = Persecutor()
	# per.rect.x =  200
	# per.rect.y =  500
	# per.vel_x =  5
	# per.vel_y =  5
	# perseguidores.add(per)
	# enemigos.add(per)
	# todos.add(per)


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
					jugador.vel_x = jugador.spd
					Dir[0] = 1
				if event.key == pygame.K_LEFT:
					jugador.vel_x = -jugador.spd
					Dir[1] = 1
				if event.key == pygame.K_DOWN:
					jugador.vel_y =jugador.spd
					Dir[2] = 1
				if event.key == pygame.K_UP:
					jugador.vel_y = -jugador.spd
					Dir[3] = 1
				#--------------------------- jugador 2
				if event.key == pygame.K_d:
					jugador2.vel_x = jugador2.spd
					Dir2[0] = 1
				if event.key == pygame.K_a:
					jugador2.vel_x = -jugador2.spd
					Dir2[1] = 1
				if event.key == pygame.K_s:
					jugador2.vel_y = jugador2.spd
					Dir2[2] = 1
				if event.key == pygame.K_w:
					jugador2.vel_y = -jugador2.spd
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
		# ojo con el error aqui
		for m in minas:
			col_minas = pygame.sprite.spritecollide(m, jugadores, False)
			for j in jugadores:
				if j in col_minas:
					exp = explosion([m.rect.x, m.rect.y])
					exp.size = 2
					exp.sonido.play()
					exp_s = explosion_sang([j.rect.x, j.rect.y])
					exp_s.size = 2
					explosiones.add(exp, exp_s)
					todos.add(exp, exp_s)
					m.kill()
					j.kill()
					j.salud = 0;

		for b in balas:		
			if b.rect.x > ancho + 4000 or b.rect.x < - 4000:
				balas.remove(b)
				todos.remove(b)
			if b.rect.y > alto + 4000 or b.rect.y < -4000:
				balas.remove(b)
				todos.remove(b)
			col_m = pygame.sprite.spritecollide(b, muros, False)
			if b in col_m:
				balas.remove(b)
				todos.remove(b)
		
			col = pygame.sprite.spritecollide(b, enemigos, False)
			for e in enemigos:
				if e in col and e not in minas:		
					e.sonido.play()
					exp = explosion([e.rect.x, e.rect.y])
					if e in perseguidores:
						exp.size = 1
					explosiones.add(exp)
					todos.add(exp)
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
					exp_sang = explosion_sang([j.rect.x, j.rect.y])
					explosiones.add(exp_sang)
					todos.add(exp_sang)
					balas_enemigas.remove(b)
					todos.remove(b)
					j.salud -= 1
		
		for e in perseguidores:
			cont1 += 1
			if cont1 % 2 == 0:
				if jugador.salud > 0:
					e.perseguir(jugador)
				else:
					e.perseguir(jugador2)
			else:
				if jugador.salud > 0:
					e.perseguir(jugador)
				else:
					e.perseguir(jugador2)
			if cont1 >= 10:
				cont1 = 0
			ls_col_persecutor = pygame.sprite.spritecollide(e, jugadores, False)
			if jugador in ls_col_persecutor:
				jugador.salud = 0
				jugador.sonido_muerte.play()
				exp_sang = explosion_sang([jugador.rect.x, jugador.rect.y])
				exp_sang.size = 1
				explosiones.add(exp_sang)
				todos.add(exp_sang)
				jugadores.remove(jugador)
				todos.remove(jugador)
			if jugador2 in ls_col_persecutor:
				jugador2.salud = 0
				jugador2.sonido_muerte.play()
				exp_sang = explosion_sang([jugador2.rect.x + 25, jugador2.rect.y + 25])
				exp_sang.size = 1
				explosiones.add(exp_sang)
				todos.add(exp_sang)
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
			pantalla.blit(fondo,(fondox,fondoy))			

			if jugador.salud > 0 and jugador2.salud > 0:
				ambos_vivos = True
			else:
				ambos_vivos = False
			if ambos_vivos:
				if jugador.rect.x < 150 and jugador2.rect.x < 150:
					fondox += 15
					for mi in minas:
						mi.rect.x += 15
					for p in pociones:
						p.rect.x += 15
					for m in muros:
						m.rect.x += 15
					for e in enemigos:
						if fondox <= -100:
							e.rect.x += 15
					jugador.rect.x = 150
					jugador2.rect.x = 150
				if jugador.rect.x > 550 and jugador2.rect.x > 550:
					fondox -= 15
					for mi in minas:
						mi.rect.x -= 15
					for p in pociones:
						p.rect.x -= 15
					for m in muros:
						m.rect.x -= 15
					for e in enemigos:
						if fondox >= -3265:
							e.rect.x -= 15
					jugador.rect.x = 550
					jugador2.rect.x = 550
				if jugador.rect.y < 150 and jugador2.rect.y < 150:
					fondoy += 15
					for mi in minas:
						mi.rect.y += 15
					for p in pociones:
						p.rect.y += 15
					for m in muros:
						m.rect.y += 15
					for e in enemigos:
						if fondoy <= -100:
							e.rect.y += 15
					jugador.rect.y = 150			
					jugador2.rect.y = 150			
				if jugador.rect.y > 350 and jugador2.rect.y > 350:
					fondoy -= 15
					for mi in minas:
						mi.rect.y -= 15
					for p in pociones:
						p.rect.y -= 15
					for m in muros:
						m.rect.y -= 15
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
			else:
				if jugador.rect.x < 150:
					fondox += 15
					for m in minas:
						m.rect.x += 15
					for p in pociones:
						p.rect.x += 15
					for m in muros:
						m.rect.x += 15
					for e in enemigos:
						if fondox <= -100:
							e.rect.x += 15
					jugador.rect.x = 150
				if jugador.rect.x > 550:
					fondox -= 15
					for m in minas:
						m.rect.x -= 15
					for p in pociones:
						p.rect.x -= 15
					for m in muros:
						m.rect.x -= 15
					for e in enemigos:
						if fondox >= -3265:
							e.rect.x -= 15
					jugador.rect.x = 550
				if jugador.rect.y < 150:
					fondoy += 15
					for m in minas:
						m.rect.y += 15
					for p in pociones:
						p.rect.y += 15
					for m in muros:
						m.rect.y += 15
					for e in enemigos:
						if fondoy <= -100:
							e.rect.y += 15
					jugador.rect.y = 150			
				if jugador.rect.y > 350:
					fondoy -= 15
					for m in minas:
						m.rect.y -= 15
					for p in pociones:
						p.rect.y -= 15
					for m in muros:
						m.rect.y -= 15
					for e in enemigos:
						if fondoy >= -2480:
							e.rect.y -= 15	
					jugador.rect.y = 350
				if jugador2.rect.x < 150:
					fondox += 15
					for m in minas:
						m.rect.x += 15
					for p in pociones:
						p.rect.x += 15
					for m in muros:
						m.rect.x += 15
					for e in enemigos:
						if fondox <= -100:
							e.rect.x += 15
					jugador2.rect.x = 150
				if jugador2.rect.x > 550:
					fondox -= 15
					for m in minas:
						m.rect.x -= 15
					for p in pociones:
						p.rect.x -= 15
					for m in muros:
						m.rect.x -= 15
					for e in enemigos:
						if fondox >= -3265:
							e.rect.x -= 15
					jugador2.rect.x = 550
				if jugador2.rect.y < 150:
					fondoy += 15
					for m in minas:
						m.rect.y += 15
					for p in pociones:
						p.rect.y += 15
					for m in muros:
						m.rect.y += 15
					for e in enemigos:
						if fondoy <= -100:
							e.rect.y += 15
					jugador2.rect.y = 150			
				if jugador2.rect.y > 350:
					fondoy -= 15
					for m in minas:
						m.rect.y -= 15
					for p in pociones:
						p.rect.y -= 15
					for m in muros:
						m.rect.y -= 15
					for e in enemigos:
						if fondoy >= -2480:
							e.rect.y -= 15	
					jugador2.rect.y = 350
			todos.draw(pantalla)	
			if jugador.salud >= 1:
				texto = fuente.render("Salud Jugador 1:", False, Blanco)
				txt_valor = fuente.render(str(jugador.salud), False, Blanco)	
				pantalla.blit(texto, [50, 10])
				pantalla.blit(txt_valor, [250, 10])
			else:
				texto = fuente.render("MUERTO", False, Rojo)
				pantalla.blit(texto, [200, 10])
			if jugador2.salud >= 1:
				texto = fuente.render("Salud Jugador 2:", False, Blanco)
				txt_valor = fuente.render(str(jugador2.salud), False, Blanco)	
				pantalla.blit(texto, [300, 10])
				pantalla.blit(txt_valor, [500, 10])	
			else:
				texto = fuente.render("MUERTO", False, Rojo)
				pantalla.blit(texto, [500, 10])
			fuente3 = pygame.font.Font(None, 50)
			sec_restantes = 120 - (pygame.time.get_ticks()/1000)
			if sec_restantes >= 20:
				texto4 = fuente3.render("Tiempo restante: ", False, Blanco)		
				pantalla.blit(texto4, [50, 50])
				txt_valor4 = fuente3.render(str(sec_restantes), False, Blanco)
			else:
				texto4 = fuente3.render("Tiempo restante: ", False, Rojo)		
				pantalla.blit(texto4, [50, 50])
				txt_valor = fuente3.render(str(sec_restantes), False, Rojo)
			pantalla.blit(txt_valor4, [400, 50])			
		else:
			pantalla.fill(Negro)
			fuente2 = pygame.font.Font(None, 50)
			texto5 = fuente2.render("HAS MUERTO", False, Rojo)
			jugador.sonido_muerte.fadeout(5000)
			pantalla.blit(texto5, [ancho/2 - 100, alto/2 - 50])
		if sec_restantes == 0 or juego_fin:
			for t in todos:
				t.kill()
			pantalla.fill(Blanco)
			fuente2 = pygame.font.Font(None, 70)
			texto7 = fuente2.render("Felicitaciones", False, Rojo)
			pantalla.blit(texto7, [ancho/2 - 200, alto/2 - 50])
			juego_fin = True
		pygame.display.flip()	
		reloj.tick(clock)		
