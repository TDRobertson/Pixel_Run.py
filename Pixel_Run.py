import pygame
from sys import exit

# Class to create a screen area display with pre-defined color and title
class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.title = "Pixel Run"
        # Create screen object
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Set title of screen
        pygame.display.set_caption(self.title)
        # Set color of screen
        self.screen.fill((90, 130, 155))

# Function to draw all surfaces and images to the screen
def draw_all():
    # Display Backgrounds
    display.screen.blit(sky_background, (0, 0))
    display.screen.blit(ground_background, (0, 300))
    # Display font surface
    display.screen.blit(font_surface, (200, 100))
    # Display snail surface
    display.screen.blit(snail_surface, (snail_x_pos, snail_y_pos))

def move_obstacles():
    # Move snail obstacle to the left
    global snail_x_pos
    snail_x_pos -= 4
    # Reset snail obstacle to the right of the screen when it reaches the left edge
    if snail_x_pos <= -100:
        snail_x_pos = 800


# Initialize pygame
pygame.init()

# Create screen object
display = Display(800, 400)
# Create clock object
clock = pygame.time.Clock()
# Games font style
default_font = pygame.font.Font("font/Pixeltype.ttf", 60)


# Backgrounds:
sky_background = pygame.image.load("graphics/Sky.png").convert_alpha()
# display sky background
# display.screen.blit(sky_background, (0, 0))
# ground background
ground_background = pygame.image.load("graphics/ground.png").convert_alpha()
# display ground background
# display.screen.blit(ground_background, (0, 300))


# Surfaces:
# Create and then display them in the game loop
# test_surface = pygame.Surface((100, 200))
# test_surface.fill("red")
# test_surface2 = pygame.Surface((100, 200))
# test_surface2.fill("blue")
# Font surface
font_surface = default_font.render("My Game", False, (60, 64, 60)).convert_alpha()
# Snail surface
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()

# Obstacle Variables:
# Snail
snail_x_pos = 680; snail_y_pos = 260


# Game loop
while True:
    # Set frame rate to 60 fps
    clock.tick(60)

    # Event loop
    for event in pygame.event.get():
        # Check if user quits game window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw surfaces and images to screen
    draw_all()
    # Move obstacles
    move_obstacles()

    # Update display
    pygame.display.update()
