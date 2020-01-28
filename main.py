import pygame

pygame.init()
width, height = 800,  600
dvdlogoSpeed = [1,1]
backgroundColor = 255,  0,  0

screen = pygame.display.set_mode((width, height))

dvdLogo = pygame.image.load("dvd-logo-white.png")

dvdLogoRect = dvdLogo.get_rect()

while True:
	  screen.fill(backgroundColor)

    screen.blit(dvdLogo, dvdLogoRect)

	  pygame.display.flip()
