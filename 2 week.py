# a= 5
# while a>0:
#     print(a, end='')
#     a-=1

# primer
# a=5
# while a<= 55:
#      print(a)
#      a+=2

# a=5
# while a <=55:
#     if a% 2 ==1:
#         print(a)
#     a +=1

# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)

# n = int(input())
# c = 1
# while c<=n:
#     print('*'* c )
#     c+=2

# n= int(input())
# stars = '*'
# while  len(stars)<= n:
#     print(stars)
#     stars +='*'

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# a = int(input())
# b= int(input())
# s=0
# i=a
# while i <=b:
#     s +=i
#     i+=1
# print(s)

# a= int(input())
# s=0
# i=a
# while i!=0:
#      a= int(input)
#      s += i;
#      i +=1;
# print(s)
# Задача 2
# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
#  n=1
# sum=0
# while n!=0:
#     n = int(input())
#     sum += n
# print(sum)

# Задача 3
# В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог.
# В команде биологов aa человек, а в команде информатиков — bb человек.
#
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование,
# при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки,
# нужно найти минимальное подходящее число.
#
# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа aa и bb,
# каждое число вводится на отдельной строке) и выводить наименьшее число dd, которое делится на оба этих числа без остатка.

# a = int(input())
# b = int(input())
# d=1
# while ( d % a !=0) or ( d % b !=0 ):
#      d += 1
# else:
#     print(d)

# while True:
#     i = int(input())
#     if i > 100:
#         break
#     if i <= 10:
#         continue
#     print(i)


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# for k in range(c, d + 1):
#     print("\t" + str(k), end='')
# print()
#
# for i in range(a, b + 1):
#     print(str(i) + "\t", end='')
#     for j in range(c, d + 1):
#         print(str(j * i) + "\t", end='')
#     print()


    # for k in range(d):
    #     print('\t', k * i, "\t")


    # n= int(input())
    # c=int(input())
    # a= int(input())
    # b=int(input())
    # for i in range(n, c+1):
    #     for j in range(a,b):
    #         for k in range(i,j):
    #             print(n, c , end='')
    #         print(a, b, end='')
    #     print(i*j)


#
# Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b][a;b], которые делятся на 33.
#
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12][−5;12].
# Всего чисел, делящихся на 33, на этом отрезке 66: −3,0,3,6,9,12−3,0,3,6,9,12. Их среднее арифметическое равно 4.54.5
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 33.
# b = (int(i) for i in input(). split())
# a = int(input())
# b= int(input())
# s=0
# c=0
# for i in range (a, b+1):
#     if i % 3==0:
#       c= c + i
#       s = s+1
# print(c/s)