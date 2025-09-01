'''

    Game Title: Solitaire 
    Created By: Zachary Starr
    Created On: 07/31/2025

    Reference material online: https://api.arcade.academy/en/2.6.7/tutorials/card_game/

    Main python library used for this program will be the 'arcade' library

'''

import time
import arcade

#######################################################################################

# Screen sizing and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Solitaire"

# Main application class
class Solitaire(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

    # Set up and end the game here
    def setup(self):

        pass

    # Render the screen/clear the screen
    def on_draw(self):

        arcade.start_render()
        # Draw the game elements here
        arcade.finish_render()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):

        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):

        pass

def main():

    print("Testing testing...\n")

    window = Solitaire()
    window.setup()
    arcade.run()

if __name__ == "__main__":

    main()

    time.sleep(5)
    print("Currently under development...")
    time.sleep(3)
    print("Pardon our dust")

