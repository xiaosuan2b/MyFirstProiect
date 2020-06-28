import cmath

x1 = int(input("请输入第一个点的X坐标\n>"))
y1 = int(input("请输入第一个点的Y坐标\n>"))
x2 = int(input("请输入第二个点的X坐标\n>"))
y2 = int(input("请输入第二个点的Y坐标\n>"))
x = (x1-x2)**2
y = (y1-y2)**2
result = cmath.sqrt(x+y)
print(f"({x1},{y1})与({x2},{y2})之间的距离是：√{x+y}")
print(f"开方后:{result}")
