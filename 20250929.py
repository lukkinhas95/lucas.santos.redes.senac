#idade = int (input("Quantos anos você tem?: "))
#if idade > 18:
#        print("Você pode entrar")
#else:
#        print("Vou chamar a polícia!")

#usuario1 = input("Digite seu usuário: ")
#senha1 = input("Digite sua senha: ")
#usuario2 = input("Digite seu usuário")
#senha2 = input("insira sua senha")
#
#if usuario1 or usuario2 == terry or aluno
#    print("Usuario autorizado")
#else: 
#    print("Usuário não autorizado")


#user1 = {
#    "usuario": "admin",
#    "senha": "123"
#}
#estudante = {
#    "usuario": "estudante",
#    "senha": "123"
#}

#user = input("Qual o seu usuário? ")
#senha = input("Qual a sua senha? ")
#hora = 0
                                                                                               
#if user1["usuario"] == user and user1["senha"] == senha:
#    print("Voce está liberado!")
#elif estudante["usuario"] == user and estudante["senha"] == senha:
#    hora = int(input("Qual é a gora de agora?: "))
#    if hora >= 8 and hora <= 18:
#        print("Voce está liberado")
#    else:
#        print("Não pode utilizar fora do horario")
#else:
#    print("Voce não está liberado")


#Maquina de café com while
#graos = 5

#while graos > 0:
#    print("Café pronto!")
#    graos -= 1
#    resposta = input("Quer mais café? (s/n): ")
#    if resposta.lower() == "n":
#        break
#    print("Máquina desligada.")


#crie um programa que conte de 0 a 59 segundos, simulando um relogio.
#import time 
#for i in range (1,60):
#    time.sleep(1)
#    print(i)

#import time
#segundo = 60
#while segundo > 0:
#    print(f "{segundo} segundos")
#    segundo -= 1 
#    time.sleep(1)


#import random
#num = random.randint(1,1)
#numero = input ("Digite um número: ")
#if numero == num:
#while num == numero:
#    print("Você ganhou uma rifa")
#else:
#    print("continue")

import random
num = random.randint(1, 300)
while True:
    numero = int(input("Digite um número entre 1 e 300: "))
    if numero == num:
        print("Você ganhou uma rifa")
        break
    else:
        print("Tente novamente")