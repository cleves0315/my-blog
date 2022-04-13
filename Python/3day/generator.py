from collections.abc import Iterator

# 生成器
print('定义生成器: L = (x for x in range(1, 7))')
L = (x for x in range(1, 7))  # 用括号包裹就是 generator

print('next(L): ', next(L))
print('next(L): ', next(L))
print('next(L): ', next(L))

for x in L:
    print('for x in L: ', x)


print('\n')


# 用函数生成复杂算法的 generator
print('用函数生成复杂算法的 generator')


def createGenerator(num):
    n, a, b = 0, 0, 1

    while(n < num):
        yield b
        a, b = b, a + b
        n += 1


L = createGenerator(6)
print('createGenerator(6): ', next(L))
print('createGenerator(6): ', next(L))
print('createGenerator(6): ', next(L))
print('createGenerator(6): ', next(L))
print('createGenerator(6): ', next(L))

L = createGenerator(6)
for x in L:
    print('for createGenerator(6): ', x)

print('\n')


# 判断 Interator
print('判断 Interator: ')
print('isinstance([], Iterator): ', isinstance([], Iterator))
print('isinstance({}, Iterator): ', isinstance({}, Iterator))
print('isinstance('', Iterator): ', isinstance('', Iterator))
print('isinstance((x for x in range(1, 6)), Iterator): ',
      isinstance((x for x in range(1, 6)), Iterator))
print('isinstance(createGenerator(6), Iterator): ',
      isinstance(createGenerator(6), Iterator))

print('\n')


# Iterable 转 Iterator
print('Iterable 转 Iterator: ')
a = [1, 2, 3]
print('a: ', isinstance(a, Iterator))
b = iter(a)
print('b = iter(a)')
print('b: ', isinstance(b, Iterator))

print('\n')


# 练习：写一个杨辉三角
print('练习：写一个杨辉三角')


def generate(numRows):
    i = 0
    nums = []

    while i < numRows:
        arr = []
        n = 0
        j = i + 1

        while n < j:
            if (i - 1 >= 0 and n - 1 >= 0 and n < len(nums[i - 1])):
                arr.append(nums[i - 1][n - 1] + nums[i - 1][n])
            else:
                arr.append(1)
            n += 1

        yield arr
        nums.append(arr)
        i += 1

    # return nums


L = generate(6)
for row in L:
    print('generate(6): ', row)
