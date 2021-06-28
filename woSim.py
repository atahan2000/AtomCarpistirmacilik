#https://stackoverflow.com/questions/51652313/elastic-collision-between-moving-particles-in-python-why-is-kinetic-energy-not#51652695

#Her şeyi roundla?
#0,0'dan başlayamıyor geri gime gereksinimi
#dışarı çıkıyor sonra dönüyor
#continuous değil
#hep işlem yapan bir bilgisayar olsa?



HEIGHT = float(100)
WIDTH = float(100)


#CARTESİAN COORDINATE

#Particle_1
x1=1
y1=1
xvel1=2
yvel1=2

#Particle_2
x2=30
y2=30
xvel2=-1
yvel2=-1

#rounding için?
def truncate(n, decimals=0):   #https://realpython.com/python-rounding/
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

class Particle(object):
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.colideCheck = []



def checkCollideParticles(Particle1, Particle2):
    if (Particle1.x == Particle2.x) and (Particle1.y == Particle2.y):
        return True
    else:
        return False

def moveParticles(balls):          #Duvarla Collision ve Hareket
    for ball in balls:
         if (ball.x) < WIDTH and (ball.x) > 0:
             ball.x += ball.xvel
         else:
             ball.xvel *= -1
             ball.x += ball.xvel


         if (ball.y) < HEIGHT and (ball.y) > 0:
             ball.y += ball.yvel
         else:
             ball.yvel *= -1
             ball.y += ball.yvel




Particle1 = Particle(float(x1), float(y1), float(xvel1), float(yvel1))
Particle2 = Particle(float(x2), float(y2), float(xvel2), float(yvel2))
balls = [Particle1, Particle2]



run = True
i= 0

while run:

    moveParticles(balls)

    #her iterationda pozisyon print ediyor
    i += 1
    if i%1 == 0:
        print("Ball1: X Value: ", balls[0].x, "   |  Y Value: ", balls[0].y, "   |||   Ball2:  X Value: ", balls[1].x, "   |  Y Value: ", balls[1].y,)

    #çarpıştılar mı?
    if checkCollideParticles(Particle1, Particle2):
        print("COLLIDE")
        print("X Value: ", balls[0].x, "   |  Y Value: ", balls[0].y)
        run = False


