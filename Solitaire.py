'''

    Game Title: Solitaire
    Created By: Zachary Starr
    Created On: 07/31/2025

    Reference material online: https://api.arcade.academy/en/2.6.7/tutorials/card_game/

    Main python library used for this program will be the 'arcade' library

'''

import time
import arcade

# Screen sizing and title
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Solitaire, by Zach"

# Constants for scaling the size of the cards
CARD_SCALE = 0.5

# Card dimensions after scaling
CARD_WIDTH = 100 * CARD_SCALE
CARD_HEIGHT = 150 * CARD_SCALE

# Mat size where the cards will be placed
MAT_PERCENTAGE_OVERSIZE = 1.25
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENTAGE_OVERSIZE)
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENTAGE_OVERSIZE)

# Space between the cards and the edge of the screen
VERTICAL_MARGIN = 0.10
HORIZONTAL_MARGIN = 0.10

# Margins for the cards
BOTTOM_MARGIN = MAT_HEIGHT / 2 + (MAT_HEIGHT * VERTICAL_MARGIN)
START_MARGIN = MAT_HEIGHT / 2 + (MAT_HEIGHT * HORIZONTAL_MARGIN)

# Card Values and suits
CARD_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

# Class for the Cards
class Cards(arcade.Sprite):

    def __init__(self, value: str, suit: str, scale=1) -> None:

        # Set the card's value and suit
        self.value = value
        self.suit = suit

        # Load the card image based on its suit and value, uses the arcade library file path to load the image
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"

        # Call the parent class (Sprite) constructor
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")

#######################################################################################

# Main application class called Solitaire that inherits from arcade.Window
class Solitaire(arcade.Window):

    # Initialize the game window
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.card_list = None

        arcade.set_background_color(arcade.color.AMAZON)

    # Set up and end the game here
    def setup(self) -> None:
        print("Running...")

        # Create a sprite list to hold the cards
        self.card_list = arcade.SpriteList()

        # Create the deck of cards
        for suit in CARD_SUITS:
            for value in CARD_VALUES:
                card = Cards(value, suit, CARD_SCALE)
                card.position = START_MARGIN, BOTTOM_MARGIN
                self.card_list.append(card)                 # Add the card to the sprite list

        pass

    # Render the screen/clear the screen
    def on_draw(self) -> None:
        self.clear()

        # Draw the game elements here
        exit = arcade.Text("Press 'q' to quit",
                         780,
                         10,
                         arcade.color.WHITE,
                         14)

        exit.draw()

        self.card_list.draw()

        pass

    # Update the game state here
    def update(self, delta_time: float) -> None:

        pass

    # Handle mouse and keyboard input here
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:

        pass

    # Handle mouse release events here
    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int) -> None:

        pass

    # Handle mouse motion events here
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:

        pass

    # Handle key press events here
    def on_key_press(self, key: int, modifiers: int) -> None:
        if key == arcade.key.Q:
            print("Exiting...")
            self.close()

        pass

######################################################################################

# Main function to run the game
def main():

    print("Testing testing...\n")

    window = Solitaire()
    window.setup()
    arcade.run()

# Run the main function if this file is executed
if __name__ == "__main__":

    main()

    time.sleep(5)
    print("Currently under development...")
    time.sleep(3)
    print("Pardon our dust")