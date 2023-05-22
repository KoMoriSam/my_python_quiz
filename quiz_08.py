# 举例说明异常模块中 try except else finally 的相关意义
# try...except...else 没有捕获到异常，执行 else 语句
# try...except...finally 不管是否捕获到异常，都执行 finally 语句

def tee():
    try:
        a = 64
        print(a)
    except NameError as err_msg:
        print(f'产生错误 {err_msg} !')
    else:
        print('没有捕获到异常，则执行 else 语句。')

def tef():
    try:
        b = 128
        print(b)
    except NameError as err_msg:
        print(f'产生错误 {err_msg} !')
    finally:
        print('不管是否捕获到异常，都执行 finally 语句。')

tee()
tef()
