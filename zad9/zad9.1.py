import pygame
import sys
import random

WIDTH, HEIGHT = 1000, 800
SNOWFLAKE_SIZE = 10
SNOWFLAKE_SPEED = 3
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class SnowFlake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = random.randint(0, WIDTH - SNOWFLAKE_SIZE)
        self.y = 0
        self.shape = random.randint(0, 2)

    def move(self):
        self.y += SNOWFLAKE_SPEED

    def draw(self):
        if self.shape == 0:
            pygame.draw.circle(screen, WHITE, (self.x, self.y), SNOWFLAKE_SIZE)
        elif self.shape == 1:
            pygame.draw.polygon(
                screen,
                WHITE,
                [
                    (self.x, self.y - SNOWFLAKE_SIZE),
                    (self.x + SNOWFLAKE_SIZE // 2, self.y - SNOWFLAKE_SIZE // 2),
                    (self.x + SNOWFLAKE_SIZE, self.y),
                    (self.x + SNOWFLAKE_SIZE // 2, self.y + SNOWFLAKE_SIZE // 2),
                    (self.x, self.y + SNOWFLAKE_SIZE),
                    (self.x - SNOWFLAKE_SIZE // 2, self.y + SNOWFLAKE_SIZE // 2),
                    (self.x - SNOWFLAKE_SIZE, self.y),
                    (self.x - SNOWFLAKE_SIZE // 2, self.y - SNOWFLAKE_SIZE // 2),
                ]
            )
        else:
            pygame.draw.polygon(
                screen,
                WHITE,
                [
                    (self.x, self.y - SNOWFLAKE_SIZE * 2),
                    (self.x - SNOWFLAKE_SIZE, self.y + SNOWFLAKE_SIZE),
                    (self.x + SNOWFLAKE_SIZE, self.y + SNOWFLAKE_SIZE),
                ]
            )
            pygame.draw.polygon(
                screen,
                WHITE,
                [
                    (self.x, self.y + SNOWFLAKE_SIZE * 2),
                    (self.x - SNOWFLAKE_SIZE, self.y - SNOWFLAKE_SIZE),
                    (self.x + SNOWFLAKE_SIZE, self.y - SNOWFLAKE_SIZE),
                ]
            )

    def is_clicked(self, pos):
        return (self.x - SNOWFLAKE_SIZE < pos[0] < self.x + SNOWFLAKE_SIZE) and (
            self.y - SNOWFLAKE_SIZE < pos[1] < self.y + SNOWFLAKE_SIZE
        )

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Padający śnieg')
clock = pygame.time.Clock()

snowflakes = []
score = 0

while True:
    screen.fill(BLUE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            pygame.quit()  
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for snowflake in snowflakes[:]:
                if snowflake.is_clicked(pos):
                    snowflakes.remove(snowflake)
                    score += 1

    if random.randint(1, 20) == 1:
        snowflakes.append(SnowFlake())

    for snowflake in snowflakes[:]:
        snowflake.move()
        snowflake.draw()

        if snowflake.y > HEIGHT:
            pygame.quit()
            sys.exit(0)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)
