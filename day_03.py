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
dictionary = {'a':1,'b':2,'c':3}
d = {'j':2,'e':2,'v':1,'a':2,'n':1,'y':1,'o':1,'t':1,'h':1,'i':1}
details = {'name':'jeevanajyothi',
           'rollno':96,           
           'cgpa':9.2}
print(details)
{'name': 'jeevanajyothi', 'rollno': 96, 'cgpa': 9.2}
print(d)
{'j': 2, 'e': 2, 'v': 1, 'a': 2, 'n': 1, 'y': 1, 'o': 1, 't': 1, 'h': 1, 'i': 1}
print(dictionary)
{'a': 1, 'b': 2, 'c': 3}
 details = {'name':'ganesh',
            'no':26,
            'cgpa':9.2,
            'mbl no':9014805196}
 print(details)
{'name': 'ganesh', 'no': 26, 'cgpa': 9.2, 'mbl no': 9014805196}
d = {'a':1,'b':1}
print(details['no'])
26
print(details.get('no'))
26
x = 10
y =9.5
print(x+y)
19.5
x = 10
print(x)
10
print(type(x))
<class 'int'
cgpa = 9.3
print(type(cgpa))
<class 'float'>
c = 5+6j
print(type(c))
<class 'complex'>
t = ()
t1 = tuple()
t2 = (1,2,3,4,5)
print(type(t),type(t1),type(t2))
<class 'tuple'> <class 'tuple'> <class 'tuple'>