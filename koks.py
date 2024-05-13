import turtle
pen=turtle.Turtle()



def zari(br, angle):
    if br>5:
        pen.foward(br)
        pen.right(angle)
        zari(br-15, angle)
        pen.left(2*angle)
        zari(br-15, angle)
        pen.right(angle)
        pen.backward(br)

    


def koks(tr, angle):
    pen.left(90)
    pen.penup()
    pen.backward(tr)
    pen.pendown()
    pen.color("pink")
    pen.foward(tr)
    pen.color("red")
    zari(tr,angle)

pen.speed(1)

koks(100,30)
turtle.done()
