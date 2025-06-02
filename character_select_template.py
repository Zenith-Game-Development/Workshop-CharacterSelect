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

    # Create values for each screen we can display.


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

        # Task 2.1:

        # Define variables to represent whether the game is running or not, assign a default value.


        # Task 5:

        # Generate the characters' data.
        # For each character, load their image and randomly generate their stats.

            # Declare any needed local variables here.

            # Load up the character image and add to the character data.

            # Create random values 1 - 100 for each stat.
            # str, def, dex, int, cha

            # Add the data to the character data.

        # The player hasn't selected a character yet...
        # Need variables to keep track of whether a character has been selected and which one is currently being
        # hovered over.

        # Task 2.3:

        # Start on the start screen.

        # While the game is currently running, continue to update it.

        # Otherwise, quit the program.


    def set_screen(self, new_screen):
        """
        Changes the screen to a new screen. If switching to the start screen, generate a new character to display randomly.
        Parameters:
            new_screen (Screen): The new screen we want to change to.
        """

        # Task 2.2:

        # Set the current screen to the new screen.

        # If we are showing the start screen, randomly select one of the character images to display.

        # Remove after you've added your implementation.
        pass


    def update(self):
        """Updates the program each frame."""

        # Task 4:

        # Get the user's input and draw the screen.

        # Runs at 60 FPS.
        self.clock.tick(60)

    def get_input(self):
        """
        Processes the user's input and take actions accordingly.
        """

        # Task 3:

        # Process each input event.
        # Keep in mind that the get method clears the event queue, so you can use it multiple times.

            # If the user closes the window, stop running.


            # If the user presses a key.


                # If the user is on the start screen.


                    # If the user presses escape on the start screen, stop running the game.

                    # If the user presses any other key, go to the character select screen.
        w

                # Task 5:

                # If the user is on the character select screen.


                    # If the user presses the escape key.

                        # If the user hasn't selected a character yet, go back to the start screen.

                        # Otherwise, deselect the currently selected character.

                    # If the user presses the left arrow key and they haven't selected a character,
                    # move to the left.


                    # If the user presses the right arrow key and they haven't selected a character,
                    # move to the right.


                    # If the user presses enter.

                        # If they haven't selected a character, select it.

                        # Otherwise, continue to the next screen.
                        #else:
                        #    pass  # TODO: Go to next screen.

        # Remove after you add your implementation.
        pass

    def draw(self):
        """
        Draws the screen, including the start screen and character select screen, accordingly.
        """

        # Task 3:

        # If we are drawing the start screen.

            # Make a font for the title and prompt.

            # Define the text you want to display


            # First, fill the screen with black to hide what was previously on the screen.

            # Render the title and draw it on the top middle of the screen.

            # Render the prompt and draw it on the bottom middle of the screen.

            # Draw the random character image.

        # Task 5:

        # If we are drawing the character select screen.

            # Define the title and instruction fonts.

            # Define the title we want to display.

            # Define a list of control instructions:
            # - Left / Right Arrows
            # - Enter
            # Escape
            # What should each do?

            # First, fill the screen with black to hide what was previously on the screen.

            # Render the title and draw it on the top middle of the screen.

            # For each instruction, render the instruction and draw on the screen.

            # For each character draw their image and stats.

                # Get the character data.

                # Get the character's image and stats.

                # Define the stat names for rendering purposes.

                # Resize the images so they fit on the screen.

                # Set the position of the images so they are roughly the same distance from one
                # another across the screen.

                # Draw the character's image.

                # Draw the selection box if needed.

                    # Define the rect's shape.

                    # If the character is not selected yet, draw a yellow box.

                    # Otherwise draw a red box.

                # Draw the stats.
                # Define the starting position and font of the stats.

                # For each stat, render and display the text on screen.

        # Update the display!

        # Remove after you add your implementation.
        pass

# Task 1:

# Create a game manager to begin the execution of the program!
