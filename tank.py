# The player interacts with the game by moving the tank and firing missiles.
# Missiles are defined in a separate class, in their own file.
# Currently appears as a triangle, intend to replace with a turtle in a boat.

from turtle import Turtle

TANK_COLOR = "white"
TANK_POSITION = (0, 250)

class Tank(Turtle):
    def __init__(self):
        super(Tank, self).__init__()
        print("initializing tank")
        self.shape("tank")
        self.color(TANK_COLOR)
        self.penup()
        self.goto(TANK_POSITION)
        self.collision_width = 60

    def move_r(self):
        if self.xcor() < 320:
            self.forward(5)

    def move_l(self):
        if self.xcor() > -310:
            self.backward(5)
