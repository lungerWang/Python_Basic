try:
    num = int(input("请输入一个数字"))
    result = 9/num
except ValueError:
    print("类型错误")
except ZeroDivisionError:
    print("除0异常")
except Exception as a:
    print("未捕获异常%s" %a)
else:
    print("没有异常时执行")
finally:
    print("成功与否都会执行")