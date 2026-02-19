# Clase que maneja todo lo relacionado con el color de pluma, fondo e interfaz
from turtle import *

t = Turtle()
scr = t.getscreen()

# crear una función que te permita elegir el color
def SetColor():
   print("Ingresa un código de color en formato RGB ")
   R = int(input("R "))
   G = int(input("G "))
   B = int(input("B "))
   col = t.color((R,G,B))
   return color

def setRed():
  t.color('red')

def setGreen():
  t.color('green')


def setBlue():
  t.color('blue')

def setOrange():
    t.color('orange')


def setYellow():
    t.color('yellow')

def setLightBlue():
    t.color('light blue')

def setViolet():
    t.color('violet')


def background_black():
    scr.bgcolor('black')

def background_white():
    scr.bgcolor('white')
