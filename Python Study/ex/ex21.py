#加法器
def add(a,b):
    print(f"ADDING {a} + {b}")
    return a+b
#减法器
def subtract(a,b):
    print(f"SUBTRACTING {a}-{b}")
    return a-b
#乘法器
def multiply(a,b):
    print(f"MULTIPLYING {a}*{b}")
    return a*b
#除法器
def divide(a,b):
    print(f"DIVIDING {a}/{b}")
    return a/b


print("Let's do some math with just functions!")

age = add(10,3)
height = subtract(160,4)
weight = multiply(22.5,2)
iq = divide(100,2)

print(f"Age:{age}\nHeight:{height}\nWeight:{weight}\nIQ:{iq}")


#A puzzle for the extra credit,type it in any way.
print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes:",what,"Can you do it by hand?")