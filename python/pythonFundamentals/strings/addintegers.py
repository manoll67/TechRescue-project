print('Plasse enter an integer value:')
x = input()
y = input('Please enter another integer value:')
num1 = int(x)
num2 = int(y)
sum = num1 + num2
print(num1, '+', num2, '=', sum)

x = input('Please enter an integer value: ')
y = input('Please enter another integer value: ')
num1 = int(x)
num2 = int(y)
print(num1, '+', num2, '=', num1 + num2)


num1 = int(input('Please enter an integer value: '))
num2 = int(input('Please enter another integer value: '))
print(num1, '+', num2, '=', num1 + num2)

num = int(float(input('Please enter a number: ')))
print(num)

num = round(float(input('Please enter a number: ')))
print(num)

#Функцията int не може да преобразува низа '3.4' в
#цяло число директно, въпреки че може да преобразува числото с плаваща запетая 3.4 в цяло число 3. 
# Следната интерактивна последователност демонстрира: 

#num = int(float(input('Please enter a number: ')))
 #Please enter a number: 3.4

#num = int(3.4)
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#TypeError: int() argument must be a string, a bytes-like object or a number, not 'float'

#num = int(float(input('Please enter a number: ')))
#Please enter a number: 3.4
#>>> num
#3

#>>> num = round(float(input('Please enter a number: ')))
#Please enter a number: 3.7
#>>> num
#4

print('Please enter an integer value: ', end='')
x = int(input())
print('Please enter another integer value: ', end='')
y = int(input())
print(x, '+', y, '=', x + y)
#Please enter an integer value: 21
#Please enter another integer value: 21
#21 + 21 = 42

print(end='Please enter an integer value: ')
x = int(input())
print(end='Please enter another integer value: ')
y = int(input())
print(x, '+', y, '=', x + y)
#Please enter an integer value: 21
#Please enter another integer value: 21
#21 + 21 = 42

print('Please enter an integer value:', end='\n')
x = int(input())
print('Please enter another integer value:', end='\n')
y = int(input())
print(x, '+', y, '=', x + y)
#Please enter an integer value:
#21
#Please enter another integer value:
#21
#21 + 21 = 42
