# kohas sniegavirs
# kvartalas strukturus- vienadsanu trijsturis, kur katra mala tiek pievienots trijsturis bezgaligi


import turtle

def zimet_k(b, order, size): # mainigie kas darbojas funkcija iekšienē
  if order==0: # ja order ir vienads ar 0 tad parvirzam tik liels cik size
    b.foward(size)
  else:
    for angle in [60,-120,60,0]: #konstrukcija kas zīmē sniegparsliņu
        zimet_k(b, order-1, size/3)
        b.left(angle)

pen= turtle.Turtle()# izveidojam objektu kas būs objektss ka zimulis



pen.speed(1)

pen.penup()# paceļas zimulis virs lapas
pen.goto(-150,100)
pen.pendown() # pen noliekas uz leju

turtle.done()

# sakts zimesanu
for _ in range(3):
  zimet_k(pen,4,300)
  pen.right(120)

