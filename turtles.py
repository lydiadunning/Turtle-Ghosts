# At this time, these turtle ghosts appear stationary on the screen.
# They will appear in a staggered formation, move gradually closer to
# the player's tank as the game progresses. They will shoot bubbles
# which damage the lilypads or end the player's life. They will be
# damaged by hits from the player's missile. After two or three hits,
# a turtle will disappear.

from math import floor
from turtle import Turtle

SPACING_X = 40
SPACING_Y = 30

class Ghosts():
    def __init__(self):
        self.starting_x = -200
        self.starting_y = -200
        self.turtles = []
        self.make_turtles()

    def make_turtles(self):
        y = self.starting_y
        for turtle_row in range(4):
            x = self.starting_x
            for i in range(8):
                turtle = self.make_turtle()
                turtle.setposition(x, y)
                self.turtles.append(turtle)
                x += SPACING_X
            y -= SPACING_Y

    def make_turtle(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("turtle")
        turtle.color("white")
        turtle.setheading(90)
        return turtle

    def hit(self, turtle):
        turtle.reset()
        self.turtles.remove(turtle)


