from random import *


n = input('Выбирай Камень, Ножницы, Бумага:')
comp = ['Камень','Ножницы','Бумага']
value = choice(comp)
print(value)



if n == 'Камень' and value == 'Ножницы':
    print('You win')

elif n == 'Бумага' and value == 'Камень':
    print('You win')

elif n == 'Ножницы' and value == 'Бумага':
    print('You win')

elif value == 'Ножницы' and n == 'Бумага':
    print('comp win')

elif value == 'Бумага' and n == 'Камень':
    print('comp win')

elif value == 'Камень' and n == 'Ножницы':
     print('comp win')

elif n == value:
    print('Draw')

else:
    print('ERROR')

