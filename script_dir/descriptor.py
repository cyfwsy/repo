'''用描述符操作属性'''
from weakref import WeakKeyDictionary


class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):  # 用实例做索引
        if instance == None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

# 定义类属性


class Exam:
    math = Grade()
    science = Grade()

    def __init__(self, math, science) -> None:
        self.math = math
        self.science = science


exam1 = Exam(10, 88)
exam2 = Exam(100, 44)

print(exam1.math)
print(exam2.math)
print(exam1.science)
print(exam2.science)
exam1.math = 99
print(exam1.math)
exam2.science = 99
print(exam2.science)

