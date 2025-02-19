import pygame

pygame.init()

# Window settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Square")

# Player settings
player_size = 50
player_x, player_y = WIDTH//2, HEIGHT//2
speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Control speed of loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += speed

    screen.fill((0, 0, 0))  # Black background
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_size, player_size))  # Green square
    pygame.display.update()

pygame.quit()
