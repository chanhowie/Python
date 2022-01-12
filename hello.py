namelist = ["张三", "李四", "王五", "赵六", "孙七"]
namelist[1] = "lisi"

namelist.append("王小二")
namelist.insert(1, "张3.5")
templist = ["孙悟空", "猪八戒", "唐僧"]
listlen = len(namelist)
for name in namelist:
    print("我叫%s"%name)
