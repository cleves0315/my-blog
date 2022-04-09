names = ('xiaoming', 'xiaohong', 'xiaohuang')

# for
for name in names:
    print('names: ', name)

# range
a = list(range(5))
print('a: ', a)

# while
n = 0
while n < 100:
    n += 1

    if n == 3:
        continue
    elif n > 5:
        break
    print('while-n: ', n)
