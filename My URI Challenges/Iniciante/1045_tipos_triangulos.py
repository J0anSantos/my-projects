def inicializa_triangulo():
    lados = list(map(float, input().split()))
    lados.sort(reverse=True)
    return lados[0], lados[1], lados[2]

def operacoes(lado1, lado2, lado3):
    if (lado1 >= lado2 + lado3):
        print('NAO FORMA TRIANGULO')
    else:
        if ((lado1 ** 2) == (lado2 ** 2) + (lado3 ** 2)):
            print('TRIANGULO RETANGULO')
        if ((lado1 ** 2) > (lado2 ** 2) + (lado3 ** 2)):
            print('TRIANGULO OBTUSANGULO')
        if ((lado1 ** 2) < (lado2 ** 2) + (lado3 ** 2)):
            print('TRIANGULO ACUTANGULO')
        if (lado1 == lado2 == lado3):
            print('TRIANGULO EQUILATERO')
        elif (lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
            print('TRIANGULO ISOSCELES')

def main():
    lado1, lado2, lado3 = inicializa_triangulo()
    operacoes(lado1, lado2, lado3)
main()