def mostra_tabuada(numero):
    for i in range(1, 11):
        res = i * numero
        print(f'{i} x {numero} = {res}')

def main():
    numero = int(input())
    mostra_tabuada(numero)

main()