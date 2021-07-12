def recursive_x(x, caminho):
    if caminho > x:
        pass
    else:
        print(caminho)
        caminho += 2
        recursive_x(x, caminho)

def main():
    x = int(input())
    recursive_x(x, 1)

main()