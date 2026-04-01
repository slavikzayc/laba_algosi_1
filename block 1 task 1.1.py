print('Введите число a и b')
a,b=map(int,input().split())            #Вход двух чисел a и b в одной строке
if -10**9<=a<=10**9 and -10**9<=b<=10**9:
    print(a+b)
else:
    print('Ошибка')
