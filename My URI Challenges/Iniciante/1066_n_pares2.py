def verifica_pares():
    contador_pares = 0
    contador_negativos = 0
    contador_impar = 0
    contador_positivo = 0

    for i in range(5):
        numero = int(input())
        if numero < 0:
            contador_negativos += 1
        elif numero > 0:
            contador_positivo += 1
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impar += 1
    print(f'{contador_pares} valor(es) par(es)\n{contador_impar} valor(es) impar(es)\n{contador_positivo} valor(es) positivo(s)\n{contador_negativos} valor(es) negativo(s)')

def main():
    verifica_pares()

main()