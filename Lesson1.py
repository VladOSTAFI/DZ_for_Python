def funcName(x):
    arr = []
    for value in x:
        arr.append(x[value] * 2)
    return arr


l = {'key': 30, 'key2': 10}
print (funcName(l))

print('-----------------------------')

def exer2(x, y):
    print("Hello, %s, you'r %d y.o" % (x, y))

exer2('Vasia', 19)

print('-----------------------------')

def fibo(n):
    first = 0
    second = 1
    for i in range(n):
        first, second = second, first + second
        print(i)
    return first


print(fibo(6))

print('-----------------------------')

#sort array of words by numbers of vowels
def exer4(arr):
    for i in arr:
        if type(i) != str:
            arr.remove(i)
    for i in arr:
        if type(i) != str:
            arr.remove(i)

    return sorted(arr, key=lambda s: t(s))


def t(s):
    c = s.lower().count('a') + s.lower().count('e') + s.lower().count('i') + s.lower().count('o') + s.lower().count('u') + s.lower().count('y')
    return c


list_of_word = ['HellO', 'world', 1, True, 1.5, 'ipsum', 'dolor', 2.2, 'set', 'amet', 'aaaa']
print(exer4(list_of_word))



