""" 
LISTA 3""" """
EXERCICIO 1
Faça um programa que peça uma nota, 
entre zero e dez. Mostre uma mensagem caso o 
valor seja inválido e continue pedindo até que o 
usuário informe um valor válido.
print("\n\n")
print("-"*30)
n1 = float(input("Inseri o valor da nota : \t"))
print("-"*30)

while n1 not in range(0, 11):
    n1 = float(input("Inseri o valor da nota : \t"))

print("-"*30)
print("\n")

print(f"Valor da nota inserido {n1:.2f}")
print("\n\n")"""


#EXERCICIO 2
#Faça um programa que leia um nome de usuário 
#e a sua senha e não aceite a senha igual ao 
# nome do usuário, mostrando uma mensagem de erro 
# e voltando a pedir as informações.

""" print("\n\n")
print("-"*30)
u = input("Inserir o nome de usuário : \t")
p = input("Inserir o senha do usuário : \t")
print("-"*30)
print("\n\n")


while u == p:
    print("ERRO! Nome de usuário e senhas iguais. Favor inserir novamente. \n")
    
    print("\n\n")
    print("-"*30)
    u = input("Inserir o nome de usuário : \t")
    p = input("Inserir o senha do usuário : \t")
    print("\n\n")
    print("-"*30)

print("\n\n")
print("-"*30)
print(f"Usuário {u} cadastrado com sucesso. ")
print("-"*30)
print("\n\n") """



#EXERCICIO 4
#Supondo que a população de um país A seja da ordem de 80000 
#habitantes com uma taxa anual de crescimento de 3% e que a 
# população de B seja 200000 habitantes com uma taxa de 
# crescimento de 1.5%. Faça um programa que calcule e 
# escreva o número de anos necessários para que a população 
# do país A ultrapasse ou iguale a população do país B, 
# mantidas as taxas de crescimento

""" p1 = 80000
txp1= 0.03
p2 = 200000
txp2 = 0.015
i = 0
while p1 < p2:
    p1 = p1 * txp1 + (p1)
    p2 = p2 * txp2 + (p2)
    i+=1

print("\n\n")
print("-"*60)
print(f"Total de anos necessários para que a população cidade \nA = 80000 taxa de crescimento = 3% seja maior que a cidade \nB = 200000 com taxa de 1,5% de crescimento é \n{i} anos. ")
print("-"*60)
print("\n\n") """

#EXERCICIO 5
#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
# Sua regra de formação é simples: os dois primeiros elementos são 1; 
# a partir de então, cada elemento é a soma dos dois anteriores. 
# Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. 
# F1 = 1, F2 = 1, F3 = 2, etc.

""" f = int(input("Inserir a quantidade de termos FIBONACCI : \t"))
t1 = 0
t2 = 1
t3 = 0
i = 0

print("\n\n")
print("-"*60)
while i != f:

    print(" ► {}".format(t3), end=" ")
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    
    i+=1

print("\n")
print("-"*60)
print("\n\n") """






""" 
#EXERCICIO 6
#Dados dois números inteiros positivos, 
# determinar o máximo divisor comum entre 
# eles usando o algoritmo de Euclides.
print("\n\n")
print("-"*60)
print(f"{' '*20}ALGORITIMO DE EUCLIDES{' '*20}")
print("-"*60)

#INICIANDO AS VARIAVEIS
a = 0
b = 0
c = 0
resto = 0
print("\n\n")
#LOOP AQUISIÇÃO DE DADOS
while a == 0 or b == 0:
    
    print("-"*60)
    if c == 1:
        print(" ERRRO → NUMERO DE A OU B NÃO PODE SER 0 \n")
"""

""" #VARIAVEIS DE CONTROLE
c = 1 # TRATATIVA PARA ERRO DE VALORES NULOS
a = int(input("Inserir o valor do numero A :\t"))
b = int(input("Inserir o valor do numero B :\t"))
na = a # VARIAVEL APOIO PARA IMPRESSÃO
nb = b # VARIAVEL APOIO PARA IMPRESSÃO
print("-"*60)
print("\n\n")

#ALGORITIMO DE EUCLIDES
while (a % b) != 0:
    resto = a % b
    a = b
    b = resto
    

print("\n")
print("-"*60)
print(f"mdc dos numeros A = {na} e B = {nb} é igual à ►►► {resto}")
print("-"*60)
print("\n\n") """