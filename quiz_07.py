# 036. 写一段自定义异常代码
# 自定义异常用 raise 抛出异常

def func():
    try:
        for i in range(100):
            if i > 10:
                raise Exception('i 大于 10! ')
    except Exception as res:
        print(res)

func()
