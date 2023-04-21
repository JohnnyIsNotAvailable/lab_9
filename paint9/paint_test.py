import pygame 
class CONSTANTS:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

pygame.init()
SCREEN = pygame.display.set_mode((1100, 700))
CLOCK = pygame.time.Clock()

MODE = 'blue'

while True:
        
    pressed = pygame.key.get_pressed()
        
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

            if event.key == pygame.K_r:
                MODE = 'red'
            elif event.key == pygame.K_g:
                MODE = 'green'
            elif event.key == pygame.K_b:
                MODE = 'blue'

    if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)

    if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
    

    pygame.display.flip()
    CLOCK.tick(60)