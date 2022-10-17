""" 
s = float(input("Digite o Salário - "))
#aumento
p = (int(input("Digite o Reajuste em % - "))/100)

p = s * p
#print

print("########################################")
print("#### Salario Inicial... - ", s ,"#######")
print("#### Aumento Real...... - ", p ,"######")

print("########################################")

print(f"#### Total Salario .... - {p + s:.2f}  ####")
print("########################################")
 """
 
 
 
import datetime as dt
from workadays import workdays as wd

from datetime import date
from pandas.tseries import holiday
import holidays


print(dir(holiday))

feriados = holidays.Brazil()
for feriado in feriados['2022-01-01': '2022-12-31']:
    print(feriado)

d1 = dt.date(2022, 7, 9)
print('É feriado? ', wd.is_holiday(d1, country='BR', years=range(2021, 2022)))

d = date.today().weekday()
if d < 5:
    print("dia semana")  
else:
    print("final de semana")