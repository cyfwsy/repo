'''编码转换'''
import base64
# def uni_bytes(str):
#     a = base64.b64encode(str)
#     print(str)
#     print(a)
#     b = base64.b64decode(a)
#     print(a.decode('utf-8'))
#     print(b.decode('utf-8'))
#
# str = '中文信息'.encode('utf-8')
# str1 = '景观大道'.encode('utf-8')
# uni_bytes(str)
# uni_bytes(str1)
text = 'python 实例'.encode('utf-8')
print(text)
print(text.decode('utf-8'))
text1 = 'python 实例'.encode('utf-8')
b = base64.b64encode(text1)
c = base64.b64decode(b)
print(b)
print(c)
print("-----------------------------")