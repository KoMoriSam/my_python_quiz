# 024. 字典根据键从小到大排序

dic = {
    "name": "KoMoriSam", 
    "age": 19, 
    "city": "深圳", 
    "tel": "12345678900"
    }

lst = sorted(dic.items(), key=lambda i:i[0], reverse=False)
print(dict(lst))
