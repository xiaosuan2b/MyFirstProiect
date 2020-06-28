import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
    "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

# 他们想先练习短语吗?
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# 从网页中加载单词
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

# convert 转换
# snippet 片段
# phrase 短语


def convert(snippet, phrase):
    '''
    将模板(PHRASES)填充内容
    @return 填充后的内容
    '''
    #capitalize()将字符串的第一个字母变成大写,其他字母变小写。
    #random.sample(listname,n)从一个列表里随机抽取n个元素，返回一个列表
    #count() 方法用于统计字符串里某串字符出现的次数
    #[expression for i in iterable if condition] python列表表达式
    #先执行迭代语句，如果if语句为True，执行处理语句
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        #randint(a,b)在a~b范围内随机生成一个整数
        #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        param_count = random.randint(1, 3)
        param_names.append(','.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

    # 替换类名
    for word in class_names:
        result = result.replace("%%%", word, 1)

    # 替换其他名
    for word in other_names:
        result = result.replace("***", word, 1)

    # 替换参数列表
    for word in param_names:
        result = result.replace("@@@", word, 1)

        results.append(result)

    return results


#持续运行直到按下ctrl+d 召唤EOF
try:
    while True:
        snippets = list(PHRASES.keys())
        #shuffle() 方法将序列的所有元素随机排序。
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question,answer = answer, question

                print(question)

                input('>')
                print(f"ANSWER:{answer}\n\n")
except EOFError:
    print("\nBye")
