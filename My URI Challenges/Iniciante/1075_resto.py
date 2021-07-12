def resto(inicio):
    for i in range(10001):
        if (i % inicio) == 2:
            print(i)    

def main():
    inicio = int(input())
    resto(inicio)

main()