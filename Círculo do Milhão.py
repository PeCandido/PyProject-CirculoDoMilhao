#GABRIEL HERIQUE SC 3037851
#PEDRO CANDIDO SC 3037126

num_pessoas = int(input("Insira O Número De Pessoas: "))
x_pessoa_eliminada = int(input("Insira a x-ésima Pessoa Eliminada: "))
roda = []

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

print(f"Eliminação {x_pessoa_eliminada}: {x_esimo}")
print(f"Ganhador: {vencedor}")