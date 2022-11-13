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
# colors = ['red', 'green', 'yellow']
# data = open('some_file.txt', 'a')
# data.writelines(colors)
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# with open('some_file.txt', 'r') as data:
#     for line in data:
#         print(line)

# def some_string(sym, count):
#     return (sym*count)


# print(some_string('!', 5))
# a = (3, 4)
# print(a)
# print(a[0])
# c = {1, 2, 3, 4, 5, 6}
# d = c.copy()
# print(d)

# num = input()
# sum = 0
# for s in num:
#     if s.isdigit():
#         sum += int(s)
# print(sum)
#from random import random
# import random

# n = int(input('Enter number of list : '))
# ls = []
# for _ in range(n):
#     num = int(input())
#     ls.append(num)
# print(ls)
# random.shuffle(ls)
# print(ls)
# import time
# print(time.time())
# a = []
# n = int(input())
# for i in range(n):
#     a.append(input())
# f_num = input()
# if f_num in a:
#     print('YES')
# else:
#     print('NO')

# num = int(input('Enter amount of list : '))
# ls = []
# sum = 0
# for _ in range(num):
#     el = int(input())
#     ls.append(el)
# for i in range(1, num, 2):
#     sum += ls[i]
# print(ls)
# print(sum)

# *************************************************************

# a = list(map(int, input().split()))
# print(max(a), min(a))

# def num_translate(key, dictionary):
#     print(dictionary[key])


# d = {'one': 'один', 'two': 'два'}
# word = input('Write a word :')
# num_translate(word, d)

# some_str = input()
# some_str = some_str.split()
# maxx = int(some_str[0])
# minn = int(some_str[0])
# for i in some_str:
#     if int(i) > maxx:
#         maxx = int(i)
#     elif int(i) < minn:
#         minn = int(i)
# print(minn, maxx)


# def mult(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))


# calc(lambda x, y: x+y+2, 4, 5)

# list = []
# for i in range(1, 101):
#     if (i % 2 == 0):
#         list.append(i)
# print(list)
# def f(x):
#     return x**3


# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)
# 1 2 3 5 8 15 23 38

# path = 'file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# num = []

# while data != '':
#     space_pos = data.index(' ')
#     num.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]

# data = list(map(int, input().split()))
# print(data)

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)
# ==========================================================
# with open('Text.txt', 'r', encoding='utf-8') as data:
#     f = data.read().split(' ')
# for i in range(len(f) - 1):
#     if int(f[i]) + 1 != int(f[i + 1]):
#         print(int(f[i]) + 1)
# ==========================================================
# n = 8
# with open('Text.txt', 'r', encoding='utf-8') as k:
#     some_list = list(map(int, k.read().split()))
#     for i in range(n - 1):
#         if some_list[i] != some_list[i + 1] - 1:
#             print(some_list[i + 1] - 1)

# ==========================================================
# text = input()
# text = text.split()
# new_text = ''
# for i in text:
#     if 'abc' not in i:
#         new_text += i + ' '
# print(new_text)


# text = input()
# text = text.split()
# new_text = filter(lambda x: 'abc' not in x, text)
# print(new_text)
# ============================================================

# урок №6
def summ(ls):
    return sum(ls)


def sub(ls):
    res = ls[0]
    for i in ls[1:]:
        res -= i
    return res


def mult(ls):
    res = ls[0]
    for i in ls[1:]:
        res *= i
    return res


def div(ls):
    res = ls[0]
    for i in ls[1:]:
        res /= i
    return res


def app(txt):
    if '(' in txt:
        start = 0
        for i in range(len(txt)):
            if txt[i] == '(':
                start = i
        fin = start + txt[start:].index(')')
        tmp = txt[start+1:fin]
        result = app(tmp)
        return app(f'{txt[:start]}{result}{txt[fin+1:]}')
    sign = ''
    for s in '+-*/':
        if s in txt:
            sign = s
            break
    if sign == '':
        return int(txt)
    else:
        ls = list(map(app, txt.split(sign)))
        if sign == '*':
            return mult(ls)
        elif sign == '/':
            return div(ls)
        elif sign == '+':
            return summ(ls)
        elif sign == '-':
            return sub(ls)


print(app('11+7*4-4/2+3*7'))
print(app('11+7+3-2*4'))
