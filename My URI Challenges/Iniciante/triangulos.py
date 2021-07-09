import math

def inicializa_triangulo():
    lados = list(map(float, input().split()))
    return lados[0], lados[1], lados[2]

def verifica_triangulo(A, B, C):
    if (A < B + C) and (A > B - C) and (B < A + C) and (B > A - C) and (C < A + B) and (C > A - B):
        return True
    else:
        return False

def main():
    lado1, lado2, lado3 = inicializa_triangulo()
    resultado = verifica_triangulo(lado1, lado2, lado3)
    if resultado is True:
        perimetro = lado1 + lado2 + lado3
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((lado1 + lado2) * lado3) / 2
        print(f"Area = {area:.1f}")

main()