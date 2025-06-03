import pygame
import random
from enum import Enum

# Global Constants:
IMAGE_NAME = "gemini-character-" # gemini-character-1.png
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
# Global Variables:
character_data = []
character_image = pygame.Surface((1, 1))

class Screen(Enum):
    """
    Represents the possible different screens: the start screen and character select screen.
    """

    # Task 1:

    # Create values for each screen we can display.
    START = 0
    SELECT = 1


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

        print(pygame.font.get_fonts())

        # Task 2.1:

        # Define variables to represent whether the game is running or not, assign a default value.
        self.running = True

        # Task 5:

        # Generate the characters' data.
        # For each character, load their image and randomly generate their stats.
        for i in range(NUM_CHARS):
            # Declare any needed local variables here.
            row = []
            # Load up the character image and add to the character data.
            image = pygame.image.load(IMAGE_NAME + str(i) + IMAGE_EXT)
            image = pygame.transform.scale(image, (WIDTH / 2, HEIGHT / 2))
            row.append(image)
            # Create random values 1 - 100 for each stat.
            # str, def, dex, int, cha
            for j in range(5):
                row.append(random.randint(1, 100))
            # Add the data to the character data.
            character_data.append(row)

        # The player hasn't selected a character yet...
        # Need variables to keep track of whether a character has been selected and which one is currently being
        # hovered over.
        self.is_selected = False
        self.character_index = 0

        # Task 2.3:

        # Start on the start screen.
        self.set_screen(Screen.START)

        # While the game is currently running, continue to update it.
        while self.running:
            self.update()
        # Otherwise, quit the program.
        pygame.quit()


    def set_screen(self, new_screen):
        """
        Changes the screen to a new screen. If switching to the start screen, generate a new character to display randomly.
        Parameters:
            new_screen (Screen): The new screen we want to change to.
        """

        # Task 2.2:

        global character_image
        # Set the current screen to the new screen.
        self.current_screen = new_screen
        # If we are showing the start screen, randomly select one of the character images to display.
        index = random.randint(0, NUM_CHARS - 1)
        character_image = character_data[index][0]



    def update(self):
        """Updates the program each frame."""

        # Task 4:

        # Get the user's input and draw the screen.
        self.get_input()
        self.draw()
        # Runs at 60 FPS.
        self.clock.tick(60)

    def get_input(self):
        """
        Processes the user's input and take actions accordingly.
        """

        # Task 3:

        # Process each input event.
        # Keep in mind that the get method clears the event queue, so you can use it multiple times.
        for event in pygame.event.get():
            # If the user closes the window, stop running.
            if event.type == pygame.QUIT:
                self.running = False

            # If the user presses a key.
            if event.type == pygame.KEYDOWN:
                # If the user is on the start screen.
                if self.current_screen == Screen.START:
                    # If the user presses escape on the start screen, stop running the game.
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    # If the user presses any other key, go to the character select screen.
                    else:
                        self.set_screen(Screen.SELECT)

                # Task 5:
                # If the user is on the character select screen.
                if self.current_screen == Screen.SELECT:
                    # If the user presses the escape key.
                    if event.key == pygame.K_ESCAPE:
                        # If the user hasn't selected a character yet, go back to the start screen.
                        if not self.is_selected:
                            self.set_screen(Screen.START)
                        # Otherwise, deselect the currently selected character.
                        else:
                            self.is_selected = False

                    # If the user presses the left arrow key and they haven't selected a character,
                    # move to the left.
                    if event.key == pygame.K_LEFT and not self.is_selected:
                        self.character_index = max(0, self.character_index - 1)

                    # If the user presses the right arrow key and they haven't selected a character,
                    # move to the right.
                    elif event.key == pygame.K_RIGHT and not self.is_selected:
                        self.character_index = min(NUM_CHARS - 1, self.character_index + 1)

                    # If the user presses enter.
                    if event.key == pygame.K_RETURN:
                        # If they haven't selected a character, select it.
                        self.is_selected = True

    def draw(self):
        """
        Draws the screen, including the start screen and character select screen, accordingly.
        """

        # Task 3:

        # If we are drawing the start screen.
        if self.current_screen == Screen.START:

            # Make a font for the title and prompt.
            title_font = pygame.font.SysFont("chalkduster", 50)
            prompt_font = pygame.font.SysFont("consolas", 20)
            # Define the text you want to display
            title = "Character Select Demo"
            prompt = "Press Any Key to Start"

            # First, fill the screen with black to hide what was previously on the screen.
            self.screen.fill(BLACK)

            # Render the title and draw it on the top middle of the screen.
            title_text = title_font.render(title, True, RED)
            title_position = (WIDTH / 2 - title_text.get_width() / 2, 40)
            self.screen.blit(title_text, title_position)
            # Render the prompt and draw it on the bottom middle of the screen.
            prompt_text = prompt_font.render(prompt, True, YELLOW)
            prompt_position = (WIDTH / 2 - prompt_text.get_width() / 2, 600)
            self.screen.blit(prompt_text, prompt_position)

            # Draw the random character image.
            character_position = (
                WIDTH / 2 - character_image.get_width() / 2,
                HEIGHT / 2 - character_image.get_height() / 2
            )
            self.screen.blit(character_image, character_position)

        # Task 5:

        # If we are drawing the character select screen.
        if self.current_screen == Screen.SELECT:

            # Define the title and instruction fonts.
            title_font = pygame.font.SysFont("chalkduster", 40)
            instruction_font = pygame.font.SysFont("consolas", 16)

            # Define the text we want to display.
            title = "Select a Character"
            # Define a list of control instructions.
            instructions = [
                "Left / Right Arrow: Change Selection",
                "Enter: Select / Continue",
                "Escape: Cancel / Back"
            ]

            # First, fill the screen with black to hide what was previously on the screen.
            self.screen.fill(BLACK)
            # Render the title and draw it on the top middle of the screen.
            title_text = title_font.render(title, True, RED)
            title_position = (WIDTH / 2 - title_text.get_width() / 2, 40)
            self.screen.blit(title_text, title_position)
            # For each instruction, render the instruction and draw on the screen.
            for i in range(len(instructions)):
                instruction = instructions[i]
                instruction_text = instruction_font.render(instruction, True, YELLOW)
                instruction_position = (WIDTH / 2 - instruction_text.get_width() / 2, 600 + 20 * i)
                self.screen.blit(instruction_text, instruction_position)

            # For each character draw their image and stats.
            for i in range(len(character_data)):
                # Get the character data.
                data = character_data[i]
                image, stats = (data[0], data[1:])
                stat_names = ["STR", "DEX", "DEF", "INT", "CHA"]
                # Have to resize the images so they'll fit in a single row accross the screen.
                size = (WIDTH - MARGIN * 2 - PADDING * (NUM_CHARS - 1)) / NUM_CHARS
                image = pygame.transform.scale(image, (size, size))
                position = (MARGIN + image.get_width() * i + ((WIDTH - MARGIN * 2 - image.get_width() *
                                                              NUM_CHARS) / (NUM_CHARS - 1)) * i,
                            HEIGHT / 2 - image.get_height() - 20)
                # Draw the character's image.
                self.screen.blit(image, position)
                # Draw the selection box if needed.
                if i == self.character_index:
                    rect = pygame.Rect(position, image.get_size())
                    if not self.is_selected:
                        pygame.draw.rect(self.screen, YELLOW, rect, LINE_WIDTH)
                    else:
                        pygame.draw.rect(self.screen, RED, rect, LINE_WIDTH)
                # Draw the stats.
                stat_position = (position[0], position[1] + image.get_height() + PADDING)
                stat_font = pygame.font.SysFont("consolas", 16)
                for i in range(len(stats)):
                    stat_text = stat_font.render(stat_names[i] + ": " + str(stats[i]).zfill(2), True, YELLOW)
                    self.screen.blit(stat_text, (stat_position[0] + image.get_width() / 2 - stat_text.get_width() / 2, stat_position[1] + PADDING * 1 * i))

        # Update the display!
        pygame.display.flip()

# Task 1:

# Create a game manager to begin the execution of the program!
game_manager = GameManager()
