# abs
print('==== abs() ====')

print('abs(123): ', abs(123))
print('abs(-123): ', abs(-123))
a = abs
print('a=abs => a(-123): ', a(-123))

print('==== abs() end ====\n')

# max、min
print('==== max()、min() ====')

print('max(1, 2, 3, 4, 5): ', max(1, 2, 3, 4, 5))
print('min(1, 2, 3, 4, 5): ', min(1, 2, 3, 4, 5))

print('==== max()、min() end ====\n')

# Switching data types
print('==== Switching data types ====')
print('int("123"): ', int('123'))
print('float("123.44"): ', float("123.44"))
print('str(123.44): ', str(123.44))
print('bool(1): ', bool(1))
print('bool(""): ', bool(''))

# Custom Function
print('==== Custom Function ====')


def set_name(name):
    return 'Your name is ' + name


print('set_name("xiaoming"): ', set_name('xiaoming'))
print('==== Custom Function end ====\n')

# Empty Function
print('==== Empty Function ====')


def emptyFn():
    pass


print('emptyFn(): ', emptyFn())  # None
print('==== Empty Function end ====\n')

# Arguments
print('==== Arguments ====')


def person(name, age, city='shanghai'):
    print('person(name, age, city = shanghai): ', name, age, city)


person('xiaoming', 12)


def calc(arr=[1, 2]):
    arr.append(0)
    print('calc(arr = [1, 2]): ', arr)


calc()
calc()  # 上次运行的数字0会累加


# 可变参数
def calc(*numbers):
    print('calc(*numbers): ', numbers)


print('calc(1, 2, 3, 4) => ')
calc(1, 2, 3, 4)

nums = (1, 2, 3, 4)
print('calc(*(1, 2, 3, 4)) =>')
calc(*nums)


# 关键字参数
def person(name, **people):
    print('person(**people): ', name, people)


person('xiaoming', age='123', city='shanghai')


# 命名关键字参数
def person(name, *, age=12, city):
    print('person(name, *, age, city): ', name, age, city)


person('xiaohong', city='beijing')


# 可变参数 & 关键字参数
def f1(*nums, **kw):
    print('f1(*nums, **kw): ', nums, kw)


nums = (1, 2, 3)
kw = {'name': 'name', 'age': 2}
f1(*nums, **kw)
