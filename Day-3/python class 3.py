Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dictionary = {'a':1,'b':2,'c':3}
>>> d = {'j':2,'e':2,'v':1,'a':2,'n':1,'y':1,'o':1,'t':1,'h':1,'i':1}
>>> details = {'name':'jeevanajyothi',
...            'rollno':96,
...            'cgpa':9.2}
>>> print(details)
{'name': 'jeevanajyothi', 'rollno': 96, 'cgpa': 9.2}
>>> print(d)
{'j': 2, 'e': 2, 'v': 1, 'a': 2, 'n': 1, 'y': 1, 'o': 1, 't': 1, 'h': 1, 'i': 1}
>>> print(dictionary)
{'a': 1, 'b': 2, 'c': 3}
>>> detals =
SyntaxError: invalid syntax
>>> details = {'name':'ganesh',
...            'no':26,
...            'cgpa':9.2,
...            'mbl no':9014805196}
>>> print(details)
{'name': 'ganesh', 'no': 26, 'cgpa': 9.2, 'mbl no': 9014805196}
>>> d = {'a':1,'b':1}
>>> print(details['no'])
26
>>> print(details.get('no'))
26
>>> x = 10
>>> y =9.5
>>> print(x+y)
19.5
>>> x = 10
>>> print(x)
10
>>> print(type(x))
<class 'int'>
>>> cgpa = 9.3
>>> print(type(cgpa))
<class 'float'>
>>> c = 5+6j
print(type(c))
<class 'complex'>
t = ()
t1 = tuple()
t2 = (1,2,3,4,5)
print(type(t),type(t1),type(t2))
<class 'tuple'> <class 'tuple'> <class 'tuple'>
