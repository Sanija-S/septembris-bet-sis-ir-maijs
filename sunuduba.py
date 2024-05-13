# sunubuda

import turtle


t=turtle.Turtle()
def kvadrats():
 for _ in range(4):
    t.color("pink") 
    t.begin_fill() 
    t.forward(200)
    t.left(90)
    t.end_fill()

def aplis():
    t.color("black") 
    t.penup()
    t.goto (100,30)
    t.pendown()
    t.begin_fill() 
    t.circle(80) # priekš circle vajag importēt apli
    t.end_fill()





def tristuris():
    t.color("pink") # kontūrkrāsa = pildijuma krāsa
    t.penup()
    t.goto (0,200)
    t.pendown()
    t.begin_fill() # sāksim aizpildit
    for _ in range(3): # taka tas ir trijsturis atkartosim 3 reizes
      t.forward(200)
      t.left(120) 
    t.end_fill()

t.speed(0)


kvadrats()
aplis() # secība kurā izsaukts ir vienaada ar sito lietinu secibu
tristuris()
turtle.done()