# 054. 保留两位小数
# 题目本身只有a="%.03f"%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）

a = '%.03f' % 1.3335
print(a,type(a))

b = round(float(a),1)
print(b)

b = round(float(a),2)
print(b)
