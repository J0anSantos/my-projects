def verifica_pares():
    contador = 0
    for i in range(5):
        numero = int(input())
        if numero % 2 == 0:
            contador += 1
    return contador

def main():
    quantidade = verifica_pares()
    print(f'{quantidade} valores pares')

main()