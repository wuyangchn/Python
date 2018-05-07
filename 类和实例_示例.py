Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class A:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def add(self):
		self.add = self.x + self.y

>>> a = A(2,7)
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
TypeError: add() missing 1 required positional argument: 'y'
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
