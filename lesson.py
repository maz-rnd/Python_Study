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
