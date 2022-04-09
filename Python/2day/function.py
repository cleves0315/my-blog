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
def set_name(name):
    return 'Your name is ' + name


print('set_name("xiaoming"): ', set_name('xiaoming'))


# Empty Function
def emptyFn():
    pass


print('emptyFn(): ', emptyFn())  # None
