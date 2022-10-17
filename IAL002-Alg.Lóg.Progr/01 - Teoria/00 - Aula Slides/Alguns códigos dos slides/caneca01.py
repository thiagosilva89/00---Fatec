import urllib.request
import antigravity
#pagina = urllib.request.urlopen(
 #        'http://beans.itcarlow.ie/prices.html') 
 
pagina = urllib.request.urlopen('https://www.ime.usp.br/~pf/')  
 
texto = pagina.read().decode('utf8') 
print (texto)

