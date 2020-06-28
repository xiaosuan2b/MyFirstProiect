#ex15 读取文件 
from sys import argv
script,filename = argv
txt = open(filename)
print("This is a txt reader.")
print(f"here is your file {filename}")
print(txt.read())
txt.close()
