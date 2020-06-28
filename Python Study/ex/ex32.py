the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'prnnies',2,'dimes',3,'quarters']

#第一种for循环：通过一个列表
for number in the_count:
    print(f"This is count {number}")

#同上
for fruit in fruits:
    print(f"A fruit of type:{fruit}")

#我们也能通过混合列表
#由于我们不知道里面包含什么内容，因此必须用{}
for i in change:
    print(f"I got {i}")

#我们也可以建立列表，从新列表开始
elements = []

#然后用range(开始值默认0，生成的数的个数)函数从0数到5
for i in range(0,6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand.
    elements.append(i)

#现在我们也可以将它们打印到屏幕上了
for i in elements:
    print(f"Element was: {i}")


