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
    display.screen.blit(font_surface, font_rect)
    # Display player rect
    display.screen.blit(player_surface, player_rect)
    # Display snail rect
    display.screen.blit(snail_surface, snail_rect)


# Function to move obstacles using their x or y positions of the rectangle in the game loop
def move_obstacles():
    # Move snail obstacle to the left and reset if it reaches the left edge
    snail_rect.x -= 4
    if snail_rect.x <= -100:
        snail_rect.x = 800

def check_collision():
    # Check if player collides with snail
    if player_rect.colliderect(snail_rect):
        # Reset snail position
        snail_rect.x = 800
        # Reset player position
        player_rect.midbottom = (100, 300)


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


# Surfaces and Rectangles:
# Create and then display them in the game loop using the draw_all() function
# Font surface
font_surface = default_font.render("Pixel Runner", False, (60, 64, 60)).convert_alpha()
font_rect = font_surface.get_rect(midbottom=(400, 50))
# Player Surface and rectangle
player_surface = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk02.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(100, 300))
# Snail surface and rectangle
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(680, 300))


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
    # Check for collisions
    check_collision()

    # Update display
    pygame.display.update()
