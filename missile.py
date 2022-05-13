"""Missiles fired by tanks"""
# Missiles appear where the tank is located when the player presses
# the space bar. They move in a single direction at a consistent
# speed, and when they collide with an object they modify that object's appearance.
# All missiles must fire where their xcor() is divisible by 5.


from turtle import Turtle

class Missile(Turtle):
    """The Missile Class
    Extends Turtle"""
    def __init__(self, start_x, start_y):
        """__init__ for Missile"""
        super(Missile, self).__init__()
        self.color("white")
        self.shape("missile")
        self.penup()
        self.goto(start_x, start_y)
        self.setheading(270)

    def move(self):
        """Moves the missile up 10 units"""
        self.forward(10)

    def shoot_through(self, y_start):
        """Draws a short black line meant to indicate player-initiated damage to a lilypad.
        Hides the missile. """

        self.sety(y_start)
        self.color("black")
        self.pensize(3)
        self.pendown()
        self.forward(9)
        self.hideturtle()


class Bubble(Missile):
    def __init__(self, start_x, start_y):
        super(Bubble, self).__init__(start_x, start_y)
        self.setheading(90)
        self.shape("circle")
        self.color('aliceblue')

    def blast(self, y_center):
        self.sety(y_center)
        self.color("black")
        self.shape("blast")
        self.stamp()
        self.hideturtle()

