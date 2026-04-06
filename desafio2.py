# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: ")) 
# Verifica se o resto da divisão por 2 é igual a zero
if numero % 2 == 0: 
    # Se o resto for zero, o número é par
    print("O número é par.") 
else: 
    # Caso contrário, o número é ímpar
    print("O número é ímpar.")
