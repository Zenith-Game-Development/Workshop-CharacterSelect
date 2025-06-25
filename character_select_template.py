import pygame
import random
from enum import Enum

# Global Constants:
IMAGE_NAME = "gemini-character-"
IMAGE_EXT = ".png"
WIDTH, HEIGHT = 700, 700
CAPTION = "Character Select"
NUM_CHARS = 4
# Constants for Drawing:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
LINE_WIDTH = 4
MARGIN = 32
PADDING = 16
NUM_CELLS = 20
GRID_SIZE = (WIDTH - MARGIN * 2) / NUM_CHARS
# Global Variables:
character_data = []
character_image = pygame.Surface((1, 1))


class Screen(Enum):
    """
    Represents the possible different screens: the start screen and character select screen.
    """



    # Task 1:

    # TODO: Create values for each screen we can display.


class GameManager:
    """
    The main class that handles running the program.
    """

    def __init__(self):

        # Initialize Pygame.
        pygame.init()
        # Add the name to the window.
        pygame.display.set_caption(CAPTION)
        # Initialize the screen and clock.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()



        # Task 2:

        # TODO: Define variable to represent whether the game is running or not, assign a default value.

        # TODO: Define a variable representing the current screen, assign a default value.

        global character_image
        # TODO: Initialize character_image value with the first character image.

        # Scale down to size.
        character_image = pygame.transform.scale(character_image, (WIDTH / 2, HEIGHT / 2))



        # Task 4 Cont.:

        # TODO: Call the load_data method after you finish writing it.



        # Task 5 Cont.:

        # TODO: Call the set_screen method after you finish writing it.



        # Task 8

        # TODO: Declare the character index and whether the character is selected.



        # Task 2 Cont.:

        # TODO: While the game is currently running, continue to update it.

        # TODO: Otherwise, quit the program.

    def load_data(self):
        """
        Generates the character data and saves it into the array.
        """



        # Task 4

        # TODO: For each character, load their image and randomly generate their stats.

            # Declare any needed local variables here.

            # Load up the character image and scale it.

            # Append to row.

            # Create random values 1 - 100 for each stat.
            # str, def, dex, int, cha

            # Add the row to the character data.

    def set_screen(self, new_screen):
        """
        Changes the screen to a new screen. If switching to the start screen, generate a new character to display randomly.
        Parameters:
            new_screen (Screen): The new screen we want to change to.
        """



        # Task 5:

        # TODO: Set the current screen to the new screen.

        # TODO: If we are showing the start screen, randomly select one of the character images to display.

        # Remove after you've added your implementation.
        pass


    def update(self):
        """Updates the program each frame."""

        # Get the user's input and draw the screen.
        self.get_input()
        self.draw()
        # Runs at 60 FPS.
        self.clock.tick(60)

    def get_input(self):
        """
        Processes the user's input and take actions accordingly.
        """

        # Process each input event.
        # Keep in mind that the get method clears the event queue, so you can use it multiple times.
        for event in pygame.event.get():
            # If the user closes the window, stop running.
            if event.type == pygame.QUIT:
                self.running = False



            # Task 7

            # TODO: If the user presses a key.

                # TODO: If the user is on the start screen.

                    # If the user presses escape on the start screen, stop running the game.

                    # If the user presses any other key, go to the character select screen.

                # TODO: If the user is on the character select screen.

                    # If the user presses the escape key.

                        # TODO: Task 7 - Go back to the start screen.




                        # TODO: Task 9 - If the user hasn't selected a character yet, go back to the start screen.

                        # TODO: Otherwise, deselect the currently selected character.

                    # TODO: Task 9 - If the user presses the left arrow key and they haven't selected a character,
                    # move to the left.


                    # TODO: If the user presses the right arrow key and they haven't selected a character,
                    # move to the right.


                    # TODO: If the user presses enter.

                        # If they haven't selected a character, select it.


        # Remove after you add your implementation.
        pass

    def draw(self):
        """
        Draws the screen, including the start screen and character select screen, accordingly.
        """



        # Task 3:

        # TODO: If we are drawing the start screen.

            # TODO: First, fill the screen with black to hide what was previously on the screen.

            # TODO: Draw the title.

            # Make the font.

            # Define the text you want to display.

            # Render the title.

            # draw it on the top middle of the screen.

            # TODO: Draw the prompt.

            # Follow the same steps as with the title to render the prompt.

            # TODO: Draw the character image.



        # Task 6:

        # TODO: If we are drawing the character select screen.

            # TODO: First, fill the screen with black to hide what was previously on the screen.

            # TODO: For each character draw their image and stats.

                # Get the character data.

                # Get the character's image and stats.



                # Task 6.1:

                # TODO: Determine the size of each image.

                # Resize the images so they fit on the screen.



                # Task 6.2:

                # TODO: Determine the position of each image.

                # Set the position of the images so they are roughly the same distance from one
                # another across the screen.

                # TODO: Draw the character's image.



                # Task 6.3:

                # TODO: Draw the stats of each character.

                # Define the stat names for rendering purposes.

                # Create the font.

                # Define the starting Y position.

                # TODO: For each stat:

                    # Define the text.

                    # Render the text.

                    # Determine the position.

                    # Draw on screen.



                # Task 8 Cont.:

                # TODO: If the index of this character matches the character index.

                    # TODO: If the character is not selected yet, draw a yellow box.

                    # TODO: Otherwise, draw a red box.



            # Task 6.4:

            # TODO: Define, render, and display the title text.

            # TODO: Define the instructions text:
            # - Left / Right Arrows
            # - Enter
            # Escape
            # What should each do?

            # Define the font.

            # TODO: For each instruction, render the instruction and draw on the screen.

        # TODO: Update the display!

        # Remove after you add your implementation.
        pass



# Task 2 Cont.:

# TODO: Create a game manager to begin the execution of the program!
