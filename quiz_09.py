# 044. a = "张明 98分"，用 re.sub，将 98 替换为 100

import re

a = '张明  98 分'
print(f'原始分 {a}')

result = re.sub(r'\d+', '100', a)

print(f'修改后 {result}')
