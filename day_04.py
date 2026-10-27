{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ef94b3ed",
   "metadata": {},
   "source": [
    "DATATYPES\n",
    "\n",
    "->Numeric: integers, floats, complex\n",
    "->Sequence: list, tuple, string\n",
    "->Mapping: dictionary\n",
    "->Boolean: True/False\n",
    "->None Type: None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "059f4bd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "#Numeric Datatype\n",
    "x=10\n",
    "print(type(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5575397c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n",
      "<class 'complex'>\n"
     ]
    }
   ],
   "source": [
    "x=13.45\n",
    "y=10+4j\n",
    "print(type(x))\n",
    "print(type(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1e7fe5f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n",
      "<class 'tuple'>\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "#Sequence\n",
    "l=[1,2,3,4,5]\n",
    "t=(1,2,3,4,5)\n",
    "str=\"Hello World\"\n",
    "print(type(l))\n",
    "print(type(t))\n",
    "print(type(str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "73b7cdfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n",
      "<class 'set'>\n"
     ]
    }
   ],
   "source": [
    "#Mapping\n",
    "d={\"name\":\"John\",\"age\":30}\n",
    "s={1,2,3,4,5}\n",
    "print(type(d))\n",
    "print(type(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "97b919a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "#Boolean\n",
    "a=True\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ea4138eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'NoneType'>\n"
     ]
    }
   ],
   "source": [
    "#None Type\n",
    "b=None\n",
    "print(type(b))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2e4fef7",
   "metadata": {},
   "source": [
    "TYPE CASTING\n",
    "\n",
    "1.Implicit- Machine itself does the conversion.\n",
    "2.Explicit- we forcefully convert one type to another."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4f4159e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19.5\n"
     ]
    }
   ],
   "source": [
    "#Implicit Type Conversion\n",
    "x=10\n",
    "y=9.5\n",
    "print(x+y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ef6c9f4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n"
     ]
    }
   ],
   "source": [
    "#Explicit Type Conversion\n",
    "s1='123'\n",
    "x=int(s1)\n",
    "print(x)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
},

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
