#https://stackoverflow.com/questions/51652313/elastic-collision-between-moving-particles-in-python-why-is-kinetic-energy-not
import random
from nec.particleClass import Particle
from nec.func import *


radius = 30
seed = random.randint(0,0)


for i in range(20):
    random.seed(seed)
    radius = radius*0.8


    P1 = Particle(x=random.uniform(radius, WIDTH-radius), y=random.uniform(radius, HEIGHT-radius),radius=radius, xvel=random.random(), yvel=random.random())
    P2 = Particle(x=random.uniform(radius, WIDTH-radius), y=random.uniform(radius, HEIGHT-radius),radius=radius, xvel=random.random(), yvel=random.random())
    balls = [P1,P2]


    run = True
    while run:
        moveParticles(balls)

        if checkCollideParticles(balls[0], balls[1]):
            print("COLLIDE")
            print("Ball #1:     ","X Value: ", balls[0].x, "   |  Y Value: ", balls[0].y)
            print("Ball #2:     ","X Value: ", balls[1].x, "   |  Y Value: ", balls[1].y)
            run = False

