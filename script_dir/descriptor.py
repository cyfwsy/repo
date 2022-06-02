'''用描述符操作属性'''
from weakref import WeakKeyDictionary


class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()


    def __get__(self, instance, instance_type): #用实例做索引
        if instance == None:
            return self
        return self._values.get(instance, 0)


    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

#定义类属性
# class Exam:
#     math_grade = Grade()
#     science_grade = Grade()

#定义实例属性使用
class Exam:
    def __init__(self):
        self.math_grade = Grade()
        self.science_grade = Grade()

first_exam = Exam()
second_exam = Exam()
first_exam.math_grade = 86
first_exam.science_grade = 58
second_exam.math_grade = 100
print(Exam.__dict__)
print(Grade.__dict__)
print(first_exam.__dict__)
print(second_exam.__dict__)
print(f'first instance {first_exam.math_grade}')
print(f'second instance {second_exam.math_grade}')
