#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      No
#
# Created:     26/06/2020
# Copyright:   (c) No 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import time

class planet:
    def __init__ (self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
    def returninfo (self):
        return [self.mass, self.position]
    def recalcvelocity (self, allplanets):
        force = [0, 0]
        for a in allplanets:
            xdistance = a[1][0]-self.position[0]
            ydistance = a[1][1]-self.position[1]
            distancesquared = (xdistance**2)+(ydistance**2)
            #900 was found to be a relatively small distance which prevented the balls from being flung
            if distancesquared >= 900:
                totalgravity = (self.mass*a[0])/distancesquared
                multiplystuffbythis = totalgravity/(distancesquared**0.5)
                #vectors are phun
                xgravity = multiplystuffbythis*xdistance
                ygravity = multiplystuffbythis*ydistance
                #fysics is phun
                force[0] += 10*xgravity/self.mass
                force[1] += 10*ygravity/self.mass
        self.velocity[0] += force[0]
        self.velocity[1] += force[1]
    def recalcposition (self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

#can be changed to whatever
ball1 = planet(1, [400, 300], [0, 0])
ball2 = planet(1, [200, 300], [0, 0])
ball3 = planet(1, [200, 250], [0, 0])

#pygame stuff that I don't understand
pygame.init()
gamedisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#"game loop"
while running:
    startframetime = time.time()

    #closes nicely when X is clicked on window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gamedisplay.fill((255, 255, 255))

    #list of information of planets
    planets = [ball1.returninfo(), ball2.returninfo(), ball3.returninfo()]

    #makes position nice for pygame and draws it
    for a in planets:
        drawposition = [int((a[1][0])), 600-int((a[1][1]))]
        pygame.draw.circle(gamedisplay, (0, 0, 0), drawposition, 5)

    pygame.display.update()

    ball1.recalcposition()
    ball2.recalcposition()
    ball3.recalcposition()

    ball1.recalcvelocity(planets)
    ball2.recalcvelocity(planets)
    ball3.recalcvelocity(planets)

    #waits for appropriate time
    if (0.01-(time.time()-startframetime)) > 0:
        time.sleep(0.01-(time.time()-startframetime))

pygame.quit()



















