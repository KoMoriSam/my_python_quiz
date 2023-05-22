# python 中生成随机整数、随机小数、0--1之间小数方法
# 随机整数 - random.randint(a,b), 生成区间内的整数
# 随机小数 - 习惯用 numpy 库，利用 np.random.randn(5) 生成5个随机小数
# 0~1随机小数 - random.random(), 括号中不传参

import random, numpy

integer = random.randint(0,100)
decimal_1 = numpy.random.randn(5)
decimal_2 = random.random()

print(f'生成的 0-100 内的整数为 {integer}')
print(f'生成的随机小数为 {decimal_1}')
print(f'生成的大于0小于1的随机小数为 {decimal_2}')
