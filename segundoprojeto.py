a = 5
b = 3
print(a+b)

# calculo para financiamento ou emprestimo
Renda=float(input('Renda Mensal: '))
Valor_Desejado=float(input('Qual valor desejado: '))
if Renda>=5000 and Valor_Desejado<=0.2*Renda:
    print('(Seu pedido foi Aprovado)')
else:
    print('(Seu pedido não foi Aprovado)')    
