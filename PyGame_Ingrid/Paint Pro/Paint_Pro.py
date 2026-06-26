from turtle import *

# usamos clases auxiliares definidas en archivos aparte
from clase_dibujo import *
from clase_colores import *

t = Turtle()
scr = t.getscreen()

# por ahora solamente muestra el menú pero aún no se puede dibujar

#función para dibujar un cuadrado de un color dado
def draw_square(color):
    ti.pendown()
    ti.color('gray',color)
    ti.begin_fill()
    for i in range(4):
        ti.forward(40)
        ti.left(90)
    ti.end_fill()
    ti.penup()


# una función para dibujar una etiqueta con un color dado y una sangría dada
# (la sangría permite no establecer nuevas coordenadas para la letra, sino alejarse del elemento para el que se hace la etiqueta)
def draw_symbol(symbol,indent):    
    ti.forward(indent)
    ti.pendown()
    ti.color('gray')
    ti.write(symbol, font=('Arial', 12, 'normal'))  
    ti.penup()


def circle_t(size):
    ti.pendown()
    ti.begin_fill()
    ti.color('gray')
    ti.circle(size)
    ti.end_fill()
    ti.penup()


ti = Turtle()
ti.penup()
ti.speed(0)


# elementos para el fondo
indent = -20
ti.goto(-200,80)
draw_symbol('Fondo:',5)
ti.goto(-200,30)
draw_square('black')
draw_symbol('N',-20)
ti.goto(-200,-20)
draw_square('white')
draw_symbol('D',-20)

# elementos de la paleta
y = 180
indent = 42
ti.goto(-190,y)
draw_square('red')
draw_symbol('R',indent)
ti.goto(-130,y)
draw_square('orange')
draw_symbol('O',indent)
ti.goto(-70,y)
draw_square('yellow')
draw_symbol('Y',indent)
ti.goto(-10,y)
draw_square('green')
draw_symbol('G',indent)
ti.goto(50,y)
draw_square('light blue')
draw_symbol('L',indent)
ti.goto(110,y)
draw_square('blue')
draw_symbol('B',indent)
ti.goto(170,y)
draw_square('violet')
draw_symbol('V',indent)


# elementos de grosor de la pluma
x = 200
y = 150
indent = 30
ti.goto(x,140)
circle_t(5)
draw_symbol('1',indent)
ti.goto(x,100)
circle_t(10)
draw_symbol('2',indent)
ti.goto(x,53)
circle_t(15)
draw_symbol('3',indent)
ti.goto(x,0)
circle_t(20)
draw_symbol('4',indent)
ti.goto(x,-60)
circle_t(25)
draw_symbol('5',indent)


#print("Muévete arriba, abajo, derecha, izquierda con las flechas del teclado.")

ti.ht()

scr = t.getscreen()

# establecer las funciones de las teclas

scr.onscreenclick(move)
scr.onkey(setRed,'r')
scr.onkey(setGreen,'g')
scr.onkey(setBlue,'b')
scr.onkey(setOrange,'o')
scr.onkey(setYellow,'y')
scr.onkey(setLightBlue,'l')
scr.onkey(setViolet,'v')


scr.onkey(setWidth_1,'1')
scr.onkey(setWidth_2,'2')
scr.onkey(setWidth_3,'3')
scr.onkey(setWidth_4,'4')
scr.onkey(setWidth_5,'5')


scr.onkey(stepUp,'Up')
scr.onkey(stepDown,'Down')
scr.onkey(stepLeft,'Left')
scr.onkey(stepRight,'Right')


scr.onkey(startFill,'f')
scr.onkey(endFill,'e')


scr.onkey(background_black,'n')
scr.onkey(background_white,'d')
 
scr.listen()
