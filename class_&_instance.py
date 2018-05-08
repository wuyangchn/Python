Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class A:
	def __init__(self,x,y):  # 创建实例的时候通过__init__输入类的属性
		self.x = x
		self.y = y
	def add(self):
		self.add = self.x + self.y

>>> a = A(2,7)  # __init__方法需要两个参数
>>> a.x
2
>>> a.y
7
>>> a.add()
>>> a.add
9
>>> class A:
	def __init__(self,x,y):
		
	def add(self,x,y):
		self.add = x + y
		
SyntaxError: expected an indented block
>>> class A:
	def __init__(self,x,y):
		pass
	def add(self,x,y):
		self.add = x + y

		
>>> a = A(3,5)
>>> a.add(3.2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.add(3.2)
TypeError: add() missing 1 required positional argument: 'y'  # 类的属性必须用self"加持"？……迷茫
>>> class A:
	def test(self,x,y):
		self.x = x
		self.y = y
	def add(self):
		self.add = self.x + self.y

		
>>> a = A(2,7)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a = A(2,7)
TypeError: object() takes no parameters
>>> 
##############################################################################
# 举例
class Student():
    def __init__(self,name,score):    #有__init__方法，实例传入的参数必须是它相匹配的
        self.name = name
        self.score = score


	def print_score(self):
        print('%s:%s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 60:
            return 'A'
        else:
            return 'B'
        
# 运行效果
>>> manny = Student('manny',80)
>>> manny.name
'manny'
>>> manny.score
80
>>> manny.print_score()
manny:80
>>> manny.get_grade()
'A'
>>> 
# 鱼C课后习题，涉及类的组合
class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池中一共有乌龟%d只，小鱼%d条' % (self.turtle.num,self.fish.num))
# 运行效果
>>> pool = Pool(4,55)
>>> pool.print_num()
水池中一共有乌龟4只，小鱼55条
>>> Turtle(5)
<__main__.Turtle object at 0x0000029A1BE97B00>
>>> t = Turtle(5)
>>> t.num
5
>>> pool.turtle.num
4
>>> 
# 属性跟方法名冲突会发生覆盖
>>> class A:
	def test(self):
		print('hello')

		
>>> a = A()
>>> a.test()
hello
>>> a.test = 1  # 定义实例a的属性
>>> a.test
1
>>> a.test()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.test()
TypeError: 'int' object is not callable  # 实例a的属性a.test覆盖方法a.test()，报错
>>> 
# 不定义属性，只有方法
>>> class C:
	def get_xy(self,x,y):
		self.x = x
		self.y = y
	def print_xy(self):
		print(self.x,self.y)

		
>>> c = C()
>>> c.__dict__
{}
>>> c.get_xy(4,5)
>>> c.__dict__
{'x': 4, 'y': 5}
>>> c.print_xy()
4 5
>>> C.__dict__
mappingproxy({'__module__': '__main__', 'get_xy': <function C.get_xy at 0x0000015908381E18>, 'print_xy': <function C.print_xy at 0x0000015908D68D08>, '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None})
#######################################################################
