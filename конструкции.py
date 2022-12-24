while True:
    s = input("Введите да, если хотите вйти из цикла: ")
    if s == "да":# вечный цикл с выходом по break
        break
print("Все комбинации для двухзначного числа")
for x in range(2):
   for y in range(2): # двойной пребор из диапазона 2 значений (0,1) в дмумерном массиве или подбор двух параметров
        print(str(x)+str(y))

a=int(input("итак если вы введете не 2, и вы увидете сообщение: "))  
if a != 2:
    print("Вы ввели не два")
       
flag=False  
arr = [1,4,3,2,5,6]
print("Если в цикле есть цифра 3, то изменится значение флага: flag = False")
for i in range(len(arr)):
    if arr[i] == 3:    
        flag=True
print("она есть, значит: flag = True")
x = 3
y = 2
z = 5
print("x = 3, y = 2, z = 5")
if ((y<=x) or not(z))==False: 
    print("Условие (y<=x) or not(z))==False выполнено")
else:
    print("Услвоие (y<=x) or not(z))==False не выполнено")# условие лжи
if ((y<=x ) or not(z)): 
    print("Условие ((y<=x ) or not(z)) выполнено")
else:
    print("Услвоие ((y<=x ) or not(z)) не выполнено")# условие лжи
    
num = int(input("Введите число, которое будет проверно на четность и взяа цела часть от деления на 2: "))
#if num == num%2:
    
