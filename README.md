# 这是一份 Python 初学者自用的面试题练习

> **原题链接** - [https://zhuanlan.zhihu.com/p/54430650?utm_id=0](https://zhuanlan.zhihu.com/p/54430650?utm_id=0)

## **001.** 一行代码实现 1-100 之和

> 利用 `sum()` 函数求和

```python
>>> a = sum(range(1,101))
>>> a
5050
```

## **002.** 如何在一个函数内部修改全局变量

> 利用 `global` 在函数声明，修改全局变量

```python
>>> a = 5
>>> def fn():
        global a
        a = 4

>>> fn()
>>> print(a)
4
```

## **003.** 列出 5 个 Python 标准库

> `os` 提供了不少与操作系统相关联的函数  
> `sys` 通常用于命令行参数  
> `re` 正则匹配  
> `math` 数学运算  
> `datetime` 处理日期时间

## **004.** 字典如何删除键和合并两个字典

> `del` 和 `update` 方法

```python
>>> dic = {"name":"zs", "age":18}
>>> del dic["name"]
>>> dic
{'age':18}
>>> dic2 = {"name":"1s"}
>>> dic.update(dic2)
>>> dic
{'age':18, 'name':"1s"}
```

## **005.** 谈下 Python 的 GIL

> GIL 是 python 的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行 python 程序的时候会霸占 python 解释器（加了一把锁即 GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。  
多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个 python 解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大。

## **006.** Python 实现列表去重的方法

> 先通过集合去重，在转列表

```python
>>> lis = [11, 12, 13, 12, 15, 16, 13]
>>> a = set(lis)
>>> a
{11, 12, 13, 15, 16}
>>> [x for x in a]
[11, 12, 13, 15, 16]
```

## **007.** `fun(*args,**kwargs)` 中的 `*args`, `**kwargs` 是什么意思？

> 在 Python 中，`*args` 和 `**kwargs` 都是特殊的语法，它们代表函数参数中的“可变参数”和“关键字参数”。  
> `*args` 表示把传递给函数的所有不带关键字的参数放在一个元组 args 中，然后传递给函数。例如：

```python
def my_function(*args):
    for arg in args:
        print(arg)

my_function('Hello', 'World', 2023)  # 输出: Hello World 2023
```

> `**kwargs` 则表示把传递给函数的所有带关键字的参数放在一个字典kwargs中，然后传递给函数。例如：

```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_function(name='Alice', age=25, location='New York')  # 输出: name = Alice, age = 25, location = New York
```

> 当一个函数同时具有 `*args` 和 `**kwargs` 参数时，通常这两个参数放在函数参数列表的最后一个，例如：

```python
def my_function(arg1, arg2, *args, **kwargs):
    print(arg1, arg2)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_function('hello', 'world', 'how', 'are', 'you', name='Alice', age=25, location='New York')
```

> 以上代码输出：`hello world how are you` 和 `name = Alice, age = 25, location = New York`。

## **008.** Python2 和 Python3 的 `range(100)` 的区别

> Python2 返回列表，Python3 返回迭代器，节约内存

## **009.** 一句话解释什么样的语言能够用装饰器？

> 函数可以作为参数传递的语言，可以使用装饰器

## **010.** Python 内建数据类型有哪些

> `int` 整型  
> `bool` 布尔型  
> `str` 字符串  
> `list` 列表  
> `tuple` 元组  
> `dict` 字典

## **011.** 简述面向对象中 `__new__` 和 `__init__` 区别

> `__init__` 是初始化方法，创建对象后，就立刻被默认调用了，可接收参数，如:

```python
class Bike:

    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def move(self):
        print('车会跑')

# 创建对象
BM = Bike(2, 'green')

print(f'车的颜色为 {BM.color}')
print(f'车轮数量为 {BM.wheelNum}')
```

1. `__new__` 至少要有一个参数 `cls` ，代表当前类，此参数在实例化时由Python解释器自动识别

2. `__new__` 必须要有返回值，返回实例化出来的实例，这点在自己实现 `__new__` 时要特别注意，可以 `return` 父类（通过 `super` (当前类名, `cls`)）`__new__` 出来的实例，或者直接是 `object` 的 `__new__` 出来的实例

3. `__init__` 有一个参数 `self`，就是这个 `__new__` 返回的实例，`__init__` 在 `__new__` 的基础上可以完成一些其它初始化的动作，`__init__` 不需要返回值

4. 如果 `__new__` 创建的是当前类的实例，会自动调用 `__init__` 函数，通过 `return` 语句里面调用的 `__new__` 函数的第一个参数是 `cls` 来保证是当前类实例，如果是其他类的类名；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的 `__init__` 函数，也不会调用其他类的 `__init__` 函数。

```python
class A(object):

    def __init__(self):
        print('这是 init 方法', self)

    def __new__(cls):
        print('')

# 创建对象
BM = Bike(2, 'green')

print(f'车的颜色为 {BM.color}')
print(f'车轮数量为 {BM.wheelNum}')
```
