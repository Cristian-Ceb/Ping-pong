import pygame
pygame.init()

# const
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
ROCKET_IMG = 'rocket.png'
BALL_IMG = 'ball.png'
BG_COLOR = 'background.png'
# const

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Пинг понг')
window.fill(BG_COLOR)
colck = pygame.time.Clock()

game_status = 'game'
while game_status != 'off':
    window.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = 'off'

    clock.tick(60)
    pygame.display.update()