"""
#exted会追加打散的数字
In [7]: a.extend(b)

In [8]: a
Out[8]: [1, 2, 3, 4]


#append会追加成一个列表
Out[14]: [1, 2, 3, 4, 0, [3, 4]]

In [15]: a.append([8,9])

In [16]: a
"""
"""
for i in [1,2,3,4,5,6,7,8,9]:
    if i ==10:
        break
    print(i)
else:
    print("如果没有循环完毕，将不会输出")#for循环和else的搭配使用
print("执行完毕")
"""
student=[{"name":"小黄","age":11},
         {"name":"小红","age":12},
         {"name":"小蓝","age":13},
         {"name":"小黑","age":14},
         {"name":"小白","age":15},
         {"name":"小鸟","age":16},]
findname="小黑黑"
for someone in student:
    if someone["name"]==findname:
        print("找到结果%s"%someone["age"])
        break
else:
    print("没找到结果")
    