
#EXERCICIO 1
def cont(c):
    for i in range(c,-1,-1):
        if i == 0:
            print('zero!')
        else:
            print(i)
        
    return

cont(9)




#EXERCICIO 2 
def nums(a):
    soma = 0
    for i in range(len(a)):
        soma += a[i]
    return soma

lista = [0, 14, 52, 11, 18, 10]
print(nums(a=lista))


#EXERCICIO 3    
def lines(txt):
    count = 0
    for i in txt:
        if i == '\n':
            count += count
    return count

with open('.\\00 - Programas\\bd.txt', encoding='utf-8') as f:
    print(lines(f.read()))


    




