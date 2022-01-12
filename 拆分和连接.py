peom = "黄鹤楼\t李白\t昔人已乘黄鹤去，此地空余黄鹤楼。\t黄鹤一去不复返，白云千载空悠悠。\n晴川历历汉阳树，芳草萋萋鹦鹉洲。\n日暮乡关何处是？烟波江上使人愁。"
peomresult=peom.split()
print(peomresult)
peomresult=" ".join(peomresult)
print(peomresult)
for peomstr in peom.split():
    print("|%s|"%peomstr.strip().center(20," "))
