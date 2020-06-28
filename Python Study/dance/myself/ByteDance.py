import os
import cv2
str = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."#字符表
video = cv2.VideoCapture(input("视频名称\n>"))#读取视频
ret,frame = video.read()#读取帧

while ret:#逐帧读取
    str_img = ''
    grey = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)#灰度转换
    grey = cv2.resize(grey,(120,40))#该表大小
    for i in grey:#读取每帧
        for j in i:#读取每行
            index = int(j / 256 *len(str))#获取字符坐标
            str_img += str[index]#将字符添加到字符画中
        str_img += '\n'#换行
    os.system('clear')#下一帧
    print(str_img)#输出字符画
    ret,frame = video.read()
    cv2.waitKey(1)