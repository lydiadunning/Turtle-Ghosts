# This is a modified version of the Atari classic Space Invaders.
# It uses the turtle shape provided by the turtle graphics module.
# In the game, a turtle in a boat defends against ghost turtles
# rising from the depths.
# Maybe player death should add a turtle to the group.
import random
from turtle import Turtle, Screen
from tank import Tank
from time import sleep
from lilypad import LilyPad
from turtles import GhostTurtleSwarm
from missile import Missile
from missile import Bubble

screen = Screen()
screen.bgcolor("black")
screen.setup(700, 600, None, 100)
screen.title("Space Invaders")
screen.tracer(0)


screen.register_shape("tank", ((-10, -30), (-10, 30), (10, 0)))
screen.register_shape("missile", ((-1, -5), (1, -5), (1, 5), (-1, 5)))
screen.register_shape("blast", ((-6, -7), (7, -7), (6, -6), (7, -4),
                                (6, -2), (7, -1), (7, 2), (4, 1),
                                (6, 4,), (5, 5), (-2, 4), (1, -7),
                                (-2, 6), (-1, 3), (-7, 6), (-5, 4),
                                (-7, 2), (-5, -1), (-7, -3), (-7, -5)))

tank = Tank()
lilypad = LilyPad()
ghosts = GhostTurtleSwarm()
missiles = []
bubbles = []

def fire_a_missile():
    if tank.on_screen:
        missile = Missile(tank.xcor(), tank.ycor())
        missiles.append(missile)


screen.listen()
screen.onkeypress(tank.move_r, "Right")
screen.onkeypress(tank.move_l, "Left")
screen.onkeypress(fire_a_missile, "space")
collision_turtle = None

while True:
    sleep(.05)
    screen.update()

# Consider:
    # Rework all collision.
    # Start with a list of x coordinates for missiles, lilypads, and ghosts.
    # if they're the same, compare y coordinates.
    # actually, generating a list of x coordinates for ghosts might be simpler than calculating a range.

    # ghosts.move() returns hitboxes for each turtle.
    ghost_collision = ghosts.move()
    if ghost_collision:
        lilypad_x, damaged_ghosts = lilypad.detect_collision(ghost_collision)
        ghosts.remove_ghost_by_collision(damaged_ghosts)
        lilypad.destroy_lilypads(lilypad_x)



    spent_missiles = []
    for missile in missiles:
        in_motion = True
        if missile.ycor() <= 210 and missile.ycor() >= 190:
            hit_test = lilypad.detect_missile(missile.xcor(), missile.ycor(), "missile")
            if hit_test:
                missile.shoot_through(hit_test)
                spent_missiles.append(missile)
                in_motion = False
        if missile.ycor() <= -300:
            spent_missiles.append(missile)
        # Detect collision with any ghost. Damage the ghost, destroy the missile.
        if ghosts.detect_hit(missile.xcor(), missile.ycor()):
            in_motion = False
            missile.hideturtle()
            spent_missiles.append(missile)

        # check for bubble collision:
        for bubble in bubbles:
            bubble_collisions = [bubble for bubble in bubbles if bubble.xcor() - 10 <=
                                  missile.xcor() <= bubble.xcor() + 10 and bubble.ycor() - 5 <=
                                  missile.ycor() <= bubble.ycor() + 5]
            if bubble_collisions:
                spent_missiles.append(missile)
                missile.hideturtle()
                for bubble in bubble_collisions:
                    bubble.hideturtle()
                    bubbles.remove(bubble)


        if in_motion:
            missile.move()
    missiles = [m for m in missiles if m not in spent_missiles]

    # Ghost bubbles
    if random.randint(1, 12) == 12:
        first_row = ghosts.get_first_row()
        chosen = first_row[random.randint(0, len(first_row) - 1)]
        bubble = Bubble(chosen.xcor(), chosen.ycor())
        bubbles.append(bubble)

    for bubble in bubbles:

        # checking collision with missiles happens in the missile loop
        # check collision with lilypads
        hit_detected = lilypad.detect_missile(bubble.xcor(), bubble.ycor(), 'bubble')
        if hit_detected:
            bubble.blast(hit_detected)
            bubble.hideturtle()
            bubbles.remove(bubble)

        # check collision with the tank
        if tank.on_screen:
            if tank.xcor() - 40 < bubble.xcor() < tank.xcor() + 40 and tank.ycor() - 20 < bubble.ycor() < tank.ycor() + 20:
                tank.blow_up()
                bubble.hideturtle()
                bubbles.remove(bubble)

        bubble.move()

    if not tank.on_screen:
        print("moving")
        tank.sink()
        if tank.ycor() < -350:
            tank.reset_from_top()

    # if collision_turtle:
    #     collision_turtle = lilypad.draw_collision(collision_turtle)
    # else:
    #     collision_turtle = lilypad.draw_collision()
# End-game condition not yet implemented
screen.exitonclick()