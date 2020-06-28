#获取数的数量
count = int(input("请输入 参与计算的值 的数量：\n>"))


weight = []
number = []

#获取权的值
for i in range(1,count+1):
	print(f"请输入第 {i} 个权")
	weight.append(int(input(">")))
	
#获取数的值
for i in range(1,count+1):
	print(f"请输入第 {i} 个数")
	number.append(int(input(">")))
	
#加权
add_n = 0
for i in range(0,count):
	print(f"adding: {weight[i]} * {number[i]}")
	add_n += (weight[i] * number[i])
	
add_w = 0
for w in weight:
	add_w += w

print("add_n:",add_n)
print("add_w:",add_w)
result = add_n/add_w

print(f"该组数据的加权平均值是：\n{result}")