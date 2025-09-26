'''

    Game Title: Solitaire
    Created By: Zachary Starr
    Created On: 07/31/2025

    Reference material online: https://api.arcade.academy/en/2.6.7/tutorials/card_game/

    Main python library used for this program will be the 'arcade' library

    zzzzzzzzzzzzzzzzzzzzzzzz

'''

import time
import arcade

#######################################################################################

# Screen sizing and title
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Solitaire, by Zach"

# Main application class
class Solitaire(arcade.Window):

    # Initialize the game window
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

    # Set up and end the game here
    def setup(self) -> None:
        print("Running...")

        pass

    # Render the screen/clear the screen
    def on_draw(self) -> None:
        self.clear()

        # Draw the game elements here
        exit = arcade.Text("Press 'q' to quit",
                         10,
                         10,
                         arcade.color.WHITE,
                         14)

        exit.draw()

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

