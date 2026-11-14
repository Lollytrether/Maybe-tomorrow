# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ash = Character("Ash", color="#38468D")
define bryce = Character("Bryce", color="#731B1B")
define harper = Character("Harper", color="#A245BC")

image bg corridor = "images/Bg/corridor.jpg"
image bg gym = "images/Bg/gym.jpg"
image bg locker = "images/Bg/locker.jpg"
image bg toilet = "images/Bg/toilet.jpg"

image ash = "images/ash.png"
image bryce = "images/bryce.png"
image harper = "images/harper.png"

default happiness = 5
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg locker

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ash

    # These display lines of dialogue.
    "this is narration"

    ash "This is me talking"

    # This ends the game.

    return
