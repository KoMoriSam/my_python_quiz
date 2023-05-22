# 022. s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
# set去重，去重转成list,利用sort方法排序，reverse=False是从小到大排
# list是不变数据类型，s.sort时候没有返回值，所以注释的代码写法不正确

s = 'ajldjlajfdljfddd'
s = set(s)
s = list(s)
s.sort(reverse=False)
res = ''.join(s)
print(res)
