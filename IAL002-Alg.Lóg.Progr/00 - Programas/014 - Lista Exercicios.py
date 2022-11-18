#print ('x', end = ' ')
#print ('x', end = ' ')

#print (3 == 3.0)
#print (1//3)
#print (3 == '3')
#print ('x' != 'x')
#print (2/1)
#print (2//1)
#print (not False)
#print (not True)
#print (not 0)

#a = 5
#b = a + 7
#a = 10
#print (b)

#print (True and (False or not True))

""" print (type(0))

print (type(0.0))

print (type(3.14))

print (type('Py'))

print (type(True))

print (type(1/2))

print (type(1//2))

print (type(2//1))

print (type(3**3))

print (type(0==0))

print (type(3<0))

print (type(3!=3)) """

#print (type(str(int(3.14159265358979))))

""" a = 20
print (15-(a-15), end = ' ')
a = 10
print (15-(a-15), end = ' ') """

""" a = 12.75
print (a - int(a), end = ' ')
a = int((a - int(a))*100)
print (a)

a = 3
b = 4
a = a + b
b = a - b
a = a - b
print (a, b) """

#print (3 % 2)

#print (0 % 2)

#print (123%356254)

#print (type([1, 2]))

#print (type({1:2}))

#print (type([]))

""" a = 'abacate'
print ('e' in a, 'x' in a, end = ' ')
print ('ate' in a, end = ' ')
print ('' in a, end = ' ')
print ('eta' in a, end = ' ')
print ('eta' not in a) """

""" a = '0123456789'
print (a[0], a[3], a[-1], end = ' ')
print (a[0:3], a[3:6], a[6:9], end = ' ')
print (a[:3], a[7:], end = ' ')
print (a[:9:2], end = ' ')
print (a[::-1]) """

""" a = 5
b = 9
while a <= b:
    print ('X', end = ' ')
    if a % 2 == 0: print ('O', end = ' ')
    a = a + 1 """

""" a=1
while a % 7 != 0:
    if a % 2 == 0: print ('O', end = ' ')
    if a == 2: print ('X', end = ' ')
    a=a+1 """
    
""" repete = True
a=0
b=0
while repete:
    print ('O', end = ' ')
    a=a+5
    b=b+7
    if a + b >= 24:
        repete = False """
        
""" repete = True
a=0
b=0
while repete:
    print ('O', end = ' ')
    if a + b >= 24:
        repete = False
    a=a+5
    b=b+7 """
    
""" repete = True
a=0
b=0
while repete:
    print ('O', end = ' ')
    if a + b > 24:
        repete = False
    a=a+5
    b=b+7 """
    
""" a=0
while a < 3:
    while True:
        print ('X', end = ' ')
        break
    print ('O', end = ' ')
    a=a+1 """
    
    
""" a=1
while a < 3:
    while a < 3:
        print ('O', end = ' ')
a=a+1 """

""" a=1
while a < 3:
    if a % 2 == 0:
        b=1
        while b < 3:
            print ('X', end = ' ')
            b=b+1
    print ('O', end = ' ')
    a=a+1 """
    
""" a=1
while a < 3:
    b=1
    while b < 3:
        if a == 2:
            print ('X', end = ' ')
        print ('O', end = ' ')
        b=b+1
    print ('O', end = ' ') """
    
""" x = 'abacate'
while x:
    print (x, end = ' ')
    x = x[1:] """
    
""" x = 10
while x:
    x = x - 1
    if x % 2 != 0:
        continue
    print (x, end = ' ') """
    
""" while 1:
    nome = input('Nome:')
    if nome == 'fim': break
    print ('Bom dia ', nome) """
    
""" x = 'python'
achou = False
vogal = 'aeiou'
while x and not achou:
    if x[0] in vogal:
        print ('X', end = ' ')
        achou = True
    else:
        x = x[1:]
if not achou:
    print ('O', end = ' ') """
""" 
for x in ['a', 3.14, 7/2]:
    print (x, end = ' ') """
    
    
""" s = 0
for x in [7, 2, -2, 5]:
    s = s + x
print (s) """


""" p = 1
for x in [1, -1, 2, -2]: p = p * x
print (p) """

""" p = 1
for x in 'aeiou':
    print (x*3, end = ' ')   """
    
""" L = [1, 2, 3, 4, 5]
for x in range(len(L)): 
    L[x] += 1
print (L) """

""" for x in 'abc':
    for y in '012':
        print (x + y, end = ' ') """
        
""" L = [1, 7, 4, 12, -2]
x = L[0]
while True:
    L = L[1:]
    if not L:
        break
    if L[0] > x:
        x = L[0]
print (x) """


""" def f(a):
    a=a+5
    return a
b=0
f(b)
print (b, ',', end = '')
b = f(b)
print (b) """

""" def f(x):
    print ('x', end = '')
    if x <= 1:
        return 1
    else:
        return x + f(x-1)
    
    
print(f(4)) """


""" def comum(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

print(comum('azul', ['a','b'])) """


""" a = 'X'
def func( ):
    a = "O"
func( )
print (a) """

""" a = 'X'
def func( ):
    global a
    a = 'O'
func( )
print (a) """


""" def fat():
    n = 1
    f = 1
    while True:
        f = f * n
        yield f
        n = n + 1
a = fat()
for i in range(5):
    print (next(a), end = ' ') """
    
    
""" def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
a = fib()
for i in range(5):
    print (next(a), end = ' ') """