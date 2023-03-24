from turtle import Turtle, Screen
from posicaoinicial2 import posicoes
import random

corrida_comecou = False
screen = Screen()
screen.setup(width=500, height=400)
usuario = screen.textinput(title="Faça sua aposta!", prompt="Qual tartaruga irá vencer? Digite uma cor: ")
colors = ["red", "green", "yellow", "purple", "pink", "orange"]
todas_tartarugas = []

tartaruga1 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga1)
tartaruga1.color(colors[0])
tartaruga2 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga2)
tartaruga2.color(colors[1])
tartaruga3 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga3)
tartaruga3.color(colors[2])
tartaruga4 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga4)
tartaruga4.color(colors[3])
tartaruga5 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga5)
tartaruga5.color(colors[4])
tartaruga6 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga6)
tartaruga6.color(colors[5])
posicoes(tartaruga1, tartaruga2, tartaruga3, tartaruga4, tartaruga5, tartaruga6)

if usuario:
    corrida_comecou = True

while corrida_comecou:
    for t in todas_tartarugas:
        if t.xcor() > 230:
            corrida_comecou = False
            ganhou_color = t.pencolor()
            if ganhou_color == usuario:
                print(f'Parabéns a sua tartaruga {ganhou_color} venceu a corrida!')
            else:
                print(f'Poxa, você perdeu! A tartaruga vencedora é {ganhou_color}!')





        distancia = random.randint(0, 10)
        t.forward(distancia)


screen.exitonclick()

