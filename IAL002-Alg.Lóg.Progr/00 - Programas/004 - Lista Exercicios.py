################################################
###############  LISTA 4 #######################
################################################


################################################
############## EXERCICIO 1 #####################
# Sorteie 10 inteiros entre 1 e 100 para uma ###
# lista e descubra o maior e o menor valor  ####
# sem usar as funções max e min. ###############
################################################

#CARREGANDO DADOS PARA LISTA DE SORTEIO
import random 

#DEFININDO LISTA
lsort = []

#SORTEANDO DEZ ITENS NA LISTA.
for x in range(0, 10):
    lsort.append(random.randint(1,100))

print("\n"*3)
print("-"*80)
print("Lista sorteada 0 a 100. Dez Itens", lsort)
print("-"*80)
print("\n"*3)

minimo, minaux = 0, lsort[0]
maximo, maxaux = 0, 0

for x in range(len(lsort)):
    if maxaux < lsort[x]:
        maximo = lsort[x]
        maxaux = maximo
    if minaux > lsort[x]:
        minimo = lsort[x]
        minaux = minimo



print("-"*80)
print("MAIOR número da lista é : ", maximo,"\n")
print("Menor número da lista é : ", minimo)
print("-"*80)
print("\n"*3)



""" ################################################
############## EXERCICIO 2 #####################
# Sorteie 20 inteiros entre 1 e 100 numa lista.#
# Armazene os números pares na lista PAR e os ##
# números ímpares na lista IMPAR. Imprima as ###
# três listas.##################################
################################################

#CARREGANDO DADOS PARA LISTA DE SORTEIO
import random 

#DEFININDO LISTA
lsort = []

#SORTEANDO DEZ ITENS NA LISTA.
for x in range(0, 20):
    lsort.append(random.randint(1,100))

print("\n"*3)
print("-"*120)
print("Lista sorteada 0 a 100. Vinte Itens", lsort)
print("-"*120)
print("\n"*2)

listpar, listimpar = [], []

for x in range(len(lsort)):
    if (lsort[x]%2) == 0:
        listpar.append(lsort[x])
    else:
        listimpar.append(lsort[x])
    



print("-"*80)
print("Lista dos números PARES é : ", listpar,"\n")
print("Lista dos números IMPARES é : ", listimpar,)
print("-"*80)
print("\n"*3) """

  

##############################################################################################
############## EXERCICIO 3 ###################################################################
# . Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. ########
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos ##########
# elementos intercalados dos dois outros vetores. Imprima os três vetores. ###################
##############################################################################################
##############################################################################################



from random import randint

vetor1 = []
vetor2 = []
vetor3 = []

ctt = 10

for k in range(ctt):
  x = randint(1, 100)
  vetor1.append(x)
  vetor3.append(x)
  x = randint(1, 100)
  vetor2.append(x)
  vetor3.append(x)


print("-"*80)
print("Lista dos números do vetor 1: ", vetor1,"\n")
print("Lista dos números do vetor 2: ", vetor2,"\n")
print("Lista dos números do vetor 3: ", vetor3,)
print("-"*80)
print("\n"*3)



##############################################################################################
############## EXERCICIO 4 ###################################################################
# Seja o statement sobre diversidade: “The Python Software Foundation and the global Python###
# community welcome and encourage participation by everyone. Our community is based on #######
# mutual respect, tolerance, and encouragement, and we are working to help each other live up#
# to these principles. We want our community to be more diverse: whoever you are, and ########
# whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com #####
# split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras#
# “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres ########
# especiais e cuidado com maiúsculas e minúsculas. ###########################################
##############################################################################################


""" #IMPORTANDO BIBLIOTECA
import string

#TEXTO PROPOSTO
txt = '''"The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”'''.lower()

#RETIRANDO CARACTERES ESPECIAIS E COLOCANDO ESPAÇO
for i in string.punctuation:
  txt = txt.replace(i, ' ')

# DEFININDO FILTRO DA LISTA. 
resultado = []
for p in txt.split():
  if p[0] in 'python' or p[-1] in 'python':
    resultado.append(p)
    

print("\n"*3)
print("-"*80)
print("Lista de resultados é : ", resultado,)
print("-"*80)
print("\n"*3) """




##############################################################################################
############## EXERCICIO 5 ###################################################################
# Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras #######
# “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para ##
# minúsculas e de remover antes os caracteres especiais.. ####################################
##############################################################################################
""" 



txt = '''"The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”'''.lower()

import string
for c in string.punctuation:
  txt = txt.replace(c, ' ')
resultado = []

def liststring(palavra):
  for letra in palavra:
    if letra in 'python':
      return True
  return False


for p in txt.split():
  if liststring(p) and len(p) > 4:
    resultado.append(p)
    
print("\n"*3)
print("-"*80)
print("Lista de resultados é : ", resultado, "\n")
print ("Quantidade de elementos na lista ",len(resultado))
print("-"*80)
print("\n"*3)

 """