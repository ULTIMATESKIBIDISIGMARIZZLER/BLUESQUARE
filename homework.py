import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("BLUESQUARE")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
rect_x, rect_y = WIDTH // 2, HEIGHT // 2
rect_width, rect_height = 50, 50
VEL = 5  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:  
        rect_x -= VEL
    if keys_pressed[pygame.K_RIGHT]:  
        rect_x += VEL
    if keys_pressed[pygame.K_UP]:  
        rect_y -= VEL
    if keys_pressed[pygame.K_DOWN]: 
        rect_y += VEL

    # Rendering
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

