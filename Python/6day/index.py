# 类和实例
from time import process_time_ns


print('===================类和实例\n')

class Student(object):
  pass

ming = Student()
ming.name = 'xiaoming'

print('ming.name: ', ming.name)
print('\n')


# 定义构造函数
print('===================定义构造函数\n')

class Student(object):
  name = 'Student'

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_info(self):
    print('ming.get_info: ', self.name, self.age)

ming = Student('xiaoming', 12)
ming.get_info()
print('\n')

# 设置访问限制
print('===================设置访问限制\n')

class Student(object):
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def get_name(self):
    return self.__name

ming = Student('xiaoming', 12)

print('ming.get_age(): ', ming.get_age())
print('ming.get_name(): ', ming.get_name())
print('\n')


# 继承和多态
print('===================继承和多态\n')

class Animal(object):
  def run(self):
    print('Animal is running...')

class Dog(Animal):
  def eat(self):
    print('Dog is eating...')


huang = Dog()

huang.run()
huang.eat()

print('isinstance(huang, Dog): ', isinstance(huang, Dog))
print('isinstance(huang, Animal): ', isinstance(huang, Animal))
print('isinstance(huang, object): ', isinstance(huang, object))

print('\n')


# 获取对象信息
print('===================获取对象信息\n')

print('dir(huang): ', dir(huang)) # 打印所有属性



# 使用__slots__

class Student(object):
  __slots__ = ('name', 'age')

hong = Student()
hong.name = 'xiaohong'
hong.age = 12
# hong.hobby = '跳舞' 将会报错
print('\n')


# 使用@property

class Student(object):

  @property
  def name(self):
      return self._name # 要加下划线
  
  @name.setter
  def name(self, value):
      self._name = value # 要加下划线

s = Student()
s.score = 'xiaoming'
print('s.score: ', s.score)
print('\n')

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
  def __init__(self) -> None:
      self._resolution = 'resolution'

  @property
  def width(self):
    return self._width
  @width.setter
  def width(self, value):
    self._width = value

  @property
  def height(self):
    return self._height
  @height.setter
  def height(self, value):
    self._height = value

  @property
  def resolution(self):
    return self._resolution

a = Screen()
print('练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：')
print('a.resolution: ', a.resolution)
a.width = 100
print('a.width = 100')
a.height = 100
print('a.height = 100')
print('a: ', a.width)
print('a: ', a.height)