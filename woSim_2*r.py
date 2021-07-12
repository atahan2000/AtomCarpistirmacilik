#https://stackoverflow.com/questions/51652313/elastic-collision-between-moving-particles-in-python-why-is-kinetic-energy-not
import random
from math import sqrt

HEIGHT = 500
WIDTH = 500
NUM_BALLS = 2



class Particle(object):
    def __init__(self, x, y, radius, xvel, yvel):
        self.x = x
        self.y = y
        self.radius = radius
        self.xvel = xvel
        self.yvel = yvel




def euclidianDistance(tuple1, tuple2):
    return sqrt((tuple1[0] - tuple2[0])**2 + (tuple1[1] - tuple2[1])**2)


def checkCollideParticles(P1, P2):
    if euclidianDistance((P1.x,P1.y),(P2.x,P2.y)) <= 2*P1.radius:
        return True
    else:
        return False

def moveParticles(balls):          #Duvarla Collision ve Hareket
    for ball in balls:
         if (ball.x+ball.radius) <= WIDTH and (ball.x-ball.radius) >= 0:
             ball.x += ball.xvel
         else:
             ball.xvel *= -1
             ball.x += ball.xvel


         if (ball.y+ball.radius) <= HEIGHT and (ball.y-ball.radius) >= 0:
             ball.y += ball.yvel
         else:
             ball.yvel *= -1
             ball.y += ball.yvel


radius = 30
seed = random.randint(0,0)
for i in range(20):
    random.seed(seed)
    radius = radius*0.8

    balls = []
    balls.append(Particle(x=random.uniform(radius, WIDTH-radius), y=random.uniform(radius, HEIGHT-radius),radius=radius, xvel=random.random(), yvel=random.random()))
    balls.append(Particle(x=random.uniform(radius, WIDTH-radius), y=random.uniform(radius, HEIGHT-radius),radius=radius, xvel=random.random(), yvel=random.random()))

    run = True
    while run:
             #Duvarla Collision
        moveParticles(balls)

        # çarpıştılar mı?
        if checkCollideParticles(balls[0], balls[1]):
            print("COLLIDE")
            print("Ball #1:     ","X Value: ", balls[0].x, "   |  Y Value: ", balls[0].y)
            print("Ball #2:     ","X Value: ", balls[1].x, "   |  Y Value: ", balls[1].y)
            run = False

