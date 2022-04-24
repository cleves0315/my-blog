# 闭包

# 函数返回值返回一个函数
from email.mime import base
import functools


def testFn():
  x = 1

  def fn():
    return x

  return fn

# 练习利用闭包返回一个计数器函数，每次调用它返回递增整数：
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5

print('练习: 利用闭包返回一个计数器函数，每次调用它返回递增整数：')

def createCounter():
  l = 0

  def counter():
    nonlocal l
    l = l + 1
    return l

  return counter

counterA = createCounter()
counterB = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
print(counterB(), counterB(), counterB(), counterB(), counterB())

print('\n')


# 匿名函数
print('匿名函数')

# 申明符 lambda
print('map(lambda x: x * x, [1, 3, 5, 7, 9]): ', list(map(lambda x: x * x, [1, 3, 5, 7, 9])))

# 赋值变量存储
a = lambda x: x * x
print('a(2): ', a(2))

print('\n')


# 练习
# 请用匿名函数改造下面的代码：

# def is_odd(n):
#    return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print('练习: 请用匿名函数改造下面的代码：')
print('# def is_odd(n):')
print('return n % 2 == 1')

print('L: ', L)


# 偏函数

# 定义：通过设定参数的默认值，可以降低函数调用的难度
int('10000', base=2)

def int2(n, base=2):
  return int(n, base)

print(int2('10000'))

int2 = functools.partial(int, base=2)
print(int2('10000'))
