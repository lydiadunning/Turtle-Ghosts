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
        self.draw()


    # Current approach - the lilipads are stamped into place.
    def draw(self):
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
        # identify the relevant item in the hitbox list.
        # identify if the y location falls in the hitbox's y range
        # print(self.collision[0])
        # relevant_hitbox = [hit for hit in self.collision if hit.x == missile_x]
        # hit = relevant_hitbox[0]
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


# from turtle import Turtle
#
# class LilyPad():
#     def __init__(self, center_x, y):
#         self.lilypad_left = self.make_section(center_x - 30, y, "circle")
#         self.lilypad_center_l = self.make_section(center_x - 20, y, "square")
#         self.lilypad_center = self.make_section(center_x, y, "square")
#         self.lilypad_center_r = self.make_section(center_x + 20, y, "square")
#         self.lilypad_right = self.make_section(center_x + 30, y, "circle")
#
#         self.hits = [0, 0, 0, 0, 0]
#         self.hit_range = [[center_x - 40, center_x - 30, y + 10],
#                           [center_x - 30, center_x - 10, y + 10],
#                           [center_x - 10, center_x + 10, y + 10],
#                           [center_x + 10, center_x + 30, y + 10],
#                           [center_x + 30, center_x + 40, y + 10]]
#         self.hitbox = self.create_hitbox(center_x, y)
#         self.whole_lilypad = [self.lilypad_left,
#                               self.lilypad_center_l,
#                               self.lilypad_center,
#                               self.lilypad_center_r,
#                               self.lilypad_right]
#
#     def make_section(self, x, y, shape):
#         turtle = Turtle()
#         turtle.penup()
#         turtle.shape(shape)
#         turtle.color("green")
#         turtle.setposition(x, y)
#         turtle.stamp()
#         turtle.hideturtle()
#         return turtle
#
# # Current approach - these change size when the lilypad is hit.
#     def create_hitbox(self, center_x, center_y):
#         hitbox = []
#         for x in range(center_x - 30, center_x + 30, 3):
#             hitbox.append({'x': x, 'top_y': center_y - 10, 'bottom_y': center_y + 10})
#             return hitbox
#
#
#
#
#     def hit(self, section):
#         self.hits[section] += 1
#         if self.hits[section] == 1:
#             self.hit_range[section][2] -= 10
#         elif self.hits[section] == 2:
#             self.whole_lilypad[section].color = "black"
#             self.whole_lilypad[section].stamp()
#             del self.hit_range[section]
#
#     def detect_missile(self, missile_x, missile_y):
#         for lilypad in self.hit_range:
#             if missile_x > lilypad[0] and missile_x < lilypad[1]:
#                 if missile_y == lilypad[2]:
#                     return self.hit_range.index(lilypad)