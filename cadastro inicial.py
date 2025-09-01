# Programa de cadastro de alunos e notas

aluno1 = "Laura Azevedo"
nota1_1 = 8.0
nota1_2 = 7.5
nota1_3 = 6.0

aluno2 = "João Pé de Feijão"
nota2_1 = 5.0
nota2_2 = 6.0
nota2_3 = 4.5

# Calculando médias
media1 = (nota1_1 + nota1_2 + nota1_3) / 3
media2 = (nota2_1 + nota2_2 + nota2_3) / 3

# Verificando aprovação (média mínima = 6.0)
situacao1 = "Aprovado" if media1 >= 6 else "Reprovado"
situacao2 = "Aprovado" if media2 >= 6 else "Reprovado"

# Gerando relatório
print("===== RELATÓRIO =====")
print(f"Aluno: {aluno1}")
print(f"Notas: {nota1_1}, {nota1_2}, {nota1_3}")
print(f"Média: {media1:.2f}")
print(f"Situação: {situacao1}")
print("----------------------")
print(f"Aluno: {aluno2}")
print(f"Notas: {nota2_1}, {nota2_2}, {nota2_3}")
print(f"Média: {media2:.2f}")
print(f"Situação: {situacao2}")
