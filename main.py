import turtle
import keyboard
import time
tis = turtle.Turtle()
tis.shape('turtle')
color1 = 'green'

while True:
    if keyboard.is_pressed("w"):
        tis.forward(10)
        time.sleep(0.1)
    elif keyboard.is_pressed("r"):
        tis.penup()
    elif keyboard.is_pressed("f"):
        tis.pendown()
    elif keyboard.is_pressed("s"):
        tis.backward(10)
        time.sleep(0.1)
    elif keyboard.is_pressed("d"):
        tis.right(90)
        time.sleep(0.1)
    elif keyboard.is_pressed("a"):
        tis.left(90)
        time.sleep(0.1)
    elif keyboard.is_pressed("q"):
        break


turtle.done()
# pip3 install keyboard
