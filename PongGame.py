import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 5
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddles and ball
paddle1 = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

# Ball direction
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

# Score
score1, score2 = 0, 0
font = pygame.font.Font(None, 74)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.move_ip(0, PADDLE_SPEED)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.move_ip(0, PADDLE_SPEED)

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1

    # Ball out of bounds
    if ball.left <= 0:
        score2 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_dx = random.choice([BALL_SPEED_X, -BALL_SPEED_X])
        ball_dy = random.choice([BALL_SPEED_Y, -BALL_SPEED_Y])
    if ball.right >= WIDTH:
        score1 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_dx = random.choice([BALL_SPEED_X, -BALL_SPEED_X])
        ball_dy = random.choice([BALL_SPEED_Y, -BALL_SPEED_Y])

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    score_text1 = font.render(str(score1), True, WHITE)
    score_text2 = font.render(str(score2), True, WHITE)
    screen.blit(score_text1, (WIDTH//4, 20))
    screen.blit(score_text2, (WIDTH*3//4, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
s