##### LISTA DE EXERCICIOS 2 THIAGO CARVALHO DA SILVA ###
##
##
#####
##
##
# DEFINIÇÕES DOS LADOS DO TRIAGULO COM BASE NOS VALORES INPUTADAS.
##
##
##a = float(input("INSERIR O LADO A DO TRIANGULO :\t"))
##b = float(input("INSERIR O LADO B DO TRIANGULO :\t"))
##c = float(input("INSERIR O LADO C DO TRIANGULO :\t"))
##
##
##
# ANALISE DOS TRIÂNGULOS:
# if (a==b and b==c):
##    print("\nTRIANGO EQUILÁTERO - POSSUI TODOS OS LADOS IGUAIS")
##
# elif (a!=b and a!=c and b!=c):
##    print("\nTRIANGO ESCALENO - POSSUI TODOS OS LADOS DIFERENTE")
##
# else:
##    print("\nTRIANGO ISÓSCELES - POSSUI DOIS LADOS IGUAIS E UM DIFERENTE")
##

##
# EXERCICIO 2
# Determine se um ano é bissexto. Verifique no Google como fazer isso...
##
# IMPORTANDO BIBLIOTECA
##from calendar import isleap
##
##
# DEFININDO ANO COLETADO.
##ano = int(input("INFORME O ANO QUE SERÁ VERIFICADO :\t"))
##
##
##
# if isleap(ano):
##    print("ANO É BISSEXTO")
##
# else:
##    print("ANO É NÃO É BISSEXTO")


# EXERCICIO 3
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de  seu trabalho. Toda vez que ele traz um peso de peixes
# maior que o estabelecido pelo regulamento de pesca do  estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você  faça um programa que leia a variável peso
# (peso de peixes) e verifique se há excesso. Se houver, gravar na
# variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais  variáveis com o conteúdo ZERO.
##
##
##peso = int(input("VALOR EM KG DA PESCA..:\t"))
##limite = 50.00
##taxa = 4.00
##
##
##
# if peso > limite:
##    multa = taxa * (peso - limite)
##    print (f"\nPESO - {peso:.2f} KG\t LIMITE - {limite:.2f} KG\t EXECEDENTE - {peso - limite:.2f} KG\t MULTA - R$ {multa:.2f}")
# else:
##    print (f"\nPESO - {peso:.2f} KG\t LIMITE - {limite:.2f} KG\t EXECEDENTE - 00.00 KG\t MULTA - R$ 00.00")
##
##


# EXERCICIO 4.
# Faça um Programa que leia três números e mostre o maior deles.
##
##
# DEFINIÇÕES DOS LADOS DO TRIAGULO COM BASE NOS VALORES INPUTADAS.
##
##
##a = float(input("INSERIR O PRIMEIRO NÚMERO :\t"))
##b = float(input("INSERIR O SEGUNDO NÚMERO :\t"))
##c = float(input("INSERIR O TERCEIRO NÚMERO :\t"))
##
##
##
# ANALISE DOS VALORES:
# if (a>b and a>c):
##    print(f"\nMAIOR VALOR REGISTRADO É O A = {a:.2f}")
##
# elif (b>a and b>c):
##    print(f"\nMAIOR VALOR REGISTRADO É O B = {b:.2f}")
##
# elif (c>a and c>b):
##    print(f"\nMAIOR VALOR REGISTRADO É O C = {c:.2f}")
##
# else:
##    print("POSSUI IGUALDADE ENTRE OS NUMEROS")


# EXERCICIO 5.
# Faça um Programa que leia três números e mostre o maior e o menor deles.
##
##
##
##a = float(input("INSERIR O PRIMEIRO NÚMERO :\t"))
##b = float(input("INSERIR O SEGUNDO NÚMERO :\t"))
##c = float(input("INSERIR O TERCEIRO NÚMERO :\t"))
##
##
##
# ANALISE DOS VALORES:
# if (a>b and a>c):
##    print(f"\nMAIOR VALOR REGISTRADO É O A = {a:.2f}")
##
# elif (b>a and b>c):
##    print(f"\nMAIOR VALOR REGISTRADO É O B = {b:.2f}")
##
# elif (c>a and c>b):
##    print(f"\nMAIOR VALOR REGISTRADO É O C = {c:.2f}")
##
# else:
##    print("\nMAIOR VALOR POSSUI IGUALDADE ENTRE OS NUMEROS")
##
##
# ANALISE DOS VALORES:
# if (a<b and a<c):
##    print(f"\nMENOR VALOR REGISTRADO É O A = {a:.2f}")
##
# elif (b<a and b<c):
##    print(f"\nMENOR VALOR REGISTRADO É O B = {b:.2f}")
##
# elif (c<a and c<b):
##    print(f"\nMENOR VALOR REGISTRADO É O C = {c:.2f}")
##
# else:
##    print("MENOR VALOR POSSUI IGUALDADE ENTRE OS NUMEROS")


##
##
############################################################################################
############################################################################################
############################################################################################
##
##
# EXERCICIO 6.
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule  e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda,  8% para o INSS e 5% para o sindicato, faça um programa que nos dê o
# salário bruto, quanto pagou ao INSS,  quanto pagou ao sindicato e o salário líquido.
# Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os  descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$
##
##ir = 0.11
##inss = 0.08
##sind = 0.05
##
##salario  = float(input("DIGITE VALOR HORA DO SEU SALÁRIO: R$ "))
##tot_horas = int(input("DIGITE TOTAL DE HORAS TRABALHADS R$ "))
##
##sbruto = tot_horas * salario
##
##
# print("#############  SALARIO MÊS VIGENTE   #############\n")
##print(f"\n_________SALÁRIO BRUTO DO MES__________")
##
##
##print(f"\nSALÁRIO BRUTO DO MÊS..........:\t R$ {sbruto:.2f}\n")
##
# print(f"\n_________DESCONTOS_____________")
##
##print(f"\nIR............................:\t R$ -{sbruto*ir:.2f}")
##print(f"\nINSS..........................:\t R$ -{sbruto*inss:.2f}")
##print(f"\nSINDICATO.....................:\t R$ -{sbruto*sind:.2f}")
##
##print(f"\n_________SALÁRIO LIQUIDO FINAL__________")
##sliquido = sbruto - ((sbruto * ir) + (sbruto * inss) + (sbruto * sind))
##print(f"\nSALÁRIO LIQUIDO DO MÊS........:\t R$ {sliquido:.2f}\n")
##
##
##


# EXERCICIO 6.
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a  ser pintada. Considere que a cobertura da tinta é de 1 litro para
# cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem  compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas.


litro = float(18)
v_lata = float(80.00)
m = float(3.00)
area = float(input("DIGITE QUANTIDADE DE ÁREA A SER PINTADA EM METROS QUADRADOS :\t"))



#DEFINIÇÃO SE O NUMERO CALCULADO É SEM RESTO. 
tot_latas = area%(litro*m)

#CASO VALOR DA ÁREA SEJA MENOR QUE O VALOR DE UMA LATA. 
if area <= (litro*m):
    tot_latas = 1.00

#CASO VALOR SEJA EXATO
elif tot_latas == 0:
    tot_latas = area / (litro*m)

#CASO VALOR NÃO SEJA EXATO. 
else:
    tot_latas = (area // (litro*m))+1


## SAIDA DOS DADOS TRATADOS 
print("\n\n____________FECHAMENTO DO ORÇAMENTO DE TINTAS_________________")
print(f"\nÁREA A SER PINTADA ...................:\t {area:.2f} m²")
print(f"RENDIMENTO DE UMA LATA ...............:\t {m * litro:.2f} m²\n")

print("_____________________TOTAL DE LATAS__________________________")
print(f"\nTOTAL DE LATAS PARA PINTURA DE UMA ÁREA DE {area:.2f} M² É............: \t {tot_latas:.2f} LATAS DE TINTA\n")