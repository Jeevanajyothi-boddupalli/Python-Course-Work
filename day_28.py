{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "94182d63",
   "metadata": {},
   "source": [
    "# POLYMORPHISM\n",
    "\n",
    "Polymorphism means \"many forms\".\n",
    "\n",
    "In Python, polymorphism allows the same method, operator, or function\n",
    "to perform different actions depending on the object or data type.\n",
    "\n",
    "## TYPES OF POLYMORPHISM\n",
    "\n",
    "### 1. METHOD POLYMORPHISM\n",
    "\n",
    "Method polymorphism occurs when the same method name behaves\n",
    "differently in different situations.\n",
    "\n",
    "It includes:\n",
    "\n",
    "#### Method Overloading\n",
    "Method overloading means defining multiple methods with the same\n",
    "name but different parameters.\n",
    "\n",
    "Python does not support traditional method overloading directly.\n",
    "However, it can be achieved using default arguments or variable-length\n",
    "arguments.\n",
    "\n",
    "#### Method Overriding\n",
    "Method overriding occurs when a child class provides its own\n",
    "implementation of a method that is already defined in the parent class.\n",
    "\n",
    "### 2. OPERATOR POLYMORPHISM\n",
    "\n",
    "Operator polymorphism occurs when the same operator performs\n",
    "different operations depending on the data types.\n",
    "\n",
    "#### Operator Overloading\n",
    "Operator overloading allows operators such as +, -, *, and ==\n",
    "to behave differently for different objects.\n",
    "\n",
    "### 3. FUNCTION POLYMORPHISM\n",
    "\n",
    "Function polymorphism occurs when the same built-in function\n",
    "can work with different types of data.\n",
    "\n",
    "Examples include len(), type(), and max()."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "33e940db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "30\n",
      "60\n"
     ]
    }
   ],
   "source": [
    "# Method overloading using default arguments\n",
    "\n",
    "class Calculator:\n",
    "\n",
    "    def add(self, a, b=0, c=0):\n",
    "        return a + b + c\n",
    "\n",
    "\n",
    "calculator = Calculator()\n",
    "\n",
    "print(calculator.add(10))\n",
    "print(calculator.add(10, 20))\n",
    "print(calculator.add(10, 20, 30))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "777a0ee8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Animal makes a sound\n",
      "Dog barks\n"
     ]
    }
   ],
   "source": [
    "# Method overriding\n",
    "\n",
    "class Animal:\n",
    "\n",
    "    def sound(self):\n",
    "        print(\"Animal makes a sound\")\n",
    "\n",
    "\n",
    "class Dog(Animal):\n",
    "\n",
    "    def sound(self):\n",
    "        print(\"Dog barks\")\n",
    "\n",
    "\n",
    "animal = Animal()\n",
    "dog = Dog()\n",
    "\n",
    "animal.sound()\n",
    "dog.sound()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "547110f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total marks: 170\n"
     ]
    }
   ],
   "source": [
    "# Operator overloading\n",
    "\n",
    "class Student:\n",
    "\n",
    "    def __init__(self, marks):\n",
    "        self.marks = marks\n",
    "\n",
    "    def __add__(self, other):\n",
    "        return self.marks + other.marks\n",
    "\n",
    "\n",
    "student1 = Student(80)\n",
    "student2 = Student(90)\n",
    "\n",
    "print(\"Total marks:\", student1 + student2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2f84cdcd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "4\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "# Function polymorphism\n",
    "\n",
    "print(len(\"Python\"))\n",
    "print(len([10, 20, 30, 40]))\n",
    "print(len((1, 2, 3)))\n",
    "print(len({\"name\": \"Bhavana\", \"age\": 22}))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "07bfc2d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "30\n",
      "y\n"
     ]
    }
   ],
   "source": [
    "# Function polymorphism\n",
    "\n",
    "print(max(10, 20, 30))\n",
    "print(max([10, 20, 30]))\n",
    "print(max(\"Python\"))"
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