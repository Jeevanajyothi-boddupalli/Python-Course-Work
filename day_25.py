{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "08ff51bb",
   "metadata": {},
   "source": [
    "# INTRODUCTION TO OOP CONCEPTS\n",
    "\n",
    "## WHAT IS OOP?\n",
    "\n",
    "OOP stands for Object-Oriented Programming.\n",
    "\n",
    "Object-Oriented Programming is a programming approach based on\n",
    "classes and objects. It helps organize programs by combining\n",
    "data and functions into a single unit.\n",
    "\n",
    "## OOP CONCEPTS\n",
    "\n",
    "The main concepts of OOP are:\n",
    "\n",
    "1. Class\n",
    "2. Object\n",
    "3. Encapsulation\n",
    "4. Inheritance\n",
    "5. Polymorphism\n",
    "6. Abstraction\n",
    "\n",
    "## CLASS\n",
    "\n",
    "A class is a blueprint or template used to create objects.\n",
    "It defines the attributes and methods that an object can have.\n",
    "\n",
    "## OBJECT\n",
    "\n",
    "An object is an instance of a class.\n",
    "It is used to access the attributes and methods defined in the class.\n",
    "\n",
    "## CONSTRUCTOR\n",
    "\n",
    "A constructor is a special method that is automatically called\n",
    "when an object is created.\n",
    "\n",
    "In Python, the constructor is represented by __init__().\n",
    "\n",
    "## SYNTAX FOR CREATING A CLASS\n",
    "\n",
    "class ClassName:\n",
    "    # attributes and methods\n",
    "\n",
    "\n",
    "## SYNTAX FOR CREATING AN OBJECT\n",
    "\n",
    "object_name = ClassName()\n",
    "\n",
    "\n",
    "## SYNTAX FOR CREATING A CONSTRUCTOR\n",
    "\n",
    "class ClassName:\n",
    "\n",
    "    def __init__(self):\n",
    "        # initialization code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "789c7d86",
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
    "# Creating a simple class\n",
    "\n",
    "class Student:\n",
    "    name = \"Jeevana\"\n",
    "    age = 23\n",
    "\n",
    "print(Student.name)\n",
    "print(Student.age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cc930a3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jeevanaa\n",
      "23\n"
     ]
    }
   ],
   "source": [
    "# Creating an object\n",
    "\n",
    "class Student:\n",
    "    name = \"Jeevana\"\n",
    "    age = 23\n",
    "\n",
    "student1 = Student()\n",
    "\n",
    "print(student1.name)\n",
    "print(student1.age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c737b02b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student details\n"
     ]
    }
   ],
   "source": [
    "# Class with method\n",
    "\n",
    "class Student:\n",
    "\n",
    "    def display(self):\n",
    "        print(\"Student details\")\n",
    "\n",
    "student1 = Student()\n",
    "\n",
    "student1.display()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d84e1d09",
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
    "# Class with constructor\n",
    "\n",
    "class Student:\n",
    "\n",
    "    def __init__(self, name, age):\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "\n",
    "student1 = Student(\"Jeevana\", 23)\n",
    "\n",
    "print(\"Name:\", student1.name)\n",
    "print(\"Age:\", student1.age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2ba2fb23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Jeevana\n",
      "Salary: 60000\n"
     ]
    }
   ],
   "source": [
    "# Class, object and constructor\n",
    "\n",
    "class Employee:\n",
    "\n",
    "    def __init__(self, name, salary):\n",
    "        self.name = name\n",
    "        self.salary = salary\n",
    "\n",
    "    def display(self):\n",
    "        print(\"Name:\", self.name)\n",
    "        print(\"Salary:\", self.salary)\n",
    "\n",
    "\n",
    "employee1 = Employee(\"Jeevanaa\", 60000)\n",
    "\n",
    "employee1.display()"
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