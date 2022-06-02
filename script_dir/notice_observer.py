"发布订阅设计模式，或者观察者模式"
from abc import ABCMeta,abstractmethod
class  observer(metaclass = ABCMeta): #定义接口
    @abstractmethod
    def update(self,notice):
        pass

class notice():
    def __init__(self):
        self.observers = []

    def attach(self,obs):
        self.observers.append(obs)

    def detach(self,obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self) # 发布者和订阅者在这里耦合，obs 为订阅者对象，self 为发布者对象

class companyNotice(notice):
    def __init__(self,company_info = None):
        super().__init__()
        self.company_info = company_info

    @property
    def company_info(self):
        return self._company_info
    @company_info.setter
    def company_info(self,info):
        self._company_info = info
        self.notify()

class staff(observer):
    def __init__(self):
        self.company_info = None

    def update(self,notice):
        self.company_info = notice.company_info

notice = companyNotice('初始化')
print(notice.company_info)
staff_1 = staff()
staff_2 = staff()
notice.attach(staff_1)
notice.attach(staff_2)
notice.company_info = '通知'
print(staff_1.company_info,staff_2.company_info)
notice.company_info = '新的通知'
print(staff_1.company_info,staff_2.company_info)
