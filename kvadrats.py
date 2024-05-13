# kvadrats


import turtle 
import random
# izveidojam objektu , kas dos iespēju "zīmēt"
t=turtle.Turtle()

# zīmēsim kvadrātu...atkārtojumam veicam divas darbības

for _ in range(4): # burta vietā lieto zemsvitru, lai noraditu ka mums nac nepieciešams saglabāt vērtības "paslēptais zīmogs", konvnesija kas norada neplānotu i vērtību- 4 reizes notiek iterācija
    t.forward(100) # kursoru nosutam 100 solus uz prieksu(saoas kursors/turtle pa vidu?)
    t.right(90) #mainam virzienu un grādus


#zimejuma atrums(1-10, 0 visatrakais)
t.speed(1)

# ka izveidot funkciju lai mainitu krasu uz gadijuna panata
def mainit_krasu():
    krasas=["red",'blue', "green","yellow"]
    # japieskir krasa objektam
    t.color(random.choice(krasas))# jaimporte bibliotēka

#zimejums
for _ in range (36):
    for _ in range(4):
     t.forward(100)
     t.left(90)
    mainit_krasu()
    t.right(10) #pagriezisu peles kursoru par 10 grādiem
    
# aizveram zīmējuma logu
turtle.done()
