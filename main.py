# This is a modified version of the Atari classic Space Invaders.
# It uses the turtle shape provided by the turtle graphics module.
# In the game, a turtle in a boat defends against ghost turtles
# rising from the depths.
# Maybe player death should add a turtle to the group.

from turtle import Turtle, Screen
from tank import Tank
from time import sleep
from lilypad import LilyPad
from turtles import GhostTurtleSwarm
from missile import Missile

screen = Screen()
screen.bgcolor("black")
screen.setup(700, 600, None, 100)
screen.title("Space Invaders")
screen.tracer(0)


screen.register_shape("tank", ((-10, -30), (-10, 30), (10, 0)))
screen.register_shape("missile", ((-1, -5), (1, -5), (1, 5), (-1, 5)))
tank = Tank()
lilypad = LilyPad()
ghosts = GhostTurtleSwarm()
missiles = []

def fire_a_missile():
    missile = Missile(tank.xcor(), tank.ycor())
    missiles.append(missile)


screen.listen()
screen.onkeypress(tank.move_r, "Right")
screen.onkeypress(tank.move_l, "Left")
screen.onkeypress(fire_a_missile, "space")


while True:
    sleep(.05)
    screen.update()
    # ghosts.move() returns hitboxes for each turtle.
    ghost_collision = ghosts.move()
    if ghost_collision:
        lilypad_collision = lilypad.get_collision_x_vals()
        # The idea here is to compare whether any lilypad xvals fall within the ghosts' collision boxes.
        # if they do, both any lilypad and ghost which have collided are destroyed.



    spent_missiles = []
    for missile in missiles:
        in_motion = True
        if missile.ycor() <= 210:
            hit_test = lilypad.detect_missile(missile.xcor(), missile.ycor(), "missile")
            if hit_test:
                missile.shoot_through(hit_test)
                spent_missiles.append(missile)
                in_motion = False
        if missile.ycor() <= -300:
            spent_missiles.append(missile)
        if in_motion:
            missile.move()
    missiles = [m for m in missiles if m not in spent_missiles]

# End-game condition not yet implemented
screen.exitonclick()