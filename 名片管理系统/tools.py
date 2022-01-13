namecard = []
relist = ["1", "2", "3"]
selelist = ["1", "2", "3", "0"]  # 使用列表方法限制输入类型，可以排除浮点数或其他
seredlist = []


def show():
    """
   菜单栏
    """
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


def newcarda():
    newname = input("输入姓名")
    newage = input("输入年龄")
    newtel = input("输入电话")
    if({"name": newname, "age": newage, "tel": newtel} in namecard):
        print("列表中存在相同数据，请重新输入")
    else:
        namecard.append({"name": newname, "age": newage, "tel": newtel})
        print("添加成功")


def sercard():
    sername = input("输入要查找的姓名")
    first_flag = True  # 用来标识是否为第一次出现
    for showcard in namecard:
        if showcard["name"] == sername:
            seredlist.append(namecard.index(showcard))
            if first_flag == True:
                print("姓名\t\t\t年龄\t\t\t电话")
                first_flag = False;
            print("%s\t\t\t%s\t\t\t%s" % (showcard["name"], showcard["age"], showcard["tel"]))
    
    if first_flag == True:
        print("没有找到%s" % sername)
        return
    
    deal(seredlist)
    seredlist.clear()#退出后清除搜索结果


def showcard():
    if len(namecard) == 0:
        print("列表为空，请先添加名片")
        return
    print("姓名\t\t\t年龄\t\t\t电话")
    print("-" * 28)
    for showcard in namecard:
        print("%s\t\t\t%s\t\t\t%s" % (showcard["name"], showcard["age"], showcard["tel"]))


def deal(seredlist):
    resec = input("①  删除  ②  修改  ③  返回")
    if resec in relist:
        if resec == "1":
            for i in reversed(seredlist): #倒序删除，防止删错位置
                del namecard[i]
        if resec =="2":
            for i in reversed(seredlist):
                modify = True # 修改失败标志位   修改成功改为假
                while(modify):
                    newname = input("输入姓名，当前为 %s 回车不修改"%namecard[i]["name"])
                    if newname == "":
                        newname=namecard[i]["name"]
                    newage = input("输入年龄，当前为 %s 回车不修改"%namecard[i]["age"])
                    if newage == "":
                        newage = namecard[i]["age"]
                    newtel = input("输入电话，当前为 %s 回车不修改"%namecard[i]["tel"])
                    if newtel == "":
                        newtel = namecard[i]["tel"]
                    if ({"name": newname, "age": newage, "tel": newtel} in namecard):
                        print("列表中存在相同数据，请重新输入")
                    else:
                        namecard[i]={"name":newname,"age":newage,"tel":newtel}
                        print("修改成功")
                        modify=False
        if resec == "3":
            return