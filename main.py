from turtle import Turtle, Screen
from posiçãoinicial import posinicial
import random


corrida_comecou = False
screen = Screen()
screen.title("Corrida")
# tamanho do meu ecrã
screen.setup(width=500, height=400)
# aparecerá uma caixa de texto (input)
usuario = screen.textinput(title="Façam valer a aposta!", prompt="Qual tartaruga vai ganhar a corrida? Digite uma cor: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
todas_tartarugas =  []


# criando minhas setas no ecrã e colocando a forma de tartaruga utilizando o atributo shape
tartaruga = Turtle(shape="turtle")
# adicionando minha tartaruga na lista todas_tartarugas
todas_tartarugas.append(tartaruga)
# adicionando cores aos meus objetos usando minha lista de cores
tartaruga.color(colors[0])
tartaruga2 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga2)
tartaruga2.color(colors[2])
tartaruga3 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga3)
tartaruga3.color(colors[1])
tartaruga4 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga4)
tartaruga4.color(colors[4])
tartaruga5 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga5)
tartaruga5.color(colors[5])
tartaruga6 = Turtle(shape="turtle")
todas_tartarugas.append(tartaruga6)
tartaruga6.color(colors[3])
posinicial(tartaruga, tartaruga2, tartaruga3, tartaruga4, tartaruga5, tartaruga6)


# se usuario digitar algo que seja, corrida começou
if usuario:
    corrida_comecou = True

# se corrida_começou = verdadeiro
while corrida_comecou:
    # Para cada tartargua in todas_tartarugas
    for t in todas_tartarugas:
        # Esta função é usada para retornar a coordenada x da tartaruga da posição atual da tartaruga. Não requer nenhum argumento.
        if t.xcor() > 230:
            # Se qualquer tartaruga ultrapassar 230 o corrida_começou se tornará false
            corrida_comecou = False
            # ganhou color recebe a cor da tartaruga t.pencolor()
            ganhou_color = t.pencolor()
            if ganhou_color == usuario:
                print(f'Parabéns a sua tartaruga {ganhou_color} ganhou a corrida!')
            else:
                print(f"Poxa, sua tartaruga não ganhou! A {ganhou_color} é a vencedora!")
        # cada tartaruga andara um valor aleatório gerado pela variável distancia que está usando o random.randint
        distancia = random.randint(0, 10)
        t.forward(distancia)

screen.exitonclick()