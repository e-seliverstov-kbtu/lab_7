import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False
is_blue = True
x = 25
y = 25

clock = pygame.time.Clock()
color = (255, 0 , 0)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    y -= 20
                    if y > 275:
                        y = 275
                    elif y < 25:
                        y = 25
                    screen.fill((0, 0, 0))
                    pygame.draw.circle(screen, color, (x, y), 25)
                    pygame.display.flip()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    y += 20
                    if y > 275:
                        y = 275
                    elif y < 25:
                        y = 25
                    screen.fill((0, 0, 0))
                    pygame.draw.circle(screen, color, (x, y), 25)
                    pygame.display.flip()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    x -= 20
                    if x > 275:
                        x = 275
                    elif x < 25:
                        x = 25
                    screen.fill((0, 0, 0))
                    pygame.draw.circle(screen, color, (x, y), 25)
                    pygame.display.flip()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    x += 20
                    if x > 275:
                        x = 275
                    elif x < 25:
                        x = 25
                    screen.fill((0, 0, 0))
                    pygame.draw.circle(screen, color, (x, y), 25)
                    pygame.display.flip()
            
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()



pygame.quit()
sys.exit()

