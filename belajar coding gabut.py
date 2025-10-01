import pygame
import random
import sys

# Init pygame
pygame.init()

# Setup layar
WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird by Bro!")

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 155, 255)
GREEN = (0, 200, 0)

# Fonts
FONT = pygame.font.SysFont("comicsans", 40)

# Game Variables
gravity = 0.5
bird_movement = 0
score = 0

# Load gambar (bentuk sederhana aja)
BIRD = pygame.Rect(100, 300, 30, 30)
PIPES = []

pipe_width = 70
pipe_gap = 180
pipe_speed = 3
clock = pygame.time.Clock()

# Fungsi bikin pipa
def create_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap)
    return top_pipe, bottom_pipe

# Tambah pipa awal
PIPES.extend(create_pipe())

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    WIN.fill(BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_movement = -10  # loncat

    # Gerakan burung
    bird_movement += gravity
    BIRD.y += int(bird_movement)

    # Gambar burung
    pygame.draw.rect(WIN, WHITE, BIRD)

    # Gerakan dan gambar pipa
    for pipe in PIPES:
        pipe.x -= pipe_speed
        pygame.draw.rect(WIN, GREEN, pipe)

    # Tambah pipa baru
    if PIPES[0].x < -pipe_width:
        PIPES.pop(0)
        PIPES.pop(0)
        PIPES.extend(create_pipe())
        score += 1

    # Cek tabrakan
    for pipe in PIPES:
        if BIRD.colliderect(pipe):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Batas bawah / atas
    if BIRD.y > HEIGHT or BIRD.y < 0:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Tampilkan skor
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
