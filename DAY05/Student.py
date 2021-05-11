class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, couser_name):
        print("%s正在学习%s." % (self.name,couser_name))


def main():
    stu1 = Student('sherlock', 18)
    stu1.study('Python')

if __name__ == '__main__':
    main()
