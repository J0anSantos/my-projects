def main():
    numeros = list()
    for i in range(100):
        n = int(input())
        numeros.append(n)

    maior_valor = numeros[0]
    indice = 0

    for i in range(len(numeros)):
        if numeros[i] > maior_valor:
            maior_valor = numeros[i]
            indice = i
    
    indice += 1
    
    print(maior_valor)
    print(indice)

main()