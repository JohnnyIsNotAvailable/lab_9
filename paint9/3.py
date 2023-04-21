import pygame
BLUE = (0 , 0 , 255)
screen = pygame.display.set_mode( (500, 500) )

def drawCircle( screen, x, y ):
  pygame.draw.circle( screen, BLUE, ( x, y ), 5 )

while True: 
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      isPressed = True
    elif event.type == pygame.MOUSEBUTTONUP:
      isPressed = False
    elif event.type == pygame.MOUSEMOTION and isPressed == True:         
      ( x, y ) = pygame.mouse.get_pos()       # returns the position of mouse cursor
      drawCircle( screen, x, y )
   pygame.display.flip()
pygame.quit()