#**Exercício 1: Calculadora Simples
#**Crie um programa que leia dois números e uma operação (`+`, `-`, `*`, `/`) e exiba o resultado.

def main():
    try:
        numero1 = float(input("Digite o primeiro número: ").strip())
        numero2 = float(input("Digite o segundo número: ").strip())
    except ValueError:
        print("Entrada inválida: digite números válidos.")
        return

    opcao = input("Operação (+, -, *, /): ").strip()
    if opcao not in ("+", "-", "*", "/"):
        print("Operação inválida.")
        return

    match opcao:
        case "+":
            res = numero1 + numero2
        case "-":
            res = numero1 - numero2
        case "*":
            res = numero1 * numero2
        case "/":
            if numero2 == 0:
                print("Erro: divisão por zero.")
                return
            res = numero1 / numero2

    # Formata resultado sem ponto desnecessário quando é inteiro
    if isinstance(res, float) and res.is_integer():
        print(f"Resultado: {int(res)}")
    else:
        print(f"Resultado: {res}")

if __name__ == "__main__":
    main()
# ...existing code...