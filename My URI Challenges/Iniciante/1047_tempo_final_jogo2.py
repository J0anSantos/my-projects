def inicializa():
    tempo = list(map(int, input().split()))
    return tempo[0], tempo[1], tempo[2], tempo[3]

def verifica_tempo(hora1, minuto1, hora2, minuto2):
    if(hora1 == hora2):
        horas = 24
        if(minuto1 == minuto2):
            minutos = 0
        elif(minuto1 > minuto2):
            minutos = minuto1 - minuto2
            minutos = 60 - minutos
            horas -= 1
    elif(hora1 > hora2):
        horas = 24 - hora1
        horas += hora2
        if(minuto1 == minuto2):
            minutos = 0
        elif(minuto1 > minuto2):
            horas -= 1
            minutos = minuto1 - minuto2
            minutos = 60 - minutos
        else:
            minutos = minuto2 - minuto1
    else:
        horas = hora2 - hora1
        if(minuto1 == minuto2):
            minutos = 0
        elif(minuto1 > minuto2):
            horas -= 1
            minutos = minuto1 - minuto2
            minutos = 60 - minutos
        else:
            minutos = minuto2 - minuto1

    return horas, minutos


def main():
    hora1, minuto1, hora2, minuto2 = inicializa()
    if hora1 is not None:
        horas, minutos = verifica_tempo(hora1, minuto1, hora2, minuto2)
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

main()