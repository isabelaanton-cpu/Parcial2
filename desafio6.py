# Solicita a quantidade total de segundos ao usuário
total_segundos = int(input("Digite a quantidade de segundos: ")) 
# Calcula a quantidade de horas inteiras
horas = total_segundos // 3600 
# Calcula o resto dos segundos após extrair as horas
resto_segundos = total_segundos % 3600 
# Calcula a quantidade de minutos inteiros a partir do resto
minutos = resto_segundos // 60 
# O que sobrar da última divisão são os segundos finais
segundos_finais = resto_segundos % 60 
# Exibe o tempo formatado em horas, minutos e segundos
print(f"Tempo formatado: {horas}h {minutos}m {segundos_finais}s")
