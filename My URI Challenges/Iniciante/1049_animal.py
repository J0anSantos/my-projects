def executa_animal():
    caracteristica1 = input()
    caracteristica2 = input()
    caracteristica3 = input()

    if(caracteristica1 == 'invertebrado'):
        if(caracteristica2 == 'inseto'):
            if(caracteristica3 == 'hematofago'):
                print('pulga')
            elif(caracteristica3 == 'herbivoro'):
                print('lagarta')
        elif(caracteristica2 == 'anelideo'):
            if(caracteristica3 == 'hematofago'):
                print('sanguessuga')
            elif(caracteristica3 == 'onivoro'):
                print('minhoca')
    elif(caracteristica1 == 'vertebrado'):
        if(caracteristica2 == 'ave'):
            if(caracteristica3 == 'carnivoro'):
                print('aguia')
            elif(caracteristica3 == 'onivoro'):
                print('pomba')
        elif(caracteristica2 == 'mamifero'):
            if(caracteristica3 == 'herbivoro'):
                print('vaca')
            elif(caracteristica3 == 'onivoro'):
                print('homem')



def main():
    executa_animal()

main()