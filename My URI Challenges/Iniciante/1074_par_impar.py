def verifica_numeros(N):
    lista = list()
    for i in range(N):
        txt = ''
        X = int(input())
        if (X % 2 == 0 and X != 0):
            txt += 'EVEN '
        else:
            if(X != 0):
                txt += 'ODD '
        if (X == 0):
            txt += 'NULL'
        elif(X > 0):
            txt += 'POSITIVE'
        else:
            txt += 'NEGATIVE'
        lista.append(txt)

    for i in range(len(lista)):
        print(lista[i])


def main():
    N = int(input())
    verifica_numeros(N)

main()