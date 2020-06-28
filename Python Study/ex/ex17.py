from sys import argv
from os.path import exists

#输入参数
script,from_file,to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line,how?
#读取源文件
indata = open(from_file).read()

#输出文件大小
print(f"The input file is {len(indata)} bytes long")
#检测目标文件存在
print(f"Does the output file exist?{exists(to_file)}")

print("Ready,hit any key to continue,CTRL-C to exit")
input(">")

#写入文件
out_file = open(to_file,'w')
out_file.write(indata)

print("Airight,all done.")

out_file.close()
