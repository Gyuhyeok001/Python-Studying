# method 1
import game.sound.echo

game.sound.echo.echo_test()
# This file is part of the Python Main package.
# It imports the echo_test function from the game.sound.echo module
# and calls it to demonstrate functionality.

# method 2
from game.sound import echo as ec

echo.echo_test()

# method 3
from game.sound import echo_test 

echo_test()