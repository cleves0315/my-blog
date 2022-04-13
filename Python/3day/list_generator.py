# 列表生成器

# 使用range
print('使用range: ')

print('(range(1, 11)): ', (range(1, 11)))

print('\n')

# 列表生成器
print('列表生成器: ')

print('[x for x in range(1, 11)]: ', [x for x in range(1, 11)])

print('[x= + x for x in range(1, 11)]: ', ['x = ' + str(x)
      for x in range(1, 11)])

print('\n')

# 添加过滤条件
print('添加过滤条件:')

print('[x for x in range(1, 11) if x % 2 == 0]: ',
      [x for x in range(1, 11) if x % 2 == 0])  # 过滤条件不能加 else

print('\n')

# 添加筛选条件
print('添加筛选条件:')

print('[x if (x % 2 == 0) else -x for x in (range(1, 11))]: ',
      [x if (x % 2 == 0) else -x for x in (range(1, 11))])  # 筛选条件必须加 else

print('\n')


# 练习：
# 已知一个列表：L1 = ['Hello', 'World', 18, 'Apple', None]
# 输出：['hello', 'world', 'apple']

print('练习：')

L1 = ['Hello', 'World', 18, 'Apple', None]
print('[x for x in L1 if isinstance(x, str)]: ',
      [x for x in L1 if isinstance(x, str)])
