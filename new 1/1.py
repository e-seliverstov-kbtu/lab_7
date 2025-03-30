import pygame
import sys
from datetime import datetime



pygame.init()
clock = pygame.time.Clock()


screen_width, screen_height = 300, 300
screen = pygame.display.set_mode((screen_width, screen_height))


image = pygame.image.load("mickeyclock.png")

image = pygame.transform.scale(image, (screen_width, screen_height))

arrow = pygame.image.load("second.png")
arrow = pygame.transform.scale(arrow, (40, 100))
arrow_minute = pygame.image.load("minute.png")
arrow_minute = pygame.transform.scale(arrow_minute, (40, 60))


def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect


def rot_side(image, angle, x, y):
    pivot = pygame.math.Vector2(image.get_width() // 2, image.get_height())
    image_center = pygame.math.Vector2(image.get_rect().center)
    offset = pivot - image_center
    rotated_offset = offset.rotate(-angle)
    new_center = pygame.math.Vector2(x, y) - rotated_offset
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=new_center)
    
    return rotated_image, new_rect


running = True
while running:
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(image, (0, 0))
    
    rotated_image, new_rect = rot_side(arrow, -(seconds*6), 150, 150)
    screen.blit(rotated_image, new_rect)

    rotated_image, new_rect = rot_side(arrow_minute, -(minutes*6), 150, 150)
    screen.blit(rotated_image, new_rect)

    
    pygame.display.flip()
    clock.tick(10)


pygame.quit()
sys.exit()
