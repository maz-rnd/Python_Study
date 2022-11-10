# Task 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input()
# text = text.split()
# new_text = ''
# for i in text:
#     if 'abc' not in i:
#         new_text += i + ' '
# print(new_text)
# ==========================================

# text = input()
# text = text.split()
# new_text = filter(lambda x: 'abc' not in x, text)
# print(new_text)

# ***************************************************************

# Task 2
#
# def encode(s):
#     encoding = ""  # сохраняет выходную строку
#     i = 0
#     while i < len(s):
#         # подсчитывает количество вхождений символа в индексе `i`
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
#         # добавляет к результату текущий символ и его количество
#         encoding += str(count) + s[i]
#         i = i + 1
#     return encoding


# if __name__ == '__main__':
#     s = 'ABBCCCD'
#     print(encode(s))
# Нужно разобраться с кодом пожалуйста
