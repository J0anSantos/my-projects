def inicializa():
    horas = list(map(int, input().split()))
    return horas[0], horas[1]

def calcula_horas(hora1, hora2):
    if(hora1 == hora2):
        return 24
    else:
        if(hora1 < hora2):
            return hora2 - hora1
        else:
            tempo = 24 - hora1
            tempo += hora2
        return tempo

def main():
    hora1, hora2 = inicializa()
    total = calcula_horas(hora1, hora2)
    print(f'O JOGO DUROU {total} HORA(S)')

main()