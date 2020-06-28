import sys
#参数解包
#script,encoding,error = sys.argv
encoding,error="utf-8","strict"

#主方法
def main(language_file,encoding,errors):
    #读取一行
    line = language_file.readline()
    #循环到文档中止(line为空)
    if line:
        print_line(line,encoding,errors)
        #跳转到main，if防止死循环
        return main(language_file,encoding,errors)

#打印一行字节<===>字符
def print_line(line,encoding,errors):
    #去除首尾空格、\n
    next_lang = line.strip()
    #把字符串编码为字节码
    raw_bytes = next_lang.encode(encoding,errors = errors)
    #把字节码编码为字符串
    cooked_string = raw_bytes.decode(encoding,errors = errors)

    #输出  {字节码}<===>{字符串}
    print(f"{raw_bytes}<===>{cooked_string}")

languages = open("./txt/languages.txt",encoding="utf-8")
#运行
main(languages,encoding,error)
