import os, sys
print((os.path.abspath('.')))

print(__file__)
print(sys.executable)
"""
你好
"""
print('0' * 10)

def hello(a, b):
    """你好
    :param a: 被加数
    :param b: 加数
    """
    print(a+b)


hello('1', '2')