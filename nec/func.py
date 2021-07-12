from math import sqrt
from nec.config import WIDTH, HEIGHT


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