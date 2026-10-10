Python 3.13.15 (tags/v3.13.15:4061bc4, Aug  5 2026, 13:05:39) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> S1 = {1,2,3,4}
>>> S2 = {3,4,5,6}
>>> print(S1.union(S2))
{1, 2, 3, 4, 5, 6}
>>> print(S1.intersection(S2))
{3, 4}
>>> print(S1-S2)
{1, 2}
>>> print(S1^S2)
{1, 2, 5, 6}
>>> S1 = {1,2,4}
>>> S2 = {4}
>>> print(S2.issubset(S2))
True
>>> print(S1.issubset(S2))
False
>>> print(S2.issubset(S1))
True
>>> print(S1.add(10))
None
>>> S1.add(10)
>>> print(S1.update[10,50,60])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(S1.update[10,50,60])
TypeError: 'builtin_function_or_method' object is not subscriptable
