info=("小明",178)
print("%s的身高是%.2f"%info)
listinfo=list(info)
listinfo[0]="小黄"
listinfo[1]=180
tupleinfo=tuple(listinfo)
print("%s的身高是%.2f"%tupleinfo)
