# GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение
# суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
#
# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов).
#
# Например, в строке "acggtgttat" процентное содержание символов G и C равно 410⋅100=40.0410⋅100=40.0,
# где 4 -- это количество символов G и C,  а 10 -- это длина строки.
#
# genome = str(input())
# c = len(genome)
# cnt=0
# for nucl in genome:
#   a=genome.upper().count('c'.upper())
#   b=genome.upper().count('g'.upper())
# cnt= a+b
# print((cnt / c) * 100)

# s= input()
# i=0
# j=1
# while i<j:
#     if s[i] != s[j]:
#      i+=1
#      j+=1
#
# genome = input()
# s = ""
# count = 1
# k = len(genome)
# for i in range(1, k):
#     if genome[i] == genome[i - 1]:
#         count += 1
# else:
#     s = s + genome[i - 1] + str(count)
#     count = 1
#     if i == k - 1:
#         s = s + genome[i] + str(count)
# print(s)
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,sep='',end='')
#     print()

# n= int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# for i in range(n-1):
#         sum-=int(input())
# print(sum)


# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия,
# который сжимает повторяющиеся символы в строке.
#
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
#
#
# s = input()
# last_sym = s[0]
# count = 1
# result = ''
# for i in range(1, len(s)):
#     if s[i] == last_sym:
#         count += 1
#     else:
#         result += last_sym + str(count)
#         last_sym = s[i]
#         count = 1
# result += last_sym + str(count)
# print(result)
