def recursive_x(x, caminho):
    if caminho == 6:
        pass
    else:
        print(x)
        x += 2
        caminho += 1
        recursive_x(x, caminho)

def main():
    x = int(input())
    if(x % 2 == 0):
        x += 1
    recursive_x(x, 0)


main()