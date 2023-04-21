import pygame

def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((1100, 700))
    CLOCK = pygame.time.Clock()
    SCREEN.fill = (255, 255, 255)
    radius = 15
    x = 0
    y = 0
    MODE = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    MODE = 'red'
                elif event.key == pygame.K_g:
                    MODE = 'green'
                elif event.key == pygame.K_b:
                    MODE = 'blue'
            
            if event.type == pygame.K_z:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.K_x:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        SCREEN.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(SCREEN, i, points[i], points[i + 1], radius, MODE)
            i += 1
        
        pygame.display.flip()
        
        CLOCK.tick(60)

def drawLineBetween(SCREEN, index, start, end, width, color_MODE):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_MODE == 'blue':
        color = (c1, c1, c2)
    elif color_MODE == 'red':
        color = (c2, c1, c1)
    elif color_MODE == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(SCREEN, color, (x, y), width)

main()