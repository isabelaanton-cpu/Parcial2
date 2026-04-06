# Cria uma lista vazia para armazenar os nomes
nomes = [] 
# Inicia um laço de repetição que executa 5 vezes
for i in range(5): 
    # Solicita um nome ao usuário e o adiciona à lista
    nome = input(f"Digite o {i+1}º nome: ") 
    nomes.append(nome) 
# Exibe a frase inicial antes de listar os nomes
print("Os nomes digitados foram:") 
# Percorre a lista de nomes e imprime cada um individualmente
for n in nomes: 
    print(n)
