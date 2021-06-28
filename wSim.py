#https://stackoverflow.com/questions/51652313/elastic-collision-between-moving-particles-in-python-why-is-kinetic-energy-not


import pygame
pygame.init()


HEIGHT = 500
WIDTH = 500
NUM_BALLS = 2


#setup
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Simulation")

class Particle(object):
    def __init__(self, x, y, radius, xvel, yvel):
        self.x = x
        self.y = y
        self.radius = radius
        self.xvel = xvel #random.randint(3)
        self.yvel = yvel #random.randint(3)
        self.colideCheck = []
    def Draw_circle(self):
        pygame.draw.circle(win, (255,0,0), (int(self.x), int(self.y)), self.radius)


def redrawGameWindow():
    win.fill((0,0,0))
    for ball in balls:
        ball.Draw_circle()
    pygame.display.update()

def bounce(v1,v2, mass1 = 1, mass2 = 1):
    #i Tried my own bouncing mechanism, but doesn't work completly well, add yours here
    multi1 = mass1/(mass1+mass2)
    multi2 = mass2/(mass1+mass2)
    deltaV2 = (multi1*v1[0]-multi2*v2[0],multi1*v1[1]-multi2*v2[1])
    deltaV1 = (multi2*v2[0]-multi1*v1[0],multi2*v2[1]-multi1*v1[1])
    print("preVelocities:",v1,v2)
    return deltaV1,deltaV2



def checkCollide(circ1Cord,circ2Cord):
    if  circ1Cord == circ2Cord:
        return True
    else:
        return False







balls = []

balls.append(Particle(x=0, y=0,radius=5, xvel=10, yvel=0))

balls.append(Particle(x=100, y=50,radius=5, xvel=0, yvel=-5))




run = True
while run:

        #Windowu kapatmak
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

         #Duvarla Collision
    for ball in balls:
         if (ball.x) <= WIDTH and (ball.x) >= 0:
             ball.x += ball.xvel
         else:
             ball.xvel *= -1
             ball.x += ball.xvel


         if (ball.y) <= HEIGHT and (ball.y) >= 0:
             ball.y += ball.yvel
         else:
             ball.yvel *= -1
             ball.y += ball.yvel



    for ball in balls:
        for secBallCheck in balls:
            if secBallCheck not in ball.colideCheck and ball!= secBallCheck and checkCollide((ball.x,ball.y),(secBallCheck.x,secBallCheck.y)):

                print("COLLIDE")
                vel1,vel2 = bounce((ball.xvel,ball.yvel),(secBallCheck.xvel,secBallCheck.yvel))
                print("X Value: ", ball.x, "   |  Y Value: ", ball.y)
                ball.xvel = vel1[0]
                ball.yvel = vel1[1]
                ball.colideCheck.append(secBallCheck)
                secBallCheck.xvel = vel2[0]
                secBallCheck.yvel = vel2[1]
                secBallCheck.colideCheck.append(ball)
            elif not checkCollide((ball.x, ball.y),(secBallCheck.x, secBallCheck.y)):

                if ball in secBallCheck.colideCheck:
                    secBallCheck.colideCheck.remove(ball)
                    ball.colideCheck.remove(secBallCheck)
    redrawGameWindow()
    pygame.time.delay(20)

pygame.quit()