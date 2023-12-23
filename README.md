# Pixel Runner
## Credits
The point of this project was to have an initial look at building games in python using the pygames library. I had little experience with python beforehand
and thought this project would be a good way to gain experience. It is based off a similar project by Clear Code's "The ultimate Introduction to Pygame" Where
he explained a lot of the basic processes going into making a game in python. I used some of his examples as a base for my project but added many extreme changes to
his project to make it my own, primarily in features, art design, and class and method structuring. 

The sound, art assets, and music were all taken from the OpenGameArt.org by Kenney.nl and Juhani Junkala are not my own. They are open source and free to use. The links to the assets are below.
link to the artwork: https://opengameart.org/content/platformer-art-complete-pack-often-updated
link to background music: https://opengameart.org/content/5-chiptunes-action

### Description
This is a simple running game where obstacles come from the right hand side of the screen towards the player. The player must jump over the obstacles, which vary in the direction they come from as well as collision size. The player gains increasing score the longer they survive. The score is based off the total time survived since the active game state starts. The game features various enemies which have different spawn weights, background music which continuously loops as long as the game is active, and a looping background image to provide a sense of speed to the player (who isn't actually moving outside of jumps). All of the sprites use multiple png image loading to act as if they are animated and have movement to them. The game state is the main game loop where the player can jump over obstacles and gain score. The game over screen is displayed when the player collides with an object and displays the score they achieved. The main menu is displayed when the game is first started and displays the controls and the title of the game. 

### Controls
The controls are incredibly simple. The player starts or continues the game with enter, and jumps over obstacles with space. No other inputs are needed.

### Design
One of the key differences in my design from the base is the abundance of functions and additional classes in order to allow greater control over changing any needed variables within the code for any existing or new features. I focused on making the code as modular as possible to allow for easy changes and additions. This made it much easier for me to make additions and drastic changes from the original base project as well as giving plenty of practice for making multiple functions and classes work together in a coherent manner. There is certainly plenty more room for improvement. But I feel this project served as a good introductory example to pygame.

## Files:
### audio
contains the background music for the game as well as the sound effects for jumping. The music is a looping track that plays continuously as long as the game is active. The sound effect is played when the player jumps.

### font
contains the font used for the all the text in the game. The font is a simple pixel font that is easy to read and fits the theme of the game.

### graphics
contains all the base images used in the game, ground.png and Sky.png were provided by Clear Code's "The ultimate Introduction to Pygame" and were used as a base for the game. The rest of the images were taken from OpenGameArt.org by Kenney.nl and Juhani Junkala. 

### Platformer Art Complete Pack 
Contains additional images for the game. Provided by OpenGameArt.org by Kenney.nl. The images are used for the player, enemies, and obstacles.

### Classes and functions used:
#### Classes:
Display - This class is used to create the display for the game. It is used to create the window and set the caption for the window. It also contains the method for updating the display and the method for closing the display. It is used in the main game loop to create the window and update the display.

Player - This class is used to create the player sprite. It contains the methods for drawing the player, updating the player with animations, and taking player input for jumping as well as applying gravity to make the player fall back down. It is used in the main game loop to create the player object and update the player object.

Obstacle - This class is used to create the obstacle Sprites that the player must jump over. It contains the methods for drawing the obstacles, updating the obstacles and features for applying "animations" and cleanup of sprites are included. It is used in the main game loop to create the obstacles and update the obstacles.

#### Functions:
collision_sprite_group():
This function is used to check for collisions between the player and the obstacles. It takes in the player and obstacle sprite groups and checks for collisions between the two. If a collision is detected, the function with change the game state false and set game over to true. It is used in the main game loop to check for collisions between the player and obstacles. As well as clearing the obstacles from the screen when the game is over to avoid extra collisions.

draw_background():
This function is used to draw the background image to the screen. It takes in the display and background image and draws the background image to the screen. It is used in the main game loop to draw the background image to the screen. it is where the backgrounds are looped to give the illusion of movement.

display_score():
This function is used to display the score to the screen. It takes in the score surface and the score and displays the score to the screen. It is used in the main game loop to display the score to the screen.

handle_start_screen():
Displays the initial start screen to the player to give basic instructions on the game. It is used in the main game loop to display the start screen when the game is first started.

handle_game_over_screen():
Displays the game over screen to the player when the game is over. It displays the score the player achieved and gives instructions on how to restart the game. It is used in the main game loop to display the game over screen when the game is over.

run_game():
Used to reset the game state and reset variables to their initial values. It is used in the main game loop to reset the game state and variables when the player restarts the game.

### Initial Variables
All initial variables not defined in a class are defined at the top of the main game loop after pygame is initialized. They are used to control various aspects throughout the functions and classes.