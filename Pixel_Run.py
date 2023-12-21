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
    # Display score surface
    display.screen.blit(score_surface, score_rect)
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


# Function to check for collisions between player and obstacles
def check_collision():
    # Check if player collides with snail
    if player_rect.colliderect(snail_rect):
        # Reset snail position
        snail_rect.x = 800
        # Reset player position
        player_rect.midbottom = (100, 300)
        # Set game state to false
        global game_state
        game_state = False


# Function to reset game
def reset_game():
    # Reset snail position
    snail_rect.x = 680
    # Reset player position
    player_rect.midbottom = (100, 300)
    # Set game state to false if user presses space bar
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            global game_state
            game_state = True


# def keyboard_input():
#     # Check if user presses space bar
#     if event.type == pygame.KEYDOWN:
#         print("Key pressed")
#         # Check if user presses space bar
#         if event.key == pygame.K_SPACE:
#             # Check if player is on the ground
#             global player_gravity
#             player_gravity = -20
#         # Check if user presses up arrow key
#         if event.key == pygame.K_UP:
#             print("Up arrow pressed")
#         # Check if user presses down arrow key
#         if event.key == pygame.K_DOWN:
#             print("Down arrow pressed")


# def apply_gravity():
#     # Check if player is in the air
#     if player_rect.bottom < 300:
#         player_rect.y += 1


# Initialize pygame
pygame.init()

# Create screen object
display = Display(800, 400)
# Create clock object
clock = pygame.time.Clock()
# Games font style
default_font = pygame.font.Font("font/Pixeltype.ttf", 60)

# Variables:
game_state = True
# Score variable
score = 0
# Track gravity
player_gravity = 0


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
# Score surface
score_surface = default_font.render(f"Score: {score}", False, (64, 64, 64)).convert_alpha()
score_rect = score_surface.get_rect(midleft=(3, 25))
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
        # If game state is true
        if game_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        # If game state is false
        if not game_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset snail position
                    snail_rect.x = 680
                    # Reset player position
                    player_rect.midbottom = (100, 300)
                    # Set game state to true
                    game_state = True


    # If game state is true then run game
    if game_state:
        # Apply gravity to player
        player_gravity += 1
        player_rect.y += player_gravity
        # Check if player is touching the ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        # Draw surfaces and images to screen
        draw_all()
        # Move obstacles
        move_obstacles()
        # Check for collisions
        check_collision()

    if not game_state:
        # Display game over surface
        display.screen.fill((90, 130, 155))
        game_over_surface = default_font.render("Game Over", False, (64, 64, 64)).convert_alpha()
        game_over_rect = game_over_surface.get_rect(center=(400, 200))
        display.screen.blit(game_over_surface, game_over_rect)


    # # Player gravity and movement
    # player_gravity += 1
    # player_rect.y += player_gravity
    # # Check if player is touching the ground
    # if player_rect.bottom >= 300:
    #     player_rect.bottom = 300
    #
    # # Draw surfaces and images to screen
    # draw_all()
    # # Move obstacles
    # move_obstacles()
    # # Check for collisions
    # check_collision()

    # Update display
    pygame.display.update()
