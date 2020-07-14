'''a = 0.1
b = 0.1
print(a)
print(b)
print(a and b)'''

'''
number_list = []
def adding(*args):
    ''''''
    获取参数之和
    ''''''
    number_list = args
    result = 0
    for i in number_list:
        result += i
    return result

def pingjun(*args):
    ''''''
    获取参数的平均值
    ''''''
    num = 0    
    sums = 0
    for i in args:
        num += 1
        sums += i

    #result = adding(args)/number
    return sums/num

print(adding(233,1000,10000))
print(pingjun(100,0))
'''

'''
#对数升序或降序排列
def uporder(*args):
    return sorted(args)

def downorder(*args):
    return sorted(args,reverse=True)
        

print(uporder(3,7,4,1))
print(downorder(2,7,4,1))
'''
'''
class xmath:
    def adding(self,a,b):
        return a+b
    
    def subtraction(self,a,b):
        return a-b

math = xmath()
print(math.adding(1,1))
print(math.subtraction(1,1))
'''

