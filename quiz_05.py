# 026. 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"

import re

a = 'not 404 found 张三 99 深圳'

list = a.split(' ')
print(list)

res = re.findall('\d+|[a-zA-Z]+', a)
for i in res:
    if i in list:
        list.remove(i)
new_str = ' '.join(list)
print(res)
print(new_str)
