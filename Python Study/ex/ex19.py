#输出函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes_of_crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    
#直接输入参数
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#使用变量方式输入参数
print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#表达式传递参数
print("we can even do math inside too:")
cheese_and_crackers(10+20,5+6)

#含变量的表达式传递参数
print("And we can combine the two,wariables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)