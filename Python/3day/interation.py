# list
from collections.abc import Iterable

for val in [1, 2, 3]:
    print('for val in [1, 2, 3]: ', val)

for x, y, z in [(1, 1, 1), (2, 4, 6), (3, 6, 9)]:
    print('x y z in [(1, 1, 1), (2, 4, 6), (3, 6, 9)]: ', x, y, z)

print('\n==============\n')

# dict
obj = {'name': 'xiaoming', 'age': 12}
for key in obj:
    print('for key in obj: ', key)
for val in obj.values():
    print('for val in obj.values(): ', val)

print('\n==============\n')

# list in key, val
for key, val in enumerate(['a', 'b', 'c']):
    print('for key, val in enumerate([1, 2, 3]): ', key, val)

for key, val in obj.items():
    print('for key, val in obj.items(): ', key, val)

print('\n==============\n')

# 判断是否可迭代
print('isinstance("abc", Iterable): ', isinstance('abc', Iterable))
print('isinstance(123, Iterable): ', isinstance(123, Iterable))
print('isinstance((1,2,3), Iterable): ', isinstance((1, 2, 3), Iterable))
print('isinstance({name: "name"}, Iterable): ',
      isinstance({'name': 'name'}, Iterable))

arr = [2, 4, 6, 3, 4, 1, 7, 0, 4, 342, 54]


# test: 从一个列表列查询最大/最小值
max = 0
min = 999999
for val in arr:
    if val > max:
        max = val
    if val < min:
        min = val

print('(min, max): ', (min, max))
