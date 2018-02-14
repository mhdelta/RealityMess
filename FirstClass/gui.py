import pygame

if __name__ == '__main__':
	pygame.init()

	pantalla = pygame.display.set_mode([600, 480])
	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print "Quitting ..."
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				print "Click"
