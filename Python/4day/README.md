# 第四天

- 高阶函数
- map
  - 作用：与js的map相似，按传入的函数返回新的数组
  - 使用：map(fn, [1, 2, 3])
  - 注意：返回值是 Iterator
- reduce
  - 作用：与js的reduce相似，按传入的函数返回新的数组
  - 使用：reduce(fn, [1, 2, 3, 4])
- filter
  - 作用：与js的filter相似，按传入的函数过滤元素并返回新数组
  - 使用：filter(fn, [1, 2, 3, 4])
- sorted
  - 作用：与js的sort相似，对数组进行排序
  - 使用：sorted([5, 2, 1, 6])
  - 第二个参数：sorted([5, 2, 1, 6], key=abs)会对应到每个元素上执行传入的函数
  - 第三个参数：sorted([5, 2, 1, 6], key=abs, reverse=True)是否反转