
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
        if type(val) == str:
            print("string detected")
            return val
        elif val % 5 == 0:
            return str(int(val))
        elif floor(val) % 5 == 0:
            return str(int(floor(val)))
        elif ceil(val) % 5 == 0:
            return str(int(ceil(val)))
        else:
            print("lilypad.convert_to_key failed")


    def detect_missile(self, missile_x, missile_y, source):
        if source == "missile":
            target = self.convert_to_key(missile_x)
            if target not in self.collision.keys():
                return None
            hit = self.collision[target]
            if hit['bottom_y'] <= missile_y <= hit['top_y']:
                if hit['top_y'] - 5 > hit['bottom_y']:
                    hit['top_y'] -= 5
                    return hit['top_y'] + 5
                else:
                    self.delete_from_collision(target)
            else:
                return None
        if source == 'bubble':
            target = self.convert_to_key(missile_x)
            if target in self.collision.keys():
                hit = self.collision[target]
                print(hit)
                if hit['bottom_y'] <= missile_y + 5 :
                    if hit['top_y'] > hit['bottom_y'] + 7:
                        self.collision[target]['bottom_y'] += 7
                        print(self.collision[target])

                        return hit['bottom_y']
                    else:
                        print('DELETE')
                        self.delete_from_collision(target)
                        return 400
            return None


            # missile_width = [missile_x, missile_x - 5, missile_x + 5]
            # for missile in missile_width:
            #     target = self.convert_to_key(missile)
            #     if target in self.collision.keys():
            #         hit = self.collision[target]
            #         print(hit)
            #         if hit['bottom_y'] <= missile_y + 5 <= hit['top_y'] or \
            #                 hit['bottom_y'] <= missile_y - 5 <= hit['top_y']:
            #             if hit['top_y'] > hit['bottom_y'] + 7:
            #                 self.collision[target]['bottom_y'] += 7
            #                 print(self.collision[target])
            #
            #                 return hit['bottom_y']
            #             else:
            #                 print('DELETE')
            #                 self.delete_from_collision(target)
            #                 return 400
            # return None


    def get_collision_x_vals(self):
        x_values = self.collision.keys()
        return[int(val) for val in x_values]

    def detect_collision(self, collision):
        lilypad_x_hits = []
        collided = []
        for i in collision:
            intersection = [x for x in self.get_collision_x_vals() if i['left'] < x < i['right']]
            collided.append(i)
            lilypad_x_hits.extend(intersection)
        return lilypad_x_hits, collided

    def destroy_lilypads(self, lilypad_x_hits):
        collision_to_delete = []
        for lilypad in self.coordinates:
            intersection = [x for x in lilypad_x_hits if lilypad[0][0] < x < lilypad[1][0]]

            if intersection:
                collision_to_delete.extend(intersection)
                turtle = Turtle()
                turtle.pensize(20)
                turtle.color('black')
                turtle.penup()
                turtle.setposition(lilypad[0])
                turtle.pendown()
                turtle.forward(60)
                turtle.hideturtle()
        for intersection in collision_to_delete:
            print('intersection')
            print(intersection)
            self.delete_from_collision(intersection)

        # if lilypad_x_hits:
        #     self.collision = {key: self.collision[key] for key in self.collision if key not in lilypad_x_hits}


    def draw_collision(self, turtle = Turtle()):
        turtle.reset()
        turtle.color('orange')
        turtle.setheading(270)
        for key in self.collision:
            turtle.penup()
            turtle.setx(int(key))
            turtle.sety(self.collision[key]['top_y'])
            distance = self.collision[key]['top_y'] - self.collision[key]['bottom_y']
            turtle.pendown()
            turtle.forward(distance)
        return turtle

    def delete_from_collision(self, key_to_delete):
        print("DELETE")
        print(key_to_delete)
        print(type(key_to_delete))
        if type(key_to_delete) != str          :
            print("not str")
            key_to_delete = self.convert_to_key(key_to_delete)
        print(key_to_delete)
        print(self.collision.pop(key_to_delete))
        # print(self.collision.keys())
        # del self.collision[key_to_delete]
        print(self.collision.keys())
        # if key_to_delete in self.collision.keys():
        #     del self.collision[key_to_delete]
        #     print(self.collision.keys())
        # else:
        #     print('cannot delete')