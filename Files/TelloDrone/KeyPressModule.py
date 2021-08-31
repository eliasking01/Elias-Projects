import pygame

def init():
	pygame.init()
	win = pygame.display.set_mode((400, 400))
	return win

def text(battery, win):
	win.fill(pygame.Color("black")) # erases the entire screen surface
	font = pygame.font.SysFont("monospace", 30)
	text = font.render("Battery: " + battery + "%", True, (0, 128, 0))
	win.blit(text, (text.get_rect().width / 2, text.get_rect().height / 2))
	pygame.display.update()

def getKey(keyName):
	ans = False
	for eve in pygame.event.get(): pass
	keyInput = pygame.key.get_pressed()
	myKey = getattr(pygame, "K_{}".format(keyName))
	if keyInput[myKey]:
		ans = True
	pygame.display.update()
	return ans
