def calcula_aumento(salario):
    if(salario > 0 and salario <= 400):
        percentual = 15
        salario_novo = salario * 1.15
        diferenca = salario_novo - salario
    elif(salario > 400 and salario <= 800):
        percentual = 12
        salario_novo = salario * 1.12
        diferenca = salario_novo - salario
    elif(salario > 800 and salario <= 1200):
        percentual = 10
        salario_novo = salario * 1.10
        diferenca = salario_novo - salario
    elif(salario > 1200 and salario <= 2000):
        percentual = 7
        salario_novo = salario * 1.07
        diferenca = salario_novo - salario
    elif(salario > 2000):
        percentual = 4
        salario_novo = salario * 1.04
        diferenca = salario_novo - salario

    return salario_novo, percentual, diferenca

def main():
    salario = float(input())
    ajuste, percentual, diferenca = calcula_aumento(salario)
    print(f'Novo salario: {ajuste:.2f}\nReajuste ganho: {diferenca:.2f}\nEm percentual: {percentual} %')

main()