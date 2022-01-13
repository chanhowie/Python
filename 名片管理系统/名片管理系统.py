namecard = []
def sec_func(selection):
    if selection == 1:
        newname = input("输入姓名")
        newage = input("输入年龄")
        newtel = input("输入电话")
        namecard.append({"name": newname, "age": newage,"tel":newtel})
        print("添加成功")
        menu()
    elif selection == 2:
        sername=input("输入要查找的姓名")
        for showcard in namecard:
            if showcard["name"]==sername:
                print("姓名\t\t年龄\t\t电话")
                print("%s\t\t%s\t\t%s"%(showcard["name"],showcard["age"],showcard["tel"]))
                break
        else:
            print("没有找到此人")
        menu()
    elif selection == 3:
        print("姓名\t\t年龄\t\t电话")
        for showcard in namecard:
            print("%s\t\t%s\t\t%s"%(showcard["name"],showcard["age"],showcard["tel"]))
        menu()
        
    elif selection == 0:
        pass
def menu():
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
    select = int(input())
    if (select >= 0) and (select <= 4):
        print("输入成功")
        sec_func(select)
    else:
        print("输入错误，请重新输入")
        menu()


# while(1):
menu()
