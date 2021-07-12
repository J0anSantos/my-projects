def recursive_lim(limite, posicao):
    if(posicao > limite):
        pass
    else:
        res = posicao ** 2
        print(f'{posicao}^2 = {res}')
        posicao += 2
        recursive_lim(limite, posicao)

def main():
    limite = int(input())
    recursive_lim(limite, 2)

main()