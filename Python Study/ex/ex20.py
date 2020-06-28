from sys import argv
#解包
script,input_file = argv

#输出文件的全部
def print_all(f):
    print(f.read())

#移动光标的位置到开头
def rewind(f):
    f.seek(0)
    
#输出单行
def print_a_line(line_count,f):
    print(line_count,f.readline())
    
current_file = open(input_file)

#输出当前文件的所有内容
print("First let's print the whole file:\n")
print_all(current_file)

#将读写位置移动到文件开头
print("Now let's rewind,kind of like a tape.")
rewind(current_file)

#逐次输出三行
print("Let's print three lines:")
current_line = 1
print_a_line(current_line,current_file)

current_line +=1
print_a_line(current_line,current_file)

current_line +=1
print_a_line(current_line,current_file)




