# Is this just a turtle object with player inputs? Consider removing this from the game.

# The player interacts with the game by moving the tank and firing missiles.
# Missiles are defined in a separate class, in their own file.
# Currently appears as a triangle, intend to replace with a turtle in a boat.
"""Allows the player to interact with the game."""
from turtle import Turtle

TANK_COLOR = "white"
TANK_POSITION = (0, 250)

class Tank(Turtle):
    """Tank extends Turtle.
    No additional attributes.
    """
    def __init__(self):
        """initiates tank."""
        super(Tank, self).__init__()
        print("initializing tank")
        self.shape("tank")
        self.color(TANK_COLOR)
        self.penup()
        self.goto(TANK_POSITION)
        self.collision_width = 60
        self.on_screen = True

    def move_r(self):
        """Moves the tank right 5 units, within screen boundaries"""
        if self.on_screen:
            if self.xcor() < 310:
                self.forward(5)

    def move_l(self):
        """Moves the tank left 5 units, within screen boundaries"""
        if self.on_screen:
            if self.xcor() > -315:
                self.backward(5)

    def blow_up(self):
        print("blow_up")
        self.on_screen = False
        self.right(90)

    def reset_from_top(self):
        self.setheading(0)
        self.penup()
        self.goto(TANK_POSITION)
        self.on_screen = True

    def sink(self):
        self.forward(20)