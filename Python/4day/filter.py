# 高阶函数2

# filter

from audioop import reverse


def is_odd(x):
    return x % 2 == 1


print('filter(is_odd, [1, 2, 3, 4, 5, 6]): ',
      list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

print('\n')


# sorted

print('sorted([34, -12, 3, -5, 67]): ', sorted([34, -12, 3, -5, 67]))

# 第二个参数，指定的函数会作用到每个元素上
print('sorted([34, -12, 3, -5, 67], key=abs): ', sorted([34, -12, 3, -5, 67], key=abs))

# 第三个参数，reverse=True开启倒序排列
print('sorted([34, -12, 3, -5, 67], key=abs, reverse=True): ', sorted([34, -12, 3, -5, 67], key=abs, reverse=True))

print("sorted(['a', 's', 'd', 'A', 'B']): ", sorted(['a', 's', 'd', 'A', 'B']))

print("sorted(['a', 's', 'd', 'A', 'B'], key=str.lower): ", sorted(['a', 's', 'd', 'A', 'B'], key=str.lower))

print('\n')

# 练习：请用sorted()对下述列表分别按名字排序：

print('练习：请用sorted()对下述列表分别按名字排序：')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def test(tup):
  return tup[0]

print('sorted(L, key=test): ', sorted(L, key=test))
