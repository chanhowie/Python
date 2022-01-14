# def meause():
#     print("测量开始")
#     temp = 30
#     wet = 40
#     print("测量结束")
#     return temp, wet  # 返回的类型是元组
#
#
# result1, result2 = meause()# 变量中个数应该与元组中保持一致
# print(result1)
# print(result2)
# result2,result1=result1,result2
# print(result1)
# print(result2)


# a=5
# b=20
# a=a+b
# b=a-b
# a=a-b
# print (a,b)


# a=5
# b=20
# a,b=(b,a)
# print(a,b)


# def demo(list1):
#     list1 += [3,4] # 列表使用+=实际上是使用了extend会修改外部数据
# #    list1 =list1+[3,4]  #而只是用+不会修改外部数据
#     print(list1)
#
# list2=[2,1]
# demo(list2)
#
# print(list2,"wwwwwwww")
# list2.sort(reverse=True) # 缺省参数的默认值为False
# print(list2)


# def namegen(name, title, gender=True):
#     """
#     输出姓名及性别
#     :param title:
#     :param name: 姓名
#     :param gender: True = 男生 False = 女生
#     """
#     gender_text = "男生"
#     if not gender:
#         gender_text = "女生"
#
#     print("%s是%s" % (name, gender_text))
#
#
# namegen("小明","sad")
# namegen("小红","hap", False)


# def demo(num, *nums, **numss):
#     print(num)
#     print(nums)
#     print(numss)
# demo(1, 1, 1, 1, 2, 3, 4, 6, name="xiaomi")


# def demo(*args):  # *args 接收多个参数
#     num = 0
#     print(args)
#     for n in args:
#         num += n
#     return num
#
#
# result = demo(1, 2, 3, 4, 5)
# print(result)



# def demo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# gl_num=(1,2,3,4)
# #gl_dict={"name":"小明","qq":"123"}
# gl_dict={"7":8}
# demo(gl_num,**gl_dict)