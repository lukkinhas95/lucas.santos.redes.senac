#Nível 1
#Pergunta: Com python: peça ao usuário que digite seu nome e imprima uma saudação simples.
#nome = input("Digite seu nome: ")
#print (nome)

#Pergunta: Solicite ao usuário que digite sua idade e exiba a mensagem "Você tem X anos".
#idade = input("Digite a sua idade: ")
#idade_calculo = int(idade)
#print(f"Daqui a cinco anos você terá {idade_calculo + 5}")

#Pergunta: Pergunte ao usuário qual é a sua cor favorita e mostre a resposta.
#cor = input("Digite sua cor favorita: ")
#print(cor)

#Nível 2
#Pergunta: Peça ao usuário dois números e armazene-os em variáveis. Em seguida, exiba a soma.

#n1 = float(input("Digite o primeiro número: \n"))
#n2 = float(input("Digite o segundo número: "))
#input (n1+n2)

#Pergunta: Solicite o nome e a idade do usuário, armazene em variáveis e mostre: "Nome: [nome], Idade: [idade]".
#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade"))
#print(f"Nome: [{nome}], Idade: [{idade}]")

#Pergunta: Peça ao usuário seu nome, idade e cidade. Armazene essas informações em um dicionário e exiba-o.

nome = input(" Digite o seu nome: ")
idade = float(input("Digite a sua idade: "))
cidade = input("Qual cidade você nasceu: ")
dic = {
    "O nome do cabra é": nome,
    "A idade do cabra é": idade,
    "O cabra nasceu em": cidade
}

lista = []
lista.append(dic)

print(lista)
