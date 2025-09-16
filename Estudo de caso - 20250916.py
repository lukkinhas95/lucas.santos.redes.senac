#Estudo de caso Sistema de Controle de Alarme com Portas Lógicas

#Resolver o Nível 1 (só fumaça).

f = input ("Há fumaça?")

if f == "sim":
    print("Alarme Ativado")
else:
    print("Alarme não ativo")

#Expandir para o Nível 2 (fumaça OU botão + chave).

b = input("Há fumaça?")
c = input("Chave ativada?")

if b and c == "sim":
   print("Alarme Ativo")
else:
    print("Alarme não ativo")

### Nível 3 — Três Condições Agora incluir o **movimento em área restrita (M)**.

f = input("Há fumaça?")
b = input("O botão está ativo?")
c = input("A chave está ativa?")
m = input("Há movimento?")

if f == "sim":
     print("Alarme ativo")
elif b and c == "sim":
     print("Alarme ativo")
elif m == "sim":
    print("Alarme ativo")
else:
    print("Alarme não ativo")   
