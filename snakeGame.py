import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
width, height = 600, 400

# Spaceship properties
spaceship_block = 10

# Initialize the game window
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Snake')

clock = pygame.time.Clock()

# Spaceship class
class Spaceship:
    def __init__(self):
        self.x = width / 2
        self.y = height / 2
        self.x_change = 0
        self.y_change = 0
        self.length = 1
        self.blocks = []

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

        # Update blocks
        head = [self.x, self.y]
        self.blocks.append(head)

        if len(self.blocks) > self.length:
            del self.blocks[0]

    def draw(self, surface):
        for block in self.blocks:
            pygame.draw.rect(surface, white, [block[0], block[1], spaceship_block, spaceship_block])

# Game Loop
def game_loop():
    game_over = False
    game_close = False

    spaceship = Spaceship()

    # Fuel
    fuel_x = round(random.randrange(0, width - spaceship_block) / 10.0) * 10.0
    fuel_y = round(random.randrange(0, height - spaceship_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_window.fill(black)
            font = pygame.font.SysFont(None, 35)
            message = font.render('Game Over! Press C-Continue or Q-Quit', True, red)
            game_window.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spaceship.x_change = -spaceship_block
                    spaceship.y_change = 0
                elif event.key == pygame.K_RIGHT:
                    spaceship.x_change = spaceship_block
                    spaceship.y_change = 0
                elif event.key == pygame.K_UP:
                    spaceship.y_change = -spaceship_block
                    spaceship.x_change = 0
                elif event.key == pygame.K_DOWN:
                    spaceship.y_change = spaceship_block
                    spaceship.x_change = 0

        if spaceship.x >= width or spaceship.x < 0 or spaceship.y >= height or spaceship.y < 0:
            game_close = True

        spaceship.move()
        game_window.fill(black)
        pygame.draw.rect(game_window, green, [fuel_x, fuel_y, spaceship_block, spaceship_block])
        spaceship.draw(game_window)

        pygame.display.update()

        # Check if spaceship gets the fuel
        if spaceship.x == fuel_x and spaceship.y == fuel_y:
            fuel_x = round(random.randrange(0, width - spaceship_block) / 10.0) * 10.0
            fuel_y = round(random.randrange(0, height - spaceship_block) / 10.0) * 10.0
            spaceship.length += 1

        clock.tick(15)

    pygame.quit()
    quit()

game_loop()
