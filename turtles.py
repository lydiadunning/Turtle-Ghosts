# At this time, these turtle ghosts appear stationary on the screen.
# They will appear in a staggered formation, move gradually closer to
# the player's tank as the game progresses. They will shoot bubbles
# which damage the lilypads or end the player's life. They will be
# damaged by hits from the player's missile. After two or three hits,
# a turtle will disappear.

from math import floor
from turtle import Turtle

SPACING_X = 60
SPACING_Y = 70

class GhostTurtle(Turtle):
    """A single turtle, extends Turtle.

    Arguments:
        x: int
        y: int

    Attributes:
        All Turtle attributes.
        move_distance_x: int
        move_distance_y: int
    """
    def __init__(self, x, y):
        super(GhostTurtle, self).__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.turtlesize(2, 2, 2)

        # Current movement direction and distance. Negative for backwards movement.
        self.move_distance_x = 5
        self.move_distance_y = 20
        self.setposition(x, y)

    def move_x_detect_edge(self):
        """
        Moves the turtle over by move_distance_x and returns true if out of bounds

        returns: boolean indicating whether to turn here
        """
        self.setx(self.xcor() + self.move_distance_x)
        print(self.xcor())
        return self.xcor() > 300 or self.xcor() < -310

    def move_y(self):
        """
        Moves the turtle up by move_distance_y and returns collision information if necessary

        Returns: a dictionary with the turtle's collision boundaries if ycor risks hitting lilypads
        """
        self.sety(self.ycor() + self.move_distance_y)
        if self.ycor() >= 160:
            return self.get_collision()

    def hit(self):
        """
        Reflects visually that the ghost has been hit by changing its color

        returns: True if the ghost should be destroyed.
        """
        if self.color() == "white":
            self.color("lavenderblush3")
        elif self.color() == "lavenderblush3":
            self.color("lavenderblush4")
        elif self.color() == "lavenderblush4":
            self.color("gray20")
        else:
            return True

    def get_collision(self):
        """
        Returns a dictionary of the outer boundaries of the turtle
        """
        return {'top': self.ycor() + 20,
                'bottom': self.ycor() - 20,
                'left': self.xcor() - 20,
                'right': self.xcor() + 20}


class GhostTurtleSwarm():
    """
    Creates ghost turtle objects, controls ghost turtle behavior.

    Attributes:
        starting_x: int
        starting_y: int
        turtles: list of ghost turtle objects
    """
    def __init__(self):
        """Initializes the Ghost Turtles"""
        self.starting_x = -220
        self.starting_y = -100

        # A list of ghost turtle object instances
        self.turtles = []

        self.make_turtles()

    def make_turtles(self):
        """
        Declares GhostTurtle objects positioned in a grid, adds these to the .turtles attribute
        """
        y = self.starting_y
        for turtle_row in range(4):
            x = self.starting_x
            for i in range(8):
                turtle = GhostTurtle(x, y)
                self.turtles.append(turtle)
                x += SPACING_X
            y -= SPACING_Y

    def move(self):
        """
        Tells the group of ghost turtles to move

        :return: returns collision data from any turtles above the lowest point of the lilypads.

        """
        collision = []
        # This next line might do too much.
        if [True for turtle in self.turtles if turtle.move_x_detect_edge()]:
            for turtle in self.turtles:
                turtle.move_distance_x *= -1
                collision.append(turtle.move_y())
        return collision


    def hit(self, turtle):
        """does nothing so far"""
        turtle.reset()
        index = self.turtles.index(turtle)
        self.turtles.remove(turtle)


