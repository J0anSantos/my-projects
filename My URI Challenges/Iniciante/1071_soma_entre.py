def calcula_impar(x, y):
    contador = 0
    while(x < y):
        contador += x
        x += 2
    return contador

def main():
    x = int(input())
    y = int(input())
    
    if(x == y):
        res = 0
    else:
        if (x < y):
            if(x % 2 == 0):
                x += 1
            else:
                x += 2
            res = calcula_impar(x, y)
        else:
            if(y % 2 == 0):
                y += 1
            else:
                y += 2
            res = calcula_impar(y, x)
    print(res)

main()