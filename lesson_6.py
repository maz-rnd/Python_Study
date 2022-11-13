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
