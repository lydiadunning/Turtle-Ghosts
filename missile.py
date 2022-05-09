# Missiles appear where the tank is located when the player presses
# the space bar. They move in a single direction at a consistent
# speed, and when they collide with an object they modify that object's appearance.
# All missiles must fire where their xcor() is divisible by 5.


from turtle import Turtle

class Missile(Turtle):
    def __init__(self, start_x, start_y):
        super(Missile, self).__init__()
        self.color("white")
        self.shape("missile")
        self.penup()
        self.goto(start_x, start_y)
        self.setheading(270)

    def move(self):
        self.forward(10)

    def shoot_through(self, y_start):
        self.sety(y_start)
        self.color("black")
        self.pensize(3)
        self.pendown()
        self.forward(5)
        self.hideturtle()



