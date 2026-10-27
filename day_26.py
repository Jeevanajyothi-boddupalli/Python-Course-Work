{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f81709c0",
   "metadata": {},
   "source": [
    "# ENCAPSULATION\n",
    "\n",
    "Encapsulation is an OOP concept that combines data and methods\n",
    "within a class and controls access to the data.\n",
    "\n",
    "It helps protect the data from direct access and modification.\n",
    "\n",
    "## ACCESS SPECIFIERS\n",
    "\n",
    "Python uses naming conventions to control the accessibility of\n",
    "class members.\n",
    "\n",
    "### 1. Public\n",
    "Public members can be accessed from anywhere.\n",
    "\n",
    "### 2. Protected\n",
    "Protected members are represented using a single underscore (_).\n",
    "They can be accessed within the class and its subclasses.\n",
    "\n",
    "### 3. Private\n",
    "Private members are represented using double underscores (__).\n",
    "They cannot be directly accessed from outside the class.\n",
    "\n",
    "## ADVANTAGES OF ENCAPSULATION\n",
    "\n",
    "- Provides data protection.\n",
    "- Controls access to data.\n",
    "- Improves code organization.\n",
    "- Makes the code easier to maintain."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a232085d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jeevana\n",
      "23\n"
     ]
    }
   ],
   "source": [
    "# Public member\n",
    "\n",
    "class Student:\n",
    "\n",
    "    def __init__(self, name, age):\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "\n",
    "\n",
    "student1 = Student(\"Jeevana\", 23)\n",
    "\n",
    "print(student1.name)\n",
    "print(student1.age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f7713096",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bhavana\n",
      "22\n"
     ]
    }
   ],
   "source": [
    "# Protected member\n",
    "\n",
    "class Student:\n",
    "\n",
    "    def __init__(self, name, age):\n",
    "        self._name = name\n",
    "        self._age = age\n",
    "\n",
    "\n",
    "student1 = Student(\"Jeevana\", 23)\n",
    "\n",
    "print(student1._name)\n",
    "print(student1._age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f87d407a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Jeevana\n",
      "Age: 23\n"
     ]
    }
   ],
   "source": [
    "# Private member\n",
    "\n",
    "class Student:\n",
    "\n",
    "    def __init__(self, name, age):\n",
    "        self.__name = name\n",
    "        self.__age = age\n",
    "\n",
    "    def display(self):\n",
    "        print(\"Name:\", self.__name)\n",
    "        print(\"Age:\", self.__age)\n",
    "\n",
    "\n",
    "student1 = Student(\"Jeevana\", 23)\n",
    "\n",
    "student1.display()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b0f8233e",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Student' object has no attribute '__name'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 11\u001b[39m\n\u001b[32m      7\u001b[39m \n\u001b[32m      8\u001b[39m \n\u001b[32m      9\u001b[39m student1 = Student(\u001b[33m\"Bhavana\"\u001b[39m)\n\u001b[32m     10\u001b[39m \n\u001b[32m---> \u001b[39m\u001b[32m11\u001b[39m print(student1.__name)\n",

     ]
    }
   ],
   "source": [
    "# Private member cannot be directly accessed\n",
    "\n",
    "class Student:\n",
    "\n",
    "    def __init__(self, name):\n",
    "        self.__name = name\n",
    "\n",
    "\n",
    "student1 = Student(\"Jeevana\")\n",
    "\n",
    "print(student1.__name)"
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
}