def verifica_imposto(valor):
    
    if(valor > 0 and valor <= 2000):
        total = None
    if(valor > 2000):
        valor_atualizado = valor - 2000 #2520
        if(valor_atualizado > 0 and valor_atualizado <= 1000):
            total = valor_atualizado * 0.08
            valor_atualizado = 0
        elif(valor_atualizado > 1000):
            total = 1000 * 0.08      
            valor_atualizado -= 1000 


        if(valor_atualizado > 0 and valor_atualizado <= 1500):
            total += valor_atualizado * 0.18 
            valor_atualizado = 0
        elif(valor_atualizado > 1500):
            total += 1500 * 0.18
            valor_atualizado -= 1500
        
        if(valor_atualizado > 0):
            total += valor_atualizado * 0.28
    return total

def main():
    valor = float(input())
    total = verifica_imposto(valor)
    if total is None:
        print('Isento')
    else:
        print(f'R$ {total:.2f}')

main()