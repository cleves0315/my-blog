# 第六天

- 类和实例
  - 定义：声明一个对象，并实例化
  - 使用：class Student(object);
  - 使用：xiaoming = Student()
- 定义初始化函数
  - 定义：类似构造函数
  - 使用：在类内部声明一个 ** init ** 名字的函数
- 设置访问限制
  - 定义：设置之后，实例化的对象无法直接访问该属性/方法
  - 使用：用双下划线开头命名（\_\_）
- 继承和多态
  - 定义：顾名思义
  - 使用：class Student(object)
  - 使用：class Ming(Student)
  - 校验关系：isinstance(xx, Student)
- 获取对象信息
  - 使用：dir(xiaoming) 返回该实力所有属性方法
- 使用 slots
  - 定义：限制实例对象更改的属性
  - 使用：class Student(object)
  - 使用： ——slots—— == ('name', 'age')
- @property
  - 定义：类似重写类的 get、set 方法
  - 使用：定义与属性同名的方法，并在上方申明@property
  - 如果只申明@property 则表示只读，需要再申明@[key].setter 表示可编辑
