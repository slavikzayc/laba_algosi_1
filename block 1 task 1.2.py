print('Введите число a и b')
a,b=map(int,input().split())        #Вход двух чисел a и b в одной строке
if a in range(-10**9,10**9+1) and b in range(-10**9,10**9+1):   #Проверка диапазона
    print(a+b**2)
else:
    print('Числа в недопустимом диапазоне')
