from Myro import *
from Graphics import *
from random import *

winsize=500
numball=400
win=Window("Balls", winsize, winsize)
win.mode="manual"

b=[]
dx=[]
dy=[]

for x in range(numball):
    ball=Circle((int(random()*winsize), int(random()*winsize)), 10)
    ball.draw(win)
    b.append(ball)

    ball.color=Color(random()*255,random()*255,random()*255)

    balldx=int(random()*30)-15
    balldy=int(random()*30)-15
    dx.append(balldx)
    dy.append(balldy)

for t in timer(20):
    for index in range(numball):
        b[index].move(dx[index],dy[index])
        if b[index].getX()<10 or b[index].getX()>winsize-10:
            dx[index]=-dx[index]
        if b[index].getY()<10 or b[index].getY()>winsize-10:
            dy[index]=-dy[index]

    wait(0.1)
    win.update()
