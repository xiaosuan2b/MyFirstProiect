from functools import reduce
def myAvg1(*param):
    sum1 = 0
    paramLen=0
    for n in param:
         sum1 +=n
         paramLen+=1
    avg=sum1/paramLen
    return sum1,avg

print(myAvg1(1,2,3))

def myAvg2(*param):
    sum1 = reduce(lambda x, y: x + y, param)
    return sum1,sum1/len(param)
print(myAvg2(1,2,3,4))

def myAvg3(*param):
    sumParam=sum(param)
    avg=sumParam/len(param)
    return sumParam,avg

print(myAvg3(1,2,3,4,5,6,7,8,9,10))