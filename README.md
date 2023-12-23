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