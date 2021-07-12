def calcula_media(notas):
    P1, P2, P3 = 2, 3, 5
    res = (P1 * notas[0] + P2 * notas[1] + P3 * notas[2])/(P1 + P2 + P3)
    return res

def main():
    N = int(input())
    for i in range(N):
        notas = list(map(float, input().split()))
        resultado = calcula_media(notas)
        print(f'{resultado:.1f}')

main()