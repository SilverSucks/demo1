try:
    n1 = int(input('请输入一个数：'))
    n2 = int(input('请输入另外一个数：'))
    result = n1/n2


except ValueError:
    print('输入为非法字符！')
except ZeroDivisionError:
    print('异常捕获到了~')
    print('除数不能为0')
else:
    print('结果为：', result)
    print('没有异常~')
finally:
    print('无论程序是否产生异常，总会被执行的代码')
print('程序结束')