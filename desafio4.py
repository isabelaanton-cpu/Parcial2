# Solicita dois números para a operação
n1 = float(input("Digite o primeiro número: ")) 
n2 = float(input("Digite o segundo número: ")) 
# Apresenta as opções de operação ao usuário
print("Operações: + (Soma), - (Subtração), * (Multiplicação), / (Divisão)") 
op = input("Escolha a operação desejada: ") 
# Verifica qual operação foi escolhida e realiza o cálculo correspondente
if op == "+": 
    print(f"Resultado: {n1 + n2}") 
elif op == "-": 
    print(f"Resultado: {n1 - n2}") 
elif op == "*": 
    print(f"Resultado: {n1 * n2}") 
elif op == "/": 
    # Verifica se o divisor não é zero para evitar erro matemático
    if n2 != 0: 
        print(f"Resultado: {n1 / n2}") 
    else: 
        print("Erro: Divisão por zero não permitida.") 
else: 
    # Caso o usuário digite um símbolo inválido
    print("Operação inválida.")
