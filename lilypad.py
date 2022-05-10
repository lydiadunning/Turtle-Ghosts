
# lilypads serve as barriers in the game, and take damage when hit.
# They are drawn on the screen, and damage is represented by drawing
# over them and modifying their collision data.
# Collision data is stored as a dictionary made up of lines, with an
# x coordinate and two y coordinates, indicating the top and bottom
# of the lilypad. When a collision results in drawing over the
# lilypad, the y coordinates change to correspond with their new
# appearance. Collision information for any x coordinate will be
# removed when the top and bottom y values are the same.

from turtle import Turtle
from math import ceil, floor

class LilyPad():
    def __init__(self):
        self.coordinates = []
        self.collision = {}
        self.draw_all()


    # Current approach - the lilipads are stamped into place.
    def draw_all(self):
        center_x_list = [-200, -100, 0, 100, 200]
        turtle = Turtle()
        turtle.color("green")
        # turtle.shape("circle")
        turtle.penup()
        turtle.pensize(20)
        for x in center_x_list:
            turtle.setposition(x - 30, 200)
            start = turtle.position()
            turtle.pendown()
            turtle.forward(60)
            turtle.penup()
            end = turtle.position()
            self.coordinates.append([start, end])
            self.create_hitbox(x, 200)
        turtle.hideturtle()

#   Current approach - these change size when the lilypad is hit.
    def create_hitbox(self, center_x, center_y):
        for x in range(center_x - 40, center_x + 40, 5):
            self.collision[str(x)] = {'top_y': center_y + 10, 'bottom_y': center_y - 10}

#   Overcomes floating point errors.
    def convert_to_key(self, val):
        if val % 5 == 0:
            return str(int(val))
        elif floor(val) % 5 == 0:
            return str(int(floor(val)))
        elif ceil(val) % 5 == 0:
            return str(int(ceil(val)))
        else:
            print("lilypad.convert_to_key failed")


    def detect_missile(self, missile_x, missile_y, source):
        print(self.collision.keys())
        target = self.convert_to_key(missile_x)
        print(target)
        if target not in self.collision.keys():
            print("not_found")
            return None

        hit = self.collision[target]
        if hit['bottom_y'] <= missile_y <= hit['top_y']:
            if hit['top_y'] > hit['bottom_y']:
                hit['top_y'] -= 5
                return hit['top_y'] + 5
            else:
                del hit
        else:
            return None

    def get_collision_x_vals(self):
        x_values = self.collision.keys()
        return[int(val) for val in x_values]
