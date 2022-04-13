# 切片
arr = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('arr1[0:3]: ', arr[0:3])
print('arr[:3]: ', arr[:3])  # 等同上面

print('arr[1:3]: ', arr[1:3])
print('arr[-2:]', arr[-2:])
print('arr[-2:0]', arr[-2:0])
print('arr[:]', arr[:])  # 复制数组

# 第二个参数
print('arr[::2]', arr[::2])  # 间隔2个读取
print('arr[1:4:2]', arr[1:4:2])
