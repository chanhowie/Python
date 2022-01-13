def show ():
    strlist = ["", "欢迎使用名片管理系统",
               "请选择功能",
               "①：增加名片",
               "②：查找名片",
               "③：显示全部",
               "⓪：退　　出"]
    
    print(strlist[0].center(24, "━"))
    for strout in strlist[1:]:
        print("┃%s┃" % strout.center(13, "　"))
    print(strlist[0].center(24, "━"))
namecard = []
def newcard():
    newname = input("输入姓名")
    newage = input("输入年龄")
    newtel = input("输入电话")
    namecard.append({"name": newname, "age": newage, "tel": newtel})
    print("添加成功")
def sercard():
    sername = input("输入要查找的姓名")
    for showcard in namecard:
        if showcard["name"] == sername:
            print("姓名\t年龄\t电话")
            print("%s\t%s\t%s" % (showcard["name"], showcard["age"], showcard["tel"]))
            break
    else:
        print("没有找到此人")
def showcard():
    print("姓名\t年龄\t电话")
    for showcard in namecard:
        print("%s\t%s\t%s" % (showcard["name"], showcard["age"], showcard["tel"]))