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

def fibonacci(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print("输入有误！")
        return -1
    while (n-2)>0:#若n==9,8,7,6,5,4,3，false
        n3 = n1 + n2 #n3==2，3,5,8,13,21,34
        n1 = n2 #n1==1,2,3,5,8,13,21
        n2 = n3#n2==2,3,5,8,13,21,34
        n -= 1#n==8,7,6,5,4,3,2

    return n3

n = int(input("经历了多少个月："))
result = fibonacci(n)
print("经历了%d 个月后，共有%d 对小兔崽子" % (n,result))
        
