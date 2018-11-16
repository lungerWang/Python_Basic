# s1 = 72
# s2 = 85
# r = (85 - 72) / 72 * 100
# print('成绩提升了%.1f%%' % r)
# list = ['a', 'b', ['c', 'd']]
# print('len =', len(list))
#
# height = 1.72
# weight = 60
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print("过轻")
# elif 18.5 <= bmi < 25:
#     print("正常")
# elif 25 <= bmi <= 28:
#     print("过重")
# elif 28 < bmi <= 32:
#     print("肥胖")
# else:
#     print("严重肥胖")
#
# list = ["KangKang", "Maria", "Jan", "Macheal"]
# for name in list:
#     print("hello:%s" %name)
#
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# d = {'Michael' : 95, 'Bob': 75}
# d['Adam'] = 67
# print(d['Adam'])
# a = 'Tomas' in d
# print(a)
# print(d.get('Tomas',-1))
# print(d.get('Michael'))
# # get方法不会角标越界
# d.pop('Adam')
# print(d.get('Adam'))
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的

# s = set([1, 2, 3])
# print(s)
# help(max)
# n1= 255
# n2= 1000
# print(hex(n1))
# print(hex(n2))
# def my_abs(x):
#     if(x >= 0):
#         return x
#     else:
#         return -x
#
# a = -1
# print(my_abs(a))
#
# def nop():
#     pass
# def double_return(x, y):
#     if(x < 0):
#         x = -x
#     if(y < 0):
#         y = -y
#     return x,y
# x,y = double_return(-1, -2)
# print(double_return(-1, -2))
# print(x)
# print(y)
# import math
# def quadratic(a, b, c):
#     x1 = ( -b + math.sqrt(b ** 2 - 4*a*c))/ (2*a)
#     x2 = ( -b - math.sqrt(b ** 2 - 4*a*c))/ (2*a)
#     return x1, x2
#
# print(quadratic(1, 0, -16))
# 关键参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other', kw)
#
# extra = {'city' : 'beijing', 'job' : 'doctor'}
# person('kangkang', 18, city = extra['city'], job = extra['job'])
# print(list(range(1,11)))
# l = [x * x for x in range(1, 11)]
# print(l)
# l2 = [x * x for x in range(1, 11) if x % 2 != 0]
# print(l2)
# l3 = [m + n for m in'ABC'for n in 'XYZ']
# print(l3)

# d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
# for k,v in d.items():
#     print(k, v)
# from collections.abc import Iterator
# print(isinstance({}, Iterator));
# print(isinstance([], Iterator));
# print(isinstance('abc', Iterator));
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# 高阶函数
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-2, 3, abs))
# map使用
# def f(x):
#     return x * x
#
# r = map(f, list(range(1, 10)))
# print(list(r))
# filter使用
# def is_odd(n):
#     return n%2 == 1
# print(list(filter(is_odd,list(range(1,10)))))
#
# def no_empty(s):
#     return s and s.strip()
#
# print(list(filter(no_empty, ['1', '234', '', '2',None, '3'])))
# sorted使用
# print(sorted([36, 5, -12, 9, -21]))
# 返回函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)
# print(f())
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 匿名函数
# print(list(map(lambda x: x*x, list(range(1, 9)))))

# L = list(filter(lambda n: n% 2 == 1, range(1, 20)))
# print(L)
# def log(func):
# #     def wrapper(*args, **kw):
# #         print('call %s():' % func.__name__)
# #         return func(*args, **kw)
# #     return wrapper
# #
# # @log
# # def now():
# #     print('2015-3-25')
# #
# # now();
# 继承
# class Animal(object):
#     def run(self):
#         print('animal is running...', 211.5 * 12)
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     name = "Tom"
#     age = "18"
#     def eat(self):
#         pass
#     pass
#
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()
#
# isinstance(cat, Cat)
# print(type(123))
# print(type('123'))
# print(type(None))
# print(type(abs))
#
# print(dir(Cat))
# 实例属性和类属性的区别
# class Student(object):
#      count = 0
#      def __init__(self, name):
#          self.name = name
#          Student.count += 1
#
# print(Student.count)
# s = Student('kangkang')
# print(s.count)
# print(Student.count)
# s.count = 100
# print(s.count)
# print(Student.count)
# 给实例绑定一个方法，注意是实例，对另外一个实例就不起作用
# class Student(object):
# #     pass
# # def set_age(self, age):
# #     self.age = age
# #
# # from types import MethodType
# # s = Student()
# # s.set_age = MethodType(set_age, s)
# # s.set_age(25)
# # print(s.age)
# #
# # # 给类绑定方法
# # Student.set_score = set_age
# # s2 = Student()
# # s2.set_score(26)
# # print(s2.age)
# class Student(object):
#     __slots__ = ('name', 'age') #用tuple预定义允许绑定的属性名称
#
# s = Student()
# s.name = "123"
# s.age = "99"
# s.money = "$1"
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         self._score = value;
#
# s = Student()
# s.score = 100
# print(s.score)
# class Student(object):
#     def __init__(self, name):
#         self.name = name;
#
#     def __str__(self):
#         return 'Student name = %s' % self.name
#
# s = Student("Maria")
# print(s)
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if(self.a > 1000):
#             raise StopIteration()
#         return self.a
#
# for n in Fib():
#     print(n)
# 多重继承
# class RunnableMixIn(object):
#     def run(self):
#         print('running...')
#
# class Animal(object):
#     def eat(self):
#         print('eating...')
#
# class People(Animal, RunnableMixIn):
#     pass
#
# p = People();
# p.run()
# p.eat()

# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, attr):
#         return 99
#
# s = Student();
# print(s.socre)
# 枚举
# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar'))
# print(Month.Jan.name)
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
#
# from enum import unique
#
# @unique
# class WeekDay(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#
# day1 = WeekDay.Mon
# print(day1)
# 动态语言和静态语言的最大不同，就是函数和类的定义，不是在编译时定义，而是运行时动态创建的
# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)
#
# print(type(Hello))
# h = Hello()
# h.hello()
# print(type(h))
# def fn(self, name='world'):
#     print('hello, %s.' %name)
#
# Hello = type('Hello', (object,), dict(hello = fn))
# h = Hello()
# h.hello()
# try:
#     print('try...')
#     r = 10 / 0
#     print('result :', r)
# except ZeroDivisionError as e:
#     print('except :', e)
# finally:
#     print('finally...')
# print('end')
# try:
#     r = 10 / int('a')
# except ValueError as e:
#     print('value error :', e)
# except ZeroDivisionError as e:
#     print('zero error:', e)
# else:
#     print('else')
# finally:
#     print('finally')
# from functools import reduce
#
# def str2num(s):
#     return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

# f = open('D:/1.txt', 'r')
# print(f.read())
# f.close()

# with open('d:/1.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())
# f = open('d:/1.txt', 'a')
# f.write("01234")
# f.close()
# from io import StringIO
# f = StringIO();
# f.write('hello')
# print(f.getvalue())
# from io import BytesIO
# f = BytesIO()
# f.write('日文'.encode('utf-8'))
# print(f.getvalue())
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())
# import os
# print(os.environ.get("ANDROID_HOME"))
# print(os.path.abspath('.'))
#
# print(os.path.split('/Users/michael/testdir/file.txt'))
# import pickle
# d = dict(name='bob', age=20)
# f = open('d:/a.txt','wb')
# pickle.dump(d, f)
# f.close()

# f = open('d:/a.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)
# import json
# #转换成json
# d = dict(name='bob', age=20, score=88)
# j = json.dumps(d)
# print(j)
# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('run child process %s(%s)...' % (name, os.getpid()))
#
# if __name__ =='__main__':
#     print('parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end')
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('run task %s(%s)...' %(name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random()* 10)
#     end = time.time()
#     print('task %s runs %0.2f seconds.' %(name, (end - start)) )
#
# if __name__ == '__main__':
#     print('parant process %s.' % os.getpid())
#     p = Pool(10)
#     for i in range(11):
#         p.apply_async(long_time_task, args=(i,))
#     print("waitting fo all subprocesses done...")
#     p.close()
#     p.join()
#     print('all subprocesses done.')
# from multiprocessing import Process, Queue
# import os, time, random
# def write(q):
#     print('Process to write : %s' % os.getpid())
#     for value in ['a', 'b', 'c']:
#         print('put %s to queue...' %value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print('process to read : %s' %os.getpid())
#     while True:
#         value = q.get(True)
#         print('get %s from queue' %value)
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

# import time, threading
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n+1
#         print('thread %s >>>%s' %(threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
# import time, threading
# balance = 0
# lock = threading.Lock()
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(1000000):
#         lock.acquire()
#         try:
#          change_it(n)
#         finally:
#            lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# import threading
# # local_school = threading.local()
# #
# # def process_student():
# #     std = local_school.student
# #     print('hello, %s(in%s)' % (std, threading.current_thread().name))
# #
# # def process_thread(name):
# #     local_school.student = name
# #     process_student()
# #
# # t1= threading.Thread(target=process_thread, args=('alice',), name ='thread1')
# # t2= threading.Thread(target=process_thread, args=('bob',), name='thread2')
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# datetime是Python处理日期和时间的标准库
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(type(now))
#
# dt = datetime(2015, 4, 10)
# print(dt)
# print(dt.timestamp())
# print(datetime.fromtimestamp(1428595200.0))
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
# from collections import namedtuple
# Point = namedtuple('Point',['x', 'y'])
# p = Point(1,2)
# print(p.x)
# print(p.y)
# Circle = namedtuple('Circle', ['x', 'y', 'r'])
#
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft("y")
# print(q)
# q.pop()
# print(q)
# q.popleft()
# print(q)
# from collections import defaultdict
# dd = defaultdict(lambda : 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])
# from collections import OrderedDict
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)
# import base64
# e = base64.b64encode(b'123')
# print(e)
# d = base64.b64decode('MTIz')
# print(d)
# import struct
#
#
# def image_info(image_path):
#     with open(image_path, "rb") as file:
#         image_header = file.read(30)
#         image_info = struct.unpack('<ccIIIIIIHH', image_header)
#         return {
#             "size": image_info[2],
#             "width": image_info[6],
#             "height": image_info[7],
#             "color": image_info[9]
#         }
#
# print(image_info("D:/茶烟/115.jpg"))

# import struct,base64
# bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
#
# def bmp_info(data):
#     b=struct.unpack('>ccIIIIIIHH',data[:30])
#     if True:
#           return {
#               'width': b[6],
#               'height': b[7],
#               'color': b[9]
#           }
#
# with open("D:/茶烟/115.jpg", "rb") as file:
#     image_header = file.read(30)
#     print(bmp_info(image_header))
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# md52 = hashlib.md5()
# md52.update('how to use md5 in '.encode('utf-8'))
# md52.update('python hashlib?'.encode('utf-8'))
# print(md52.hexdigest())
# import hmac
# message = b'hello,world'
# key = b'secret'
# h = hmac.new(key, message, digestmod='MD5')
# print(h.hexdigest())
#import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)
#
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x : x <= 10, natuals)
# a = list(ns)
# print(a)
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('end')
#
#     def query(self):
#         print('query info about %s...' % self.name)
#
# with Query('Bob') as q:
#     q.query()
# from contextlib import contextmanager
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('query info about %s' % self.name)
#
#
# @contextmanager
# def create_query(name):
#     print('begin')
#     q = Query(name)
#     yield q
#     print('end')
#
# with create_query("kangkang") as q:
#     q.query()

# from urllib import request
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('status :', f.status, f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' %(k,v))
#     print("data:", data.decode('utf-8'))
# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' %(k, v))
#     print('data:', f.read().decode('utf-8'))
# from urllib import request, parse
# print('login ti weibo.cn')
# email = input('Eamil:')
# pwd = input('pwd')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', pwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F' )
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('status', f.status, f.reason)
#     print('data:', f.read().decode('utf-8'))
from html.parser import HTMLParser
from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# PIL :python image library
# from PIL import Image
#
# im = Image.open('D://115.jpg')
# w,h = im.size
# print('Original image size : %s*%s' %(w,h))
# im.thumbnail((w/2, h/2))
# print('Resize iamge to : %s*%s' %((w/2, h/2)))
# im.save('thumbnail.jpg', 'jpeg')
#
# 生成验证码
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
#
# def rndChar():
#     return chr(random.randint(65, 90))
#
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
# def rndColor2():
#     return(random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# font = ImageFont.truetype('arial.ttf', 36)
# draw = ImageDraw.Draw(image)
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill = rndColor())
#
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#
# iamge = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')
#import requests
# r = requests.get('https://www.douban.com')
# print(r.status_code)
# print(r.text)
# r = requests.get('https://www.douban.com/search', params = {'q':'python', 'cat':'dog'})
# print(r.url)
# print(r.json())
# r = requests.get('https://bapi.baby-kingdom.com/index.php?mod=stand&op=types&ver=3.9.0&app=android&code=NWFkMmI0ZDU4N2RlOTg1ZDc1NThhZDQ1MWRiMmQxNmE=-MTU0MjMzNjM4Mw==')
# print(r.json())
#r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})