# Generar una clase que maneje todos los trazos
from turtle import *

v = 0 # velocidad máxima de la tortuga
step = 10 # pasos

t = Turtle()
t.color('black')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(v)

scr = t.getscreen()

def draw(x, y):
  t.goto(x, y)

def move(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()

# parámetros de trazo

def setWidth_1():
    t.width(5)

def setWidth_2():
    t.width(10)

def setWidth_3():
    t.width(18)

def setWidth_4():
    t.width(25)

def setWidth_5():
    t.width(35)    

# Movimiento con teclas

def stepUp():
 t.goto(t.xcor(), t.ycor() + step)
 
def stepDown():
 t.goto(t.xcor(), t.ycor() - step)
 
def stepLeft():
 t.goto(t.xcor() - step, t.ycor())
 
def stepRight():
 t.goto(t.xcor() + step, t.ycor())
 
def startFill():
  t.begin_fill()
 
def endFill():
  t.end_fill()

t.ondrag(draw)