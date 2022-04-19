# 高阶函数


# map
from functools import reduce


def f(x):
    return x * x


# map 函数的返回值是 Iterator
print('map(f, [1, 2, 3, 4]): ', list(map(f, [1, 2, 3, 4])))

print('\n')


# reduce
def add(x, y):
    return x + y


print('reduce(add, [1, 2, 3, 4, 5]): ', reduce(add, [1, 2, 3, 4, 5]))

print('\n')


# filter

def is_odd(x):
    return x % 2 == 1


print('filter(is_odd, [1, 2, 3, 4, 5, 6]): ',
      list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

print('\n')

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']


def normalize(name):
    n = ''

    for i, v in enumerate(name):
        if (i == 0):
            n = str.upper(name[i])
        else:
            n += str.lower(name[i])

    return n


print("练习1-输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']: \n")
print('练习1-执行：', list(map(normalize, ['adam', 'LISA', 'barT'])))

print('\n')


# 练习2
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

print('练习2-请编写一个prod()函数，可以接受一个list并利用reduce()求积：\n')


def prod(x, y):
    return x * y


print('练习2-执行：', reduce(prod, [1, 2, 3, 4, 5]))

print('\n')
