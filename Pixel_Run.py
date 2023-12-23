import pygame
from sys import exit
from random import randint
from random import choices


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


# Player Sprite Class (inherits from pygame.sprite.Sprite) to create player sprite group
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Player walking animation
        self.player_walk_1 = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk02.png").convert_alpha()
        self.player_walk_2 = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk04.png").convert_alpha()
        self.player_walk_3 = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk05.png").convert_alpha()
        # Player walk list
        self.player_walk_list = [self.player_walk_1, self.player_walk_2, self.player_walk_3]
        # Index for player walk list
        self.player_walk_index = 0
        # Player jump animation
        self.player_jump = pygame.image.load("graphics/Player/p3_jump.png").convert_alpha()
        # Player Surface and rectangle
        self.image = self.player_walk_list[self.player_walk_index]
        self.rect = self.image.get_rect(midbottom=(100, 300))
        # Player gravity variable
        self.player_gravity = 0
        # Player Jump Sound
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.08)

    # Player animation function to animate player sprite group
    def player_animation(self):
        # Check if player is touching the ground
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            # Animate player walking
            self.player_walk_index += 0.1
            if self.player_walk_index >= len(self.player_walk_list):
                self.player_walk_index = 0
            self.image = self.player_walk_list[int(self.player_walk_index)]

    # Player input function to check for user input
    def player_input(self):
        keys = pygame.key.get_pressed()
        # Check that game state is true
        if game_state:
            if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                self.player_gravity = -12
                # Play jump sound when player jumps
                self.jump_sound.play()

    # Function to apply gravity to player and check if player is touching the ground
    def apply_gravity(self):
        self.player_gravity += 0.5
        self.rect.y += self.player_gravity
        # Check if player is touching the ground
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    # Update player sprite group ran in game loop
    def update(self):
        # Run all player methods
        self.player_input()
        self.apply_gravity()
        self.player_animation()

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type  # Store the type of obstacle
        self.animation_index = 0  # Animation index for both snail and fly
        self.image = None
        self.rect = None
        self.init_obstacle()
        self.fly_direction = 1  # Direction of flying units

    def init_obstacle(self):
        if self.type == "snail":
            # Snail animations
            self.image = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            self.animation_frames = [self.image, pygame.image.load("graphics/snail/snail2.png").convert_alpha()]
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 300))
        elif self.type == "fly":
            # Fly animations
            self.image = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            self.animation_frames = [self.image, pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()]
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 190))
        # Add more types of obstacles here as needed
        elif self.type == "slime":
            # Slime animations
            self.image = pygame.image.load("graphics/Enemies/slimeWalk2.png").convert_alpha()
            self.animation_frames = [self.image, pygame.image.load("graphics/Enemies/slimeWalk1.png").convert_alpha()]
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 300))
        elif self.type =="flyfly":
            # Fly animations
            self.image = pygame.image.load("graphics/Enemies/flyFly1.png").convert_alpha()
            self.animation_frames = [self.image, pygame.image.load("graphics/Enemies/flyFly2.png").convert_alpha()]
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 50))
        elif self.type == "Bee":
            # Bee animations
            self.image = pygame.image.load("Platformer Art Complete Pack/Extra animations and enemies/Enemy sprites/bee.png").convert_alpha()
            self.animation_frames = [self.image, pygame.image.load("Platformer Art Complete Pack/Extra animations and enemies/Enemy sprites/bee_fly.png").convert_alpha()]
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 80))

    def obstacle_animation(self):
        # Animate the obstacles
        # Check if obstacle is a snail
        if self.type == "snail":
            # Animate snail
            self.animation_index += 0.04
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]
        # Check if obstacle is a fly
        elif self.type == "fly":
            # Animate Fly
            self.animation_index += 0.1
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]
        # Animate slime
        elif self.type == "slime":
            # Animate slime
            self.animation_index += 0.08
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]
        elif self.type == "flyfly":
            # Animate Fly2
            self.animation_index += 0.08
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]
        elif self.type == "Bee":
            # Animate Bee
            self.animation_index += 0.08
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]

        # For any other types of obstacles
        # Animate the obstacles
        else:
            self.animation_index += 0.1
            if self.animation_index >= len(self.animation_frames):
                self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]

    def remove(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.obstacle_animation()
        # If obstacle is flyfly, make it fly up and down based on a random y range
        if self.type == "flyfly":
            self.rect.x -= 6
            self.rect.y += 2
            if self.rect.bottom >= randint(220, 310):
                self.rect.y -= 2
        # If obstacle is a bee, make it continuously fly up and down
        elif self.type == "Bee":
            self.rect.x -= 6
            self.rect.y += 1.4 * self.fly_direction

            # Change fly direction when it reaches the top or bottom values
            if self.rect.bottom >= randint(170, 205):
                self.fly_direction = -1  # Change direction to up
            elif self.rect.bottom <= randint(35, 55):
                self.fly_direction = 1  # Change direction to down

        # For any other types of obstacles
        else:
            self.rect.x -= 6

        self.remove()


# Collision function for sprite groups (player and obstacle)
def collision_sprite_group():
    # Check if player sprite group collides with obstacle sprite group (player group must be single to work)
    if pygame.sprite.spritecollide(player_group.sprite, obstacle_group, False):  # True removes the obstacle from group
        # Remove obstacle sprites from the screen
        obstacle_group.empty()
        # Set game state to false
        global game_state, game_over
        game_state = False
        game_over = True
        # Reset player position to initial position
        global player_gravity
        player_group.sprite.rect.midbottom = (100, 300)
        player_gravity = 0


# Function to draw all surfaces to the screen
def draw_background():
    # Display Backgrounds
    display.screen.blit(sky_background, (0, 0))
    display.screen.blit(ground_background, (0, 300))
    # Draw two copies of the sky background to create a continuous scrolling effect
    display.screen.blit(sky_background, (sky_x_pos, 0))
    display.screen.blit(sky_background, (sky_x_pos + sky_background.get_width(), 0))
    # Draw two copies of the ground background to create a continuous scrolling effect
    display.screen.blit(ground_background, (ground_x_pos, 300))
    display.screen.blit(ground_background, (ground_x_pos + ground_background.get_width(), 300))
    # Display font surface
    display.screen.blit(font_surface, font_rect)
    # Display score surface
    display.screen.blit(score_surface, score_rect)

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
    score_surface = score_font.render(f"Score: {score}", False, (64, 64, 64)).convert_alpha()
    score_rect = score_surface.get_rect(midleft=(3, 25))


# Function to display start screen before game starts
def handle_start_screen():
    display.screen.fill((90, 130, 155))
    # Initial Player Icon
    player_stand_start = pygame.image.load("graphics/Player/p3_front.png").convert_alpha()
    # Scale player icon to double size
    player_stand_start = pygame.transform.scale2x(player_stand_start)
    # Set player icon to center of screen
    player_stand_start_rect = player_stand_start.get_rect(center=(400, 190))
    # Blit player icon to screen
    display.screen.blit(player_stand_start, player_stand_start_rect)
    # Instructions to start game
    start_game_surf = default_font.render("Welcome to the game", True, (60, 64, 60)).convert_alpha()
    start_game_rect = start_game_surf.get_rect(center=(400, 50))
    # Blit instructions to screen
    display.screen.blit(start_game_surf, start_game_rect)
    # Instructions to start game
    start_game_instructions_surf = default_font.render("Press Enter to Start", True, (60, 64, 60)).convert_alpha()
    # Set instructions to center of screen
    start_game_rect = start_game_instructions_surf.get_rect(center=(400, 315))
    # Blit instructions to screen
    display.screen.blit(start_game_instructions_surf, start_game_rect)
    # Instructions on how to play
    instructions_surf = default_font.render("Press Space Bar to Jump Over Enemies", True, (60, 64, 60)).convert_alpha()
    # Set instructions to center of screen
    instructions_rect = instructions_surf.get_rect(center=(400, 360))
    # Blit instructions to screen
    display.screen.blit(instructions_surf, instructions_rect)


# Function to display continue screen after game over
def handle_game_over_screen(score):
    display.screen.fill((90, 130, 155))
    # Initial Player Icon
    player_stand_start = pygame.image.load("graphics/Player/p3_duck.png").convert_alpha()
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
    start_game_instructions_surf = default_font.render("Press Enter to Continue", True, (60, 64, 60)).convert_alpha()
    # Set instructions to center of screen
    start_game_rect = start_game_instructions_surf.get_rect(center=(400, 360))
    # Blit instructions to screen
    display.screen.blit(start_game_instructions_surf, start_game_rect)

    # Display achieved score
    score_text = default_font.render(f"Score: {score}", False, (64, 64, 64)).convert_alpha()
    score_rect = score_text.get_rect(center=(400, 320))
    display.screen.blit(score_text, score_rect)


# Function to run the game and reset all variables to their initial values
def run_game():
    global game_state, score, player_gravity, start_time
    game_state = True
    # Reset all variables to their initial values
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
# Score and title font
score_font = pygame.font.Font("font/Pixeltype.ttf", 45)

# Variables:
game_state = False
game_over = False

# Background Music (looped) and volume control
background_music = pygame.mixer.music.load("audio/music.wav")
# Set the volume
pygame.mixer.music.set_volume(0.1)
# Play the background music in a loop and fade in over 3 seconds
pygame.mixer.music.play(-1, 0.0, 3000)


# Score variable
score = 0
# Track gravity
player_gravity = 0
# Start time since game started, continues to count even after game over
start_time = 0


# Player sprite group
player_group = pygame.sprite.GroupSingle()
player_group.add(Player())
# Obstacle sprite group
obstacle_group = pygame.sprite.Group()


# Backgrounds:
# Sky background
sky_background = pygame.image.load("graphics/Sky.png").convert_alpha()
# Sly background x position
sky_x_pos = 0
# ground background
ground_background = pygame.image.load("graphics/ground.png").convert_alpha()
# ground background x position
ground_x_pos = 0


# Surfaces and Rectangles:
# Create and then display them in the game loop using the draw_all() function
# Font surface
font_surface = score_font.render("Pixel Runner", False, (60, 64, 60)).convert_alpha()
font_rect = font_surface.get_rect(midbottom=(400, 40))
# Player Surface and rectangle
player_stand_surface = pygame.image.load("graphics/Player/p3_walk/PNG/p3_walk02.png").convert_alpha()


# Timers:
# Obstacle_timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

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

        # Check if user presses space bar to start game
        elif not game_state:
            if event.type == pygame.KEYDOWN:
                # Check if user presses enter to start game
                if event.key == pygame.K_RETURN:
                    run_game()  # Start the game

        # Check if user presses space bar to restart game
        elif game_over:
            if event.type == pygame.KEYDOWN:
                # Check if user presses enter to restart game
                if event.key == pygame.K_RETURN:
                    run_game()  # Restart the game

        # Check if obstacle timer has been reached
        if event.type == obstacle_timer and game_state:
            # Choose random obstacle to add to list using obstacle group
            # Define obstacle types and their corresponding probabilities
            obstacle_types = ["snail", "fly", "slime", "flyfly", "Bee"]
            probabilities = [0.3, 0.2, 0.15, 0.1, 0.15]  # Adjust these probabilities as needed
            # Randomly choose the type of obstacle based on probabilities
            obstacle_type = choices(obstacle_types, probabilities, k=1)[0]
            # Add the selected obstacle to the obstacle group
            obstacle_group.add(Obstacle(obstacle_type))

    # Sky background movement
    sky_x_pos -= 0.5
    # Check if sky background has reached the end of the screen
    if sky_x_pos <= -sky_background.get_width():
        sky_x_pos = 0

    # Ground background movement
    ground_x_pos -= 4
    # Check if ground background has reached the end of the screen
    if ground_x_pos <= -ground_background.get_width():
        ground_x_pos = 0


    # Clear the screen
    display.screen.fill((90, 130, 155))



    # Handle different game states
    if game_state:
        # Display score
        display_score()
        # Draw backgrounds and surfaces
        draw_background()
        # Player draw group method
        player_group.draw(display.screen)
        # Update player group
        player_group.update()
        # Obstacle draw group method
        obstacle_group.draw(display.screen)
        # Update obstacle group
        obstacle_group.update()
        # Collision function for sprite groups
        collision_sprite_group()

    elif game_over:
        # Display game over screen if game state is false
        handle_game_over_screen(score)

    else:
        # Display start screen
        handle_start_screen()

    # Update display
    pygame.display.update()
