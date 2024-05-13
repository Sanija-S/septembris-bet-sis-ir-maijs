
# trijsturis
import turtle
t=turtle.Turtle()
def tris_krasas():
    t.color("pink") # kontūrkrāsa = pildijuma krāsa
    t.begin_fill() # sāksim aizpildit
    for _ in range(3): # taka tas ir trijsturis atkartosim 3 reizes
      t.forward(100)
      t.right(120) # cik gradus pagrizisies
    t.end_fill()

t.speed(1)
tris_krasas()

turtle.done()