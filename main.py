import pygame

print('Setup Star')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup Finish')

print('Loop Start')
while True:
 #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #CloseWindow
            quit() #end game
