import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(t, linLen):
    if linLen > 0:
        t.forward(linLen)
        t.right(90)
        drawSpiral(t, linLen-5)

drawSpiral(myTurtle, 100)
myWin.exitonclick()