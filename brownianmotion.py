import pygame
from random import uniform
import numpy as np

WIDTH, HEIGHT = 500,500
COLORS = {'k':(0,0,0),'w':(255,255,255),'g':(0,255,0),'r':(255,0,0),'y':(255,255,0),'b':(0,0,255)}
r = 5
t = 0.01
v = 1000
n = 100

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Brownian Motion')

clock = pygame.time.Clock()

class Ball:
    def __init__(self,r):
        self.pos = np.array([uniform(0,WIDTH-1),uniform(0,HEIGHT-1)])
        self.vel = np.array([uniform(-v,v),uniform(-v,v)])
        self.r = r
        self.box = [self.pos[0]-r,self.pos[0]+r,self.pos[1]-r,self.pos[1]+r]
        
    def plot(self):
        pygame.draw.circle(screen,COLORS['b'],(int(self.pos[0]),int(self.pos[1])),self.r,0)
        
class System:
    def __init__(self,balls):
        self.balls = balls     
        self.size = len(balls)
        
    def plot(self):
        for ball in self.balls:
            ball.plot()
            
    def update(self):
        for ball in self.balls:
            ball.pos += ball.vel*t
            
    def wall_collision(self):
        for ball in self.balls:
            if ball.pos[0] < 0 or ball.pos[0] > WIDTH-1:
                ball.vel[0] *= -1
            if ball.pos[1] < 0 or ball.pos[1] > HEIGHT-1:
                ball.vel[1] *= -1
                
    def ball_collision(self):
        for i,iBall in enumerate(self.balls):
            for j,jBall in enumerate(self.balls):
                if i != j:
                    D = iBall.r+jBall.r
                    d = np.linalg.norm(jBall.pos-iBall.pos)
                    if d < D:
                        iBall.vel[0] *= -1
                        iBall.vel[1] *= -1                    
    
# balls = [Ball(),Ball()]
balls = []
for i in range(0,n):
    balls.append(Ball(r))
system = System(balls)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(COLORS['k'])
    
    system.wall_collision()
    
    system.ball_collision()
    
    system.update()
    
    system.plot()
    
    pygame.display.update()
    
    clock.tick(30)
    
pygame.quit()