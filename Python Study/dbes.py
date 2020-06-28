#decode bytes,encode strings.
#解码字节串，编码字符串

str1 = '得'
str2 = 'ョ'

#将这两个字编码为字节码（16进制），在底层是原始的0和1
zijiema1 = str1.encode("utf-8")
zijiema2 = str2.encode("utf-8")

#重新编码为字符编码
zfbm1 = zijiema1.decode("utf-8")
zfbm2 = zijiema2.decode("utf-8")

#输出 格式：“原始字符串<===>字节码”
print(f"{str1}<===>{zijiema1}")
print(f"{str2}<===>{zijiema2}")

#输出重新编码后的字符
print(zfbm1)
print(zfbm2)