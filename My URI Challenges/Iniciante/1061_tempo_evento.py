def contabiliza_tempo(dia_i, dia_f, horas_i, horas_f, minutos_i, minutos_f, segundos_i, segundos_f):
    dias_total = dia_f - dia_i
    
    if (horas_f < horas_i):
        horas_total = 24 - horas_i
        horas_total += horas_f
        dias_total -= 1
    else:
        if(horas_f == horas_i):
            horas_total = 0
        else:
            horas_total = horas_f - horas_i
    
    if(minutos_f > minutos_i):
        minutos_total = minutos_f - minutos_i
    elif(minutos_i > minutos_f):
        minutos_total = minutos_i - minutos_f
        minutos_total = 60 - minutos_total
        if(horas_total == 0):
            dias_total -= 1
            horas_total = 23
        else:
            horas_total -= 1
    else:
        minutos_total = 0
    
    if(segundos_f > segundos_i):
        segundos_total = segundos_f - segundos_i
    elif(segundos_i > segundos_f):
        segundos_total = segundos_i - segundos_f
        segundos_total = 60 - segundos_total
        minutos_total -= 1
    else:
        segundos_total = 0

    print(f'{dias_total} dia(s)\n{horas_total} hora(s)\n{minutos_total} minuto(s)\n{segundos_total} segundo(s)')

def main():
    w1 = input().split()
    x1 = input().split()
    dia_i = int(w1[1])
    horas_i = int(x1[0])
    minutos_i = int(x1[2])
    segundos_i = int(x1[4])
    w2 = input().split()
    x2 = input().split()
    dia_f = int(w2[1])
    horas_f = int(x2[0])
    minutos_f = int(x2[2])
    segundos_f = int(x2[4])
    contabiliza_tempo(dia_i, dia_f, horas_i, horas_f, minutos_i, minutos_f, segundos_i, segundos_f)

main()