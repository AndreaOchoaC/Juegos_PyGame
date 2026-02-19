# Modificación Andrea

from turtle import *
from random import randint
from time import *

w = 200
h = 200

# dibujar un perímetro para ver el área en que debe estar la tortuga
t = Turtle()
t.pensize(1)
t.color("#6f7173")
t.penup()
t.goto(200,0)
t.pendown()
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)

start = time()

t1 = Turtle()
t1.color("green")
t1.width(5)
t1.shape('turtle')

t2 = Turtle()
t2.color("blue")
t2.width(5)
t2.shape('turtle')
t2.left(120)

t3 = Turtle()
t3.color("red")
t3.width(5)
t3.shape('turtle')
t3.left(240)

# Definimos los tres eventos de catch

def catch1(x, y):
  t1.penup()
  t1.goto(randint(-100,100),randint(-100,100))
  t1.pendown()
  t1.left(randint(0, 180))

def catch2(x, y):
  t2.penup()
  t2.goto(randint(-100,100),randint(-100,100))
  t2.pendown()
  t2.left(randint(0, 180))

def catch3(x, y):
  t3.penup()
  t3.goto(randint(-100,100),randint(-100,100))
  t3.pendown()
  t3.left(randint(0, 180))

puntos = 0
penup()
goto(200,200)
pendown()
write(f"Puntos = {puntos}", font=("Arial",14, "bold"))
hideturtle()

# Condicion para terminar el juego (una tortuga ha salido)

def gameFinished(t1, t2, t3):
  t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
  t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h
  t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h
  isOutside = t1_outside or t2_outside or t3_outside
  return isOutside

t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

while gameFinished(t1, t2, t3) != True:
  t1.forward(7)
  t2.forward(7)
  t3.forward(7)
  sleep(0.1)
  end = time()
  tiempo = end - start
  print(round(tiempo))
  # cada 5 segundos le da 5 puntos
  if round(tiempo)%5 == 0:
    clear()
    puntos += 5
    write(f"Puntos = {puntos}", font=("Arial",14, "bold"))

penup()
goto(0,0)
pendown()
write("¡Perdiste!",  font=("Arial", 14, "bold"))

t1.clear()
t2.clear()
t3.clear()

'''
t1.penup()
t1.goto(-30, 0)
t1.write('¡Adiós!', font=('Arial', 16, 'bold'))


t2.penup()
t2.goto(-30, 0)
t2.write('¡Adiós!', font=('Arial', 16, 'bold'))


t3.penup()
t3.goto(-30, 0)
t3.write('¡Adiós!', font=('Arial', 16, 'bold'))
'''

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

exitonclick()

# Extra: mostrar el marcador en la esquina

""" def ganar():
  puntos += 5

if tiempo == 20:
  ganar() """