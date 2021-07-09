def inicializa():
    numeros = list(map(int, input().split()))
    return numeros[0], numeros[1]

def verifica_multiplicidade(numero1, numero2):
    if (numero1 % numero2 == 0) or (numero2 % numero1 == 0):
        return True
    else:
        return False

def main():
    numero1, numero2 = inicializa()
    resultado = verifica_multiplicidade(numero1, numero2)
    if resultado is True:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

main()