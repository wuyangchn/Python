def fibonacci(n):
    if n < 1:
        print('输入有误！')
    if n == 1 or n == 2:
        return 1
    if n>2:
        return fibonacci(n-1)+fibonacci(n-2)

monthes = int(input("经历了多少个月："))
result = fibonacci(monthes)
print("经历了%d 个月后，共有%d 对小兔崽子" % (monthes,result))
#速度较迭代慢
