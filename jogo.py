from random import randint
from time import sleep
nome = str(input("Digite seu nome..."))
print(f"olá {nome} vamos joga! ")
itens =  ('pedra, papel, tesoura')
#jogando com Karol
karol = randint (0,2)
#Apresentar as opção para o jogo
print ('''Opçães de jogo:
[0]Pedra
[1]Papel
[2]Tesolra''')

#Agora jogador faz sua jogada
jogador = str(input(f"{nome} qual é sua jogadar?"))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔÔ...')
sleep(2)
print ("*_*" *11)

#Mostrando oque cada um jogou...
print(f"Karol jogou: {itens[karol]}")
print(f"{nome} jogou: {itens[nome]}" )
print("*_*"*11)

if karol == 0: #Karol jogou Pedra
    if jogador == 0:
        print('EMPATE')
    
    elif jogador ==1:
        print (f"{nome} VENCEU")
    
    elif jogador ==2:
        print('Karol venceu')

elif karol == 1: #Karol jogou Papel
    if jogador ==0:
        print('KAROL VENCEU')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print(F"{nome} VENCEU")

elif karol == 2:#Karol jogou Tesoura
       if jogador ==0:
        print(F"{nome} VENCEU")
    elif jogador ==1:
        print('Karol venceu')
    elif jogador ==2:
        print('EMPATE')

    
