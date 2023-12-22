import pygame
from sys import exit
from random import randint
from random import choice


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


# Function to move obstacles using their x or y positions of the rectangle in the game loop
def move_obstacles():
    # Move snail obstacle to the left and reset if it reaches the left edge
    snail_rect.x -= 5
    if snail_rect.x <= -100:
        snail_rect.x = 800
    # Move fly obstacle to the left and reset if it reaches the left edge
    fly_rect.x -= 5
    if fly_rect.x <= -100:
        fly_rect.x = 800


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            # Move obstacle to the left
            obstacle_rect.x -= 5
            # Draw obstacle to screen
            if obstacle_rect.bottom == 300:
                display.screen.blit(snail_surface, obstacle_rect)
            elif obstacle_rect.bottom == 190:
                display.screen.blit(fly_surface, obstacle_rect)
            # Remove obstacle from list if it reaches the left edge
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


# Function to check for collisions between player and obstacles
def check_collision(player, obstacles):
    # Check for collisions between player and obstacles
    if obstacles:
        for obstacle_rect in obstacles:
            if player_rect.colliderect(obstacle_rect):
                # Reset player position
                player_rect.midbottom = (100, 300)
                # Set player gravity to 0
                global player_gravity
                player_gravity = 0
                # Set game state to false
                return False
                # Clear obstacles list


    return True
                # # Reset snail position
                # snail_rect.x = 680
                #
                # # Reset player position
                # player_rect.midbottom = (100, 300)
                # # Set game state to false
                # global game_state
                # game_state = False
                # # Set game over state to true
                # global game_over
                # game_over = True


# Player animation function
def player_animation():
    # Set player surface to global variable for use in draw_all() function
    global player_surface, player_walk_index
    # Check if player is touching the ground
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        # Animate player walking
        player_walk_index += 0.1
        if player_walk_index >= len(player_walk_list):
            player_walk_index = 0
        player_surface = player_walk_list[int(player_walk_index)]
    # Display player surface
    display.screen.blit(player_surface, player_rect)


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
    player_stand_start_rect = player_stand_start.get_rect(center=(400, 190))
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
# Sky background
sky_background = pygame.image.load("graphics/Sky.png").convert_alpha()
# ground background
ground_background = pygame.image.load("graphics/ground.png").convert_alpha()


# Surfaces and Rectangles:
# Create and then display them in the game loop using the draw_all() function
# Font surface
font_surface = default_font.render("Pixel Runner", False, (60, 64, 60)).convert_alpha()
font_rect = font_surface.get_rect(midbottom=(400, 50))
# Player Surface and rectangle
player_stand_surface = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk02.png").convert_alpha()
# player_rect = player_stand_surface.get_rect(midbottom=(100, 300))
# Player walking animation
player_walk_1 = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk02.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk04.png").convert_alpha()
player_walk_3 = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk05.png").convert_alpha()
# Player walk list
player_walk_list = [player_walk_1, player_walk_2, player_walk_3]
# Index for player walk list
player_walk_index = 0
# Player jump animation
player_jump = pygame.image.load("graphics/Player/p3_jump.png").convert_alpha()
# Player surface
player_surface = player_walk_list[player_walk_index]
# Player rectangle
player_rect = player_surface.get_rect(midbottom=(100, 300))

# Obstacle surfaces and rectangles
# Snail surface and rectangle
# Snail animations
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frame_list = [snail_frame_1, snail_frame_2]
# Snail index
snail_index = 0
# Snail surface
snail_surface = snail_frame_list[snail_index]
snail_rect = snail_surface.get_rect(midbottom=(680, 300))

# Fly surface and rectangle
# Fly animations
fly_frame_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
fly_frame_list = [fly_frame_1, fly_frame_2]
# Fly index
fly_index = 0
# Fly surface
fly_surface = fly_frame_list[fly_index]
fly_rect = fly_surface.get_rect(midbottom=(1000, 190))


# Obstacles list
obstacles_rect_list = []

# Start positions:
# Snail start position
snail_rect.x = 680
# Player start position
player_rect.midbottom = (100, 300)

# Timers:
# Obstacle_timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)
# Snail animation timer
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 495)
# Fly animation timer
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 330)

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
        # Check if user presses space bar to start game
        elif not game_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_game()  # Start the game
        # Check if user presses space bar to restart game
        elif game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run_game()  # Restart the game
        # Check if obstacle timer has been reached
        if event.type == obstacle_timer and game_state:
            # Choose random obstacle to add to list
            random_obstacle = choice(["snail", "fly"])
            # Add snail to obstacle list
            if random_obstacle == "snail":
                obstacles_rect_list.append(snail_surface.get_rect(midbottom=(randint(900, 1100), 300)))
            # Add fly to obstacle list
            if random_obstacle == "fly":
                obstacles_rect_list.append(fly_surface.get_rect(midbottom=(randint(900, 1100), 190)))
        # Check if animation timer has been reached
        if event.type == snail_animation_timer:
            # Animate snail
            if snail_index == 0:
                snail_index = 1
            else:
                snail_index = 0
            snail_surface = snail_frame_list[snail_index]
        if event.type == fly_animation_timer:
            # Animate fly
            if fly_index == 0:
                fly_index = 1
            else:
                fly_index = 0
            fly_surface = fly_frame_list[fly_index]

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
        # Player animation
        player_animation()
        # Move obstacles
        obstacles_rect_list = obstacle_movement(obstacles_rect_list)
        # Check for collisions
        game_state = check_collision(player_rect, obstacles_rect_list)

    elif game_over:
        # Display game over screen
        handle_game_over_screen(score)
        # Clear obstacles list
        obstacles_rect_list.clear()
    else:
        # Display start screen
        handle_start_screen()
        # Clear obstacles list
        obstacles_rect_list.clear()

    # Update display
    pygame.display.update()
