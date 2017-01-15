import math
# import everything from TurtleWorld module in the swampy package
from swampy.TurtleWorld import *

# create an Turtle instance
# bob = Turtle()

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

# def polygon(t, n, length):
# 	angle = 360.0/n

# 	for i in range(n):
# 		fd(t, length)
# 		lt(t, angle)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    print("arc_length = {}".format(arc_length))
    print("n = {}".format(n))
    print("step_length = {}".format(step_length))
    print("step_angle = {}".format(step_angle))

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

# def circle(t, r):k
# 	circumference = 2 * math.pi * r
# 	n = int(circumference / 3) + 1
# 	length = circumference / n
# 	polygon(t, n, length)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

# create an TurtleWorld instance
world = TurtleWorld()

bob = Turtle()
bob.delay = 0.01

radius = 100
pu(bob)
fd(bob, radius)
lt(bob)
pd(bob)
draw(bob, 20, 10)

wait_for_user()

