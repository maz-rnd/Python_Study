#lesson 1#
##############
# Задача №1
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# if a == b ** 2 or b == a ** 2:
#     print('yes!')
# else:
#     print('NO!')

# **********************************************************************

# Задача №2
# some_list = map(int, input('Insert numbers by space: ').split())
# max_num = max(some_list)
# print(max_num)
# /////////////////////////////////////
# number = int(input())
# max = number
# for i in range(0, 4):
#     number = int(input())
#     if number > max:
#         max = number
# print(max)
# ///////////////////////////
# some_list = []
# for i in range(5):
#     number = int(input())
#     some_list.append(number)
# maxx = some_list[0]
# for el in some_list:
#     if el > maxx:
#         maxx = el
# print(maxx)
# ///////////////////////////////
# print(max(map(int, input().split())))

# *****************************************************

# Задача №3
# a = int(input())
# for i in range(-a, a):
#     print(i, end=', ')
# print(a)
# ///////////////////////////////////////
# num = input()
# if '.' not in num:
#     print('No')
# else:
#     n = (float(num) * 10) % 10
#     print(int(n))
# ////////////////////////////////////////
# num = input()
# if '.' in num:
#     index_p = num.find('.')
#     print(num[index_p + 1])
# else:
#     print('NO')

# *********************************************************

# Задача№4
# n = int(input())
# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print('YES')
# else:
#     print('NO')

#lesson 2#
# n = int(input())
# a = []
# for i in range(n):
#     a.append((-3) ** i)
# print(*a, sep=', ')
##########
# n = int(input('Enter number: '))
# arr = []
# for i in range(1, n + 1):
#     arr.append(3 * i + 1)
# print(arr)
# ///////////////////////////////////////
# n = int(input())
# print('{', end='')
# for i in range(n + 1):
#     print(f'{i}:{3 * i + 1}', end=', ')
# print(f'{n}:{3*n+1}', end='}')
# //////////////////////////////////////
# s1 = input('Enter string 1: ')
# s2 = input('Enter string 2: ')
# print(s1.count(s2) or s2.count(s1))
# ///////////////////////////////////////
