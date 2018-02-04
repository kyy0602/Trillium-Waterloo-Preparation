Mon = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1]  #周一的停车场情况
Tue = [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]  #周二的停车场情况
Ans = 0 #定义输出结果Answer

for x in range(12):
    Pro = Mon[x] * Tue[x]   #Pro为Product，每天周一与周二在相同停车位停车情况的乘积
    if Pro == 1:
        Ans += 1    #将Ans递加1
print(Ans)