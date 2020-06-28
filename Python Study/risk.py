import time

print("相信我，这是个很有意思的冒险游戏！")
time.sleep(3)
print("确保你已进入你的最佳状态，按任意键进入游戏......")
input(">")

print("""
########  ####  ######  ##    ## 
##     ##  ##  ##    ## ##   ##  
##     ##  ##  ##       ##  ##   
########   ##   ######  #####    
##   ##    ##        ## ##  ##   
##    ##   ##  ##    ## ##   ##  
##     ## ####  ######  ##    ## """)

print("这是一个剧情向游戏，请仔细阅读剧情部分然后作答！")

print("本游戏将于3s后开始")
time.sleep(1)
print("3")
time.sleep(1)
print("2")

time.sleep(1)
print("1")
time.sleep(1)

def short():
    time.sleep(0.5)
def medium():
    time.sleep(1)
def longer():
    time.sleep(2)
def longest():
    time.sleep(3)


print("剧情部分：")
story = open("./story.txt")

for line in story.readlines():
    length = len(line)

    print(line,end='')

    if length <=3:
        short()
    elif length >3 and length <= 5:
        medium()
    elif length > 5 and length <= 10:
        longer()
    elif length > 10:
        longest()


time.sleep(4)
print("\n\n作答环节：")
time.sleep(1)
print("请问，最后去上学的是谁？")
time.sleep(1)
print("A.钉钉DingTalk")
time.sleep(1)
print("B.无敌小夸克")
time.sleep(1)
print("C.国王")
time.sleep(1)
print("D.宝剑")
time.sleep(1)


print("请作答：")
time.sleep(1)
answer = input('>')

if answer == 'A':
    print("钉钉逃学成功！")
    print("恭喜你游戏失败")
    time.sleep(2)
    print("再来一局？")
elif answer == 'B':
    print("ohhhhhhhhhhhhhhh!")
    time.sleep(2)
    print("诶，你特娘的真是个天才！")
    time.sleep(2)
    print("胜利通关！")
elif answer == 'C':
    print("你仿佛在逗我。")
    time.sleep(4)
    print("游戏结束")
elif answer == 'D':
    print("恭喜你游戏胜......")
    time.sleep(1)
    print("想啥呢？")
    print("滚去重开！")
else:
    print("你这回答的啥玩意？？！")
    print("补考去！")

story.close()