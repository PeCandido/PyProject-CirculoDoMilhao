# ENTRADA
num_pessoas = int(input("Insira O Número De Pessoas: "))  # Quantidade de pessoas na roda
x_pessoa_eliminada = int(input("Insira a x-ésima Pessoa Eliminada: ")) # x-ésima pessoa eliminada
roda = []

# PROCESSAMENTO
i = 1
while i <= num_pessoas:
    roda.append(i)
    i += 1

mudar = "Não Apagar"
numero_eliminados = 0
while numero_eliminados != len(roda)-1:
    i = 0
    while i < len(roda):
        if roda[i] != 0:
            if mudar == "Apagar":
                numero_eliminados += 1
                if numero_eliminados == x_pessoa_eliminada:
                    x_esimo = roda[i]   
                roda[i] = 0
                mudar = "Não Apagar"
            else:
                mudar = "Apagar"
        i += 1 

i = 0
while i < len(roda):
    if roda[i] != 0:
        vencedor = roda[i]
    i += 1

# SAÍDA  
print(f"Eliminação {x_pessoa_eliminada}: {x_esimo}") # X-éniso eliminado
print(f"Ganhador: {vencedor}") # Vencedor 
