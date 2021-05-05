"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    import turtle
    turtle.circle(end.x - start.x,360)
    end_fill()
    # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2): # una vuelta hace la mitad de un rectángulo; como una L
        forward(100) # base del rectángulo
        left(90) # giro de ángulo: 90°
        forward(50) # altura: avanza la mitad de su largo
        left(90) # giro de ángulo: 90°

    end_fill()

    # TODO


def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()
    # TODO

    
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        # saca, extrae el valor que tiene la var state en la llave "Shape"
        shape = state['shape']
        # crea un objeto de tipo vector con x,y y lo guarda en la var end
        end = vector(x, y)
        
        #el contenido de shape indica la función que se ejecutara
        shape(start, end)
        
        
    #reiniciar start con None - para indicar que lo siguiente es nuevo
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
# funcion que sirve para crear una ventana de ancho 420, alto 420
# los ultimos 2 argumentos indican - la posición de la esquina sup izq
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
