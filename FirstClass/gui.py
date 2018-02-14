import pygame
import os
from random import randint

if __name__ == '__main__':
	pygame.init()

	pantalla = pygame.display.set_mode([600, 480])

	#pygame.draw.line(pantalla, [0, 0, 150], [0,600], [200,600], 9)

	#img = pygame.image.load(os.path.join('../images', 'fighter.jpg'))

	#pantalla.blit(img, (0,200))

	pygame.display.flip()


	firstClick = False
	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print "Quitting ..."
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				###########COLORlINES
				# if firstClick:
				# 	secondClick = True
				# 	c,d = pygame.mouse.get_pos()
				# 	color = [randint(0, 255), randint(0, 255), randint(0, 255)]
				# 	pygame.draw.line(pantalla, color, [a,b], [c,d], 60)
				# 	pygame.display.flip()
				# 	a = c
				# 	b = d
				# else:
				# 	firstClick = True	
				# 	a,b = pygame.mouse.get_pos()
				# # event.pos



						