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
        # Set game over state to true
        global game_over
        game_over = True


# Function to display score to screen
def display_score():
    global score
    # get the current time in milliseconds
    pygame.time.get_ticks()
    # divide by 1000 to get total seconds
    score = (pygame.time.get_ticks() // 1000) - start_time
    # set score surface and rectangle to global variables for use in draw_all() function
    global score_surface, score_rect
    # display score surface and rectangle
    score_surface = default_font.render(f"Score: {score}", False, (64, 64, 64)).convert_alpha()
    score_rect = score_surface.get_rect(midleft=(3, 25))


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


# Function to display start screen
def handle_start_screen():
    display.screen.fill((90, 130, 155))
    # Initial Player Icon
    player_stand_start = pygame.image.load("graphics/Player/p3_stand.png").convert_alpha()
    # Scale player icon to double size
    player_stand_start = pygame.transform.scale2x(player_stand_start)
    # Set player icon to center of screen
    player_stand_start_rect = player_stand_start.get_rect(center=(400, 200))
    # Blit player icon to screen
    display.screen.blit(player_stand_start, player_stand_start_rect)
    # Instructions to start game
    start_game_surf = default_font.render("Welcome to the game", True, (60, 64, 60)).convert_alpha()
    start_game_rect = start_game_surf.get_rect(center=(400, 50))
    # Blit instructions to screen
    display.screen.blit(start_game_surf, start_game_rect)
    # Instructions to start game
    start_game_instructions_surf = default_font.render("Press Space to Continue", True, (60, 64, 60)).convert_alpha()
    # Set instructions to center of screen
    start_game_rect = start_game_instructions_surf.get_rect(center=(400, 340))
    # Blit instructions to screen
    display.screen.blit(start_game_instructions_surf, start_game_rect)


# Function to display continue screen
def handle_game_over_screen(score):
    display.screen.fill((90, 130, 155))
    # Initial Player Icon
    player_stand_start = pygame.image.load("graphics/Player/p3_stand.png").convert_alpha()
    # Scale player icon to double size
    player_stand_start = pygame.transform.scale2x(player_stand_start)
    # Set player icon to center of screen
    player_stand_start_rect = player_stand_start.get_rect(center=(400, 200))
    # Blit player icon to screen
    display.screen.blit(player_stand_start, player_stand_start_rect)
    # Game Over text
    game_over_surface = default_font.render("Game Over", False, (64, 64, 64)).convert_alpha()
    game_over_rect = game_over_surface.get_rect(center=(400, 56))
    # Blit game over text to screen
    display.screen.blit(game_over_surface, game_over_rect)
    display.screen.blit(game_over_surface, game_over_rect)
    # Instructions to start game
    start_game_instructions_surf = default_font.render("Press Space to Continue", True, (60, 64, 60)).convert_alpha()
    # Set instructions to center of screen
    start_game_rect = start_game_instructions_surf.get_rect(center=(400, 360))
    # Blit instructions to screen
    display.screen.blit(start_game_instructions_surf, start_game_rect)

    # Display achieved score
    score_text = default_font.render(f"Score: {score}", False, (64, 64, 64)).convert_alpha()
    score_rect = score_text.get_rect(center=(400, 320))
    display.screen.blit(score_text, score_rect)


# Function to run the game
def run_game():
    global game_state, score, player_gravity, start_time
    game_state = True
    score = 0
    player_gravity = 0
    start_time = pygame.time.get_ticks() // 1000


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
game_state = False
game_over = False
# Score variable
score = 0
# Track gravity
player_gravity = 0
# Start time since game started, continues to count even after game over
start_time = 0


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

# Start positions:
# Snail start position
snail_rect.x = 680
# Player start position
player_rect.midbottom = (100, 300)


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
        # Handle events for different game states
        if game_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        elif not game_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_game()  # Start the game
        elif game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run_game()  # Restart the game

    # Clear the screen
    display.screen.fill((90, 130, 155))

    # Handle different game states
    if game_state:
        # Run the game
        # Display score
        display_score()
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
    elif game_over:
        # Display game over screen
        handle_game_over_screen(score)
    else:
        # Display start screen
        handle_start_screen()

    # Update display
    pygame.display.update()
