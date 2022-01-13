#! /usr/bin/python3
import tools


def sec_func(selection):
    if selection == "1":
        tools.newcarda()
    elif selection == "2":
        tools.sercard()
    elif selection == "3":
        tools.showcard()


while True:
    # TODO 显示菜单
    tools.show()
    select = input()
    print("你输入了【%s】" % select)
    if select in tools.selelist:
        if select == "0":
            print("欢迎下次使用")
            break
        sec_func(select)



else:
    print("输入错误，请重新输入")
    menu()
