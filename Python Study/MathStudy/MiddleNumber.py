'''
计算中位数
'''

count = int(input("请输入数的数量：\n>"))
L = []
for i in range(1,count+1):
	L.append(int(input(f"请输入第 {i} 个数的值：\n")))

L_new = sorted(L)
if len(L_new) % 2 != 0:
    i = len(L_new)// 2
    median = L_new[i]
else:
    i = int(len(L_new)/ 2)
    if (L_new[i-1] + L_new[i]) % 2 == 0:
        median = (L_new[i-1] + L_new[i])/ 2
    else:
        median = (L_new[i-1] + L_new[i])/ 2.0
if isinstance(median, int) == True:
    print("这组数的中位值是：",median)
else:
    print("这组数的中位值是：",'%.1f' % median)