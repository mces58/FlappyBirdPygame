import pygame

# Initialize the game
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the colors
BLACK = (0, 0, 0)

# Set up the fonts
font = pygame.font.Font(None, 36)

# Set up the text
text = font.render("Hello World!", True, BLACK)

# Set up the text position
text_rect = text.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)
    pygame.display.flip()
    
# Quit the game
pygame.quit()
