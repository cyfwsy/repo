'''测试 datetime 模块'''
from datetime import datetime ,timedelta

def date_range(start,stop,step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2022,8,10),datetime(2022,8,25),timedelta(hours=12)):
    print(d)

