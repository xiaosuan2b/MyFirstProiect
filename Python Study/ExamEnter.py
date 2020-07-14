class Human(object):
    pass

grades = {}

class Students(Human):

    def PrintG(self,name,grade):
        self.grade = grade

        print(f"你这次考了: {self.grade}")
        grades[name] = grade



class GreatStudents(Students):
    def __init__(self,name,grade):
        super(GreatStudents,self).PrintG(name,grade)
        print("不能懈怠！不然后面的同学就赶上你了！")

class MediumStudents(Students):
    def __init__(self,name,grade):
        super(MediumStudents,self).PrintG(name,grade)
        print("努点力！多向周小来同学学习！人家考到了115你为什么考不到114")

class BadStudents(Students):
    def __init__(self,name,grade):
        super(BadStudents,self).PrintG(name,grade)
        print(f"才考了{self.grade}！ 你们是我带过最差的一届！")

LiHua = GreatStudents("LiHua",120)
HanMeimei = MediumStudents("HanMeimei",112)
XiaoMing = BadStudents("XiaoMing",17)

print(grades)

class Teacher(Human):
    def writeGrades(self,file,gra):
        '''记录下分数内容
        @parem filepath grades
        '''
        dataFile = open(file,'w')
        G = '\n'.join(gra)
        dataFile.write(G)
        dataFile.close()

    def Entergrade(self,filePath,gra):
        '''记录下分数内容
        @parem filePath grades
        '''
        dataFile = open(filePath,'w')
        if dataFile.read():
            print(
            '''该数据文件已被写入，请选择：
             1.清空该文件重写
             2.在该文件上追加
             3.不做操作
            ''')
            i = input('>')
            dataFile.close()
            if i == 1:
                dataFile.truncate()
                self.writeGrades(filePath,gra)
            elif i == 2:
                self.writeGrades(filePath,gra)
        else:
            self.writeGrades(filePath,gra)


Teacher.Entergrade("./grades.dat",grades)