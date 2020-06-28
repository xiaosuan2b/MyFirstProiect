def loop(num):
    '''
    @parem 循环次数
    '''
    i = 0
    numbers = []
    while i<num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now:",numbers)
        print(f"At the botton i is {i}")


    print("The numbers:")

    for num in numbers:
        print(num)
loop(10086)