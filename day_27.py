{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d7ab9ccf",
   "metadata": {},
   "source": [
    "# INHERITANCE\n",
    "\n",
    "Inheritance is an OOP concept in which one class acquires the\n",
    "properties and methods of another class.\n",
    "\n",
    "The class that provides the properties and methods is called the\n",
    "Parent Class or Base Class.\n",
    "\n",
    "The class that inherits the properties and methods is called the\n",
    "Child Class or Derived Class.\n",
    "\n",
    "## SYNTAX\n",
    "\n",
    "class Parent:\n",
    "    # properties and methods\n",
    "\n",
    "class Child(Parent):\n",
    "    # properties and methods\n",
    "\n",
    "## TYPES OF INHERITANCE\n",
    "\n",
    "### 1. Single Inheritance\n",
    "A child class inherits from only one parent class.\n",
    "\n",
    "### 2. Multiple Inheritance\n",
    "A child class inherits from more than one parent class.\n",
    "\n",
    "### 3. Multilevel Inheritance\n",
    "A class inherits from a child class, forming multiple levels.\n",
    "\n",
    "### 4. Hierarchical Inheritance\n",
    "Multiple child classes inherit from the same parent class.\n",
    "\n",
    "### 5. Hybrid Inheritance\n",
    "A combination of two or more types of inheritance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0e4c613d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vehicle starts\n",
      "Car is driving\n"
     ]
    }
   ],
   "source": [
    "# Single inheritance\n",
    "\n",
    "class Vehicle:\n",
    "\n",
    "    def start(self):\n",
    "        print(\"Vehicle starts\")\n",
    "\n",
    "\n",
    "class Car(Vehicle):\n",
    "\n",
    "    def drive(self):\n",
    "        print(\"Car is driving\")\n",
    "\n",
    "\n",
    "car = Car()\n",
    "\n",
    "car.start()\n",
    "car.drive()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "aba52c02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Father's property\n",
      "Mother's property\n",
      "Child's property\n"
     ]
    }
   ],
   "source": [
    "# Multiple inheritance\n",
    "\n",
    "class Father:\n",
    "\n",
    "    def father_property(self):\n",
    "        print(\"Father's property\")\n",
    "\n",
    "\n",
    "class Mother:\n",
    "\n",
    "    def mother_property(self):\n",
    "        print(\"Mother's property\")\n",
    "\n",
    "\n",
    "class Child(Father, Mother):\n",
    "\n",
    "    def child_property(self):\n",
    "        print(\"Child's property\")\n",
    "\n",
    "\n",
    "child = Child()\n",
    "\n",
    "child.father_property()\n",
    "child.mother_property()\n",
    "child.child_property()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "eff77470",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Family name is inherited\n",
      "Parent's property\n",
      "Child's property\n"
     ]
    }
   ],
   "source": [
    "# Multilevel inheritance\n",
    "\n",
    "class Grandparent:\n",
    "\n",
    "    def family_name(self):\n",
    "        print(\"Family name is inherited\")\n",
    "\n",
    "\n",
    "class Parent(Grandparent):\n",
    "\n",
    "    def parent_property(self):\n",
    "        print(\"Parent's property\")\n",
    "\n",
    "\n",
    "class Child(Parent):\n",
    "\n",
    "    def child_property(self):\n",
    "        print(\"Child's property\")\n",
    "\n",
    "\n",
    "child = Child()\n",
    "\n",
    "child.family_name()\n",
    "child.parent_property()\n",
    "child.child_property()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7972111e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee is working\n",
      "Developer is writing code\n",
      "Employee is working\n",
      "Tester is testing the application\n"
     ]
    }
   ],
   "source": [
    "# Hierarchical inheritance\n",
    "\n",
    "class Employee:\n",
    "\n",
    "    def work(self):\n",
    "        print(\"Employee is working\")\n",
    "\n",
    "\n",
    "class Developer(Employee):\n",
    "\n",
    "    def write_code(self):\n",
    "        print(\"Developer is writing code\")\n",
    "\n",
    "\n",
    "class Tester(Employee):\n",
    "\n",
    "    def test_application(self):\n",
    "        print(\"Tester is testing the application\")\n",
    "\n",
    "\n",
    "developer = Developer()\n",
    "tester = Tester()\n",
    "\n",
    "developer.work()\n",
    "developer.write_code()\n",
    "\n",
    "tester.work()\n",
    "tester.test_application()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "76c9097b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee works in the company\n",
      "Developer writes code\n",
      "Tester tests code\n",
      "Team Lead manages the team\n"
     ]
    }
   ],
   "source": [
    "# Hybrid inheritance\n",
    "\n",
    "class Employee:\n",
    "\n",
    "    def employee_details(self):\n",
    "        print(\"Employee works in the company\")\n",
    "\n",
    "\n",
    "class Developer(Employee):\n",
    "\n",
    "    def write_code(self):\n",
    "        print(\"Developer writes code\")\n",
    "\n",
    "\n",
    "class Tester(Employee):\n",
    "\n",
    "    def test_code(self):\n",
    "        print(\"Tester tests code\")\n",
    "\n",
    "\n",
    "class TeamLead(Developer, Tester):\n",
    "\n",
    "    def manage_team(self):\n",
    "        print(\"Team Lead manages the team\")\n",
    "\n",
    "\n",
    "team_lead = TeamLead()\n",
    "\n",
    "team_lead.employee_details()\n",
    "team_lead.write_code()\n",
    "team_lead.test_code()\n",
    "team_lead.manage_team()"
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