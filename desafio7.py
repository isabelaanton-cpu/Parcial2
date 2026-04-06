# Solicita o capital inicial (valor principal)
capital = float(input("Digite o capital inicial (R$): ")) 
# Solicita a taxa de juros em porcentagem (ex: 5 para 5%)
taxa = float(input("Digite a taxa de juros anual (%): ")) 
# Solicita o tempo de aplicação em anos
tempo = float(input("Digite o tempo da aplicação (anos): ")) 
# Calcula o valor dos juros: J = C * i * t (taxa dividida por 100)
juros = capital * (taxa / 100) * tempo 
# Calcula o montante final somando o capital inicial e os juros
montante = capital + juros 
# Exibe os juros e o valor total final formatados
print(f"Total de juros: R$ {juros:.2f}") 
print(f"Montante final: R$ {montante:.2f}")
