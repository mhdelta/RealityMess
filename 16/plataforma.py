import pygame
import random

alto=480
ancho=640
rojo=[255,0,0]
verde=[0,255,0]
negro=[0,0,0]
blanco=[255,255,255]
azul=[0,0,100]

class cjugador (pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill(verde)
        self.rect=self.image.get_rect()
        self.vel_y=0
        self.vel_x=0
        self.pls=None

    def gravedad(self):
        if self.vel_y == 0:
            self.vel_y=1
        else:
            self.vel_y+=0.5

    def update(self):
        self.gravedad()
        self.rect.y += self.vel_y
        if self.rect.y >= (alto-self.rect.height): #limite inferior y superior
            self.rect.y = alto - self.rect.height
            self.vel_y=0

        col=pygame.sprite.spritecollide(self, self.pls, False)
        for p in col:
            if (self.vel_y<=0) and (self.rect.top <= p.rect.bottom):
                self.rect.top=p.rect.bottom
                self.vel_y+=1
            elif(self.vel_y>=0) and self.rect.bottom >= p.rect.top:
                self.rect.bottom = p.rect.top
                self.vel_y=0

        col=pygame.sprite.spritecollide(self, self.pls, False)
        for p in col:
            if (self.vel_x>0) and (self.rect.right >= p.rect.left):
                self.rect.right=p.rect.left
            elif(self.vel_y<0) and self.rect.left <= p.rect.right:
                self.rect.bottom = p.rect.top
            '''
            if self.vel_y<=self.rect.top <= p.rect.bottom:
                self.rect.top=p.rect.bottom
            elif self.rect.right >= p.rect.left:
                self.rect.right=p.rect.left
            elif self.rect.left <= p.rect.right:
                self.rect.left=p.rect.right
            elif self.rect.bottom >= p.rect.top:
                self.rect.bottom=p.rect.top
            '''

        self.rect.x += self.vel_x

class plataforma (pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill(negro)
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.dir=0

    def update(self):
        if self.dir==0:
            self.rect.x +=2
        else:
            self.rect.x +=-2

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    todos = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()

    jugadores = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()

    pl=plataforma(100,30)
    pl.rect.y=300
    pl.rect.x=350
    plataformas.add(pl)
    todos.add(pl)

    jugador=cjugador(40,60)
    jugador.pls=plataformas
    jugadores.add(jugador)
    todos.add(jugador)

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #if jugador.vel_y==0:
                    jugador.vel_y=-10
                if event.key == pygame.K_DOWN:
                    jugador.vel_y=5
                if event.key == pygame.K_RIGHT:
                    jugador.vel_x=5
                if event.key == pygame.K_LEFT:
                    jugador.vel_x=-5

            if event.type == pygame.KEYUP:
                jugador.vel_x=0


        for p in plataformas:
            if p.rect.x==400:
                p.dir=1
            if p.rect.x==100:
                p.dir=0

        todos.update()
        pantalla.fill(blanco)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
