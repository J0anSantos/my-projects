def processamento(N):
    contador_C, contador_R, contador_S = 0, 0, 0
    for i in range(N):
        linha = input().split()
        total = int(linha[0])
        if(linha[1] == 'C'):
            contador_C += total
        elif(linha[1] == 'R'):
            contador_R += total
        elif(linha[1] == 'S'):
            contador_S += total
    cobaias = contador_S + contador_C + contador_R
    porcentagem_S = (contador_S * 100)/cobaias
    porcentagem_C = (contador_C * 100)/cobaias
    porcentagem_R = (contador_R * 100)/cobaias

    print(f'Total: {cobaias} cobaias\nTotal de coelhos: {contador_C}\nTotal de ratos: {contador_R}\nTotal de sapos: {contador_S}\nPercentual de coelhos: {porcentagem_C:.2f} %\nPercentual de ratos: {porcentagem_R:.2f} %\nPercentual de sapos: {porcentagem_S:.2f} %')

def main():
    N = int(input())
    processamento(N)

main()