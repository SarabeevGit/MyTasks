#Создание таблицы (n*n с наполнением через input()).
a=[[0,0,0],[0,0,0],[0,0,0]] #создание болванки
for i in range(3):
   for j in range(3):
       a[i][j]=int(input()) #наполняем данными через Enter
print(a) #выводим
