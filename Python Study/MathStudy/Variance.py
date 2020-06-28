count = int(input("请输入参与计算方差的数的数量：\n>"))
parem = []

#获取参与计算的值
for i in range(1,count+1):
	parem.append(float(input(f"请输入参与计算的第{i}个值：\n>")))

def average(numList):
	'''
	获取一个列表的平均值
	@parem 纯数字列表
	@return 平均值
	'''
	sum = 0
	for i in numList:
		sum += i
	return sum/len(numList)
	
def Variance(numList):
	'''
	获取一个列表的方差
	@parem 纯数字列表
	@return 方差
	'''
	ave = average(numList)

	sum = 0
	for i in numList:
		sum += (i-ave)**2
		
	result = sum/len(numList)
	return result


print(f"这些值的方差是：{Variance(parem)}")