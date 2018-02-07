#
#     a= int(input());
# b= int(input());
# if b!=0:
#     print( a/b);
# else:
#     print('Деление невозможно');
#     b= int(input('Введите ненулевое значение'));
#     if b == 0:
#         print('Вы не справились!');
#     else:
#         print(a / b);
# Задача про сон.
# A = int(input());
# B = int(input());
# H = int(input());
# if  ( A<=H<=B):
#      print('Это нормально');
# elif (H > B):
#          print('Пересып');
# else:
#      if (H<A):
#          print('Недосып');
# G= int(input());
# if (((G%4==0) and (G%100!=0)) or (G%400==0)):
#     print ('Високосный');
# else:
#     print('Обычный');

# Формула Герона
# a = int(input());
# b = int(input());
# c = int(input());
# p = (a + b + c) / 2;
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5;
# print(S);

# x= int(input());
# if (-15)<x<=12 or 14<x<17 or 19<=x:
#     print(True);
# else:
#     print(False);
#  задача 2
# one_namber = float(input())
# two_number = float(input())
# r = input()
# if two_number == 0 and (r == 'div' or r == 'mod' or r == '/'):
#     print('Деление на 0!')
# elif r == '+':
#     print(one_namber + two_number)
# elif r == '-':
#     print(one_namber - two_number)
# elif r == '/':
#     print(one_namber / two_number)
# elif r == 'mod':
#     print(one_namber % two_number)
# elif r == 'pow':
#     print(one_namber ** two_number)
# elif r == 'div':
#     print(one_namber // two_number)
# elif r == '*':
#     print(one_namber * two_number)

#  задача 3
# d = input();
# if d =='треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2;
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5;
#     print(S);
# if d == d =='круг':
#     r = int(input())
#     p= 3.14;
#     S = p* r**2;
#     print(S);
# if d == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     S = a*b;
#     print(S);
#  задача 4
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# if (a <= b and a <= c) and (b >= a and b >= c):
#     print(b)
#     print(a)
#     print(c)
# elif (a <= b and a <= c) and (c >= a and c >= b):
#     print(c)
#     print(a)
#     print(b)
# elif (b <= a and b <= c) and (c >= a and c >= b):
#     print(c)
#     print(b)
#     print(a)
# elif (b <= a and b <= c) and (a >= b and a >= c):
#     print(a)
#     print(b)
#     print(c)
# elif (c <= a and c <= b) and (a >= c and a >= b):
#     print(a)
#     print(c)
#     print(b)
# elif (c <= a and c <= b) and (b >= c and b >= a):
#     print(b)
#     print(c)
#     print(a)
#
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a > b > c:
#     print(a)
#     print(c)
#     print(b)
#
# if a > c > b:
#     print(a)
#     print(b)
#     print(c)
#
# if b > a > c:
#     print(b)
#     print(c)
#     print(a)
#
# if b > c > a:
#     print(b)
#     print(a)
#     print(c)
#
# if c > a > b:
#     print(c)
#     print(b)
#     print(a)
#
# if c > b > a:
#     print(c)
#     print(a)
#     print(b)
#  Задача 6
# a = int(input())
# if (a% 100!=11) and (a%10==1):
#     print (a, 'программист');
# elif ((not a % 100 == 12) and  (a% 100!=13) and  (a%100!=14)) and ((a%10==2) or (a%10==3) or (a%10==4)):
#     print(a, 'программиста');
# else:
#     print(a,'программистов')
# Задача 7
a = input();
sum1 = int(a[0])+int(a[1])+int(a[2]);
sum2= int(a[3])+int(a[4])+int(a[5]);
if sum1==sum2:
    print('Счастливый');
else:
    print('Обычный');