import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gradient Circle')

# Define colors
outer_color = (0, 0, 0)
inner_color = (255, 255, 255)
gradient_color = (0, 0, 0, 0)  # Transparent color for the gradient

# Set the radius and position of the circle
radius = 100
circle_pos = (width // 2, height // 2)

# Create a surface for the gradient
gradient_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
for i in range(radius * 2):
    alpha = max(int(255 * (1 - 1.5*i / (radius * 2))),0)
    print(alpha)
    pygame.draw.circle(gradient_surface, (gradient_color[0], gradient_color[1], gradient_color[2], alpha), (radius, radius), radius - i)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Create the circle
    circle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(circle_surface, inner_color, (radius, radius), radius)
    circle_surface.blit(gradient_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    # Blit the circle onto the screen
    screen.blit(circle_surface, (circle_pos[0] - radius, circle_pos[1] - radius))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()