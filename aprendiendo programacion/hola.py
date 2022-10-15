
from ctypes import _NamedFuncPointer
import turtle
import time

def curveMove():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


def drawHeart():
    turtle.speed(10) 
    turtle.color('red','pink')
    turtle.begin_fill()
    turtle.left(140) 
    turtle.forward(111.65) 
    curveMove() 
    turtle.left(120) 
    curveMove() 
    turtle.forward(111.65) 
    turtle.end_fill()
    time.sleep(10)

if _NamedFuncPointer== '_main_':
    drawHeart()