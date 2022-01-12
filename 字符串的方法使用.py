#numstr="654"
#numstr1="\u00b3"
#numstr2="一万零二百"

#print(numstr.isdecimal())
#print(numstr1.isdigit())
#print(numstr2.isnumeric())

str="你好，我是你哥"
print(str.startswith("你好"))
print(str.endswith("你哥"))
print(str.find("8"))#find方法字符串不存在返回-1
print(str.index("我是"))#字符串不存在报错
print(str.replace("哥","兄弟"))#返回新的字符串，不会修改原有的字符串
print(str)

peom = ["黄鹤楼",
        "李白",
        "\t昔人已乘黄鹤去，此地空余黄鹤楼。\t\t",
        "黄鹤一去不复返，白云千载空悠悠。\n",
        "晴川历历汉阳树，芳草萋萋鹦鹉洲。",
        "日暮乡关何处是？烟波江上使人愁。"]
print(peom)
for peon_str in peom:
    print("|%s|"%peon_str.strip().center(18,"　"))#也可使用ljust,rjust,strip可以去除开头结尾的空格
