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
a = int(input());
b = int(input());
c = int(input());
if (a < b and a < c) or (b > a and  b > c):
    print(b);
    print(a);
    print(c);

elif (b < a and b < c) or (c > a and  c > b):
    print(c);
    print(b);
    print(a);
elif (b < a and b < c) or (a > b and  a > c):
    print(a);
    print(b);
    print(c);
elif (c < a and c < b) or (a > c and  a > b):
    print(a);
    print(c);
    print(b);
elif (c < a and c < b) or (b > c and  b > a):
    print(b);
    print(c);
    print(a);
elif (a < b and a < c) or (c > a and c > b):
        print(c);
        print(a);
        print(b);
elif (a < b and a < c) or (c > a and c > b):
        print(c);
        print(a);
        print(b);
        # Задача 5пппп