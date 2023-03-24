# pergunat quem está realizando a operação
nome_Op = input("Favor informe seu nome: ")
# informe quanto o cliente paga no sistema.
valor_Cli = int(input("Quanto o cliente paga no sistema?"))
#Quantos cliente a  empresa possui
cli = int(input("Quantos clientes ele possue? "))
# Quanto cada cliente paga
Valor_Pag = int(input("Qual o valor base do honorarios pagos ao cliente? "))

# Soma os valores totais di cliente por 12 meses
Soma = cli * Valor_Pag 
valor_Ano = (Soma * 12)
# calculo de abatiemento com o sistema
valor_Cust =  Soma - valor_Cli

print("\n\nOlá ",nome_Op,", o valor que o cliente paga no sistema é: ""R$ {:,.2f}""\n\nO valor total bruto por por clientes é: ""R$ {:,.2f}""\n\nO valo total bruto em 12 meses é: ""R$ {:,.2f}""".format(valor_Cli, Soma, valor_Ano))
print("\n\nO valor de ganhos bruto em um mês, fora o sistema é {:,.2f}".format(valor_Cust))