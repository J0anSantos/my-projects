def verifica_intervalo(N):
    dentro = 0
    fora = 0
    for i in range(N):
        X = int(input())
        if (X >= 10 and X <= 20):
            dentro += 1
        else:
            fora += 1
    
    print(f'{dentro} in\n{fora} out')
def main():
    N = int(input())
    verifica_intervalo(N)

main()