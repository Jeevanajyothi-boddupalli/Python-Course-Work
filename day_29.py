{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "397807ff",
   "metadata": {},
   "source": [
    "# ABSTRACTION\n",
    "\n",
    "Abstraction is an OOP concept that hides the internal implementation\n",
    "details and shows only the necessary information to the user.\n",
    "\n",
    "It helps reduce complexity and makes programs easier to use and maintain.\n",
    "\n",
    "## ABSTRACT CLASS\n",
    "\n",
    "An abstract class is a class that contains one or more abstract methods.\n",
    "\n",
    "An abstract class cannot be used to create objects directly.\n",
    "\n",
    "In Python, abstract classes can be created using the ABC module.\n",
    "\n",
    "## ABSTRACT METHOD\n",
    "\n",
    "An abstract method is a method that is declared in the parent class\n",
    "but does not contain its implementation.\n",
    "\n",
    "The child class must provide the implementation of the abstract method.\n",
    "\n",
    "## MODULES USED FOR ABSTRACTION\n",
    "\n",
    "### ABC\n",
    "ABC stands for Abstract Base Class.\n",
    "It is used to create abstract classes.\n",
    "\n",
    "### @abstractmethod\n",
    "It is a decorator used to declare a method as an abstract method.\n",
    "\n",
    "## SYNTAX\n",
    "\n",
    "from abc import ABC, abstractmethod\n",
    "\n",
    "class ClassName(ABC):\n",
    "\n",
    "    @abstractmethod\n",
    "    def method_name(self):\n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3655212a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Car starts with a key\n",
      "Bike starts with a self-start button\n"
     ]
    }
   ],
   "source": [
    "# Abstraction using Vehicle\n",
    "\n",
    "from abc import ABC, abstractmethod\n",
    "\n",
    "\n",
    "class Vehicle(ABC):\n",
    "\n",
    "    @abstractmethod\n",
    "    def start(self):\n",
    "        pass\n",
    "\n",
    "\n",
    "class Car(Vehicle):\n",
    "\n",
    "    def start(self):\n",
    "        print(\"Car starts with a key\")\n",
    "\n",
    "\n",
    "class Bike(Vehicle):\n",
    "\n",
    "    def start(self):\n",
    "        print(\"Bike starts with a self-start button\")\n",
    "\n",
    "\n",
    "car = Car()\n",
    "bike = Bike()\n",
    "\n",
    "car.start()\n",
    "bike.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f010d65c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Paid 1000 using Credit Card\n",
      "Paid 500 using UPI\n"
     ]
    }
   ],
   "source": [
    "# Abstraction using Payment\n",
    "\n",
    "from abc import ABC, abstractmethod\n",
    "\n",
    "\n",
    "class Payment(ABC):\n",
    "\n",
    "    @abstractmethod\n",
    "    def pay(self, amount):\n",
    "        pass\n",
    "\n",
    "\n",
    "class CreditCard(Payment):\n",
    "\n",
    "    def pay(self, amount):\n",
    "        print(\"Paid\", amount, \"using Credit Card\")\n",
    "\n",
    "\n",
    "class UPI(Payment):\n",
    "\n",
    "    def pay(self, amount):\n",
    "        print(\"Paid\", amount, \"using UPI\")\n",
    "\n",
    "\n",
    "card = CreditCard()\n",
    "upi = UPI()\n",
    "\n",
    "card.pay(1000)\n",
    "upi.pay(500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "740dcbcd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee works in a company\n",
      "Developer writes code\n"
     ]
    }
   ],
   "source": [
    "# Abstract class with abstract and normal methods\n",
    "\n",
    "from abc import ABC, abstractmethod\n",
    "\n",
    "\n",
    "class Employee(ABC):\n",
    "\n",
    "    def company(self):\n",
    "        print(\"Employee works in a company\")\n",
    "\n",
    "    @abstractmethod\n",
    "    def work(self):\n",
    "        pass\n",
    "\n",
    "\n",
    "class Developer(Employee):\n",
    "\n",
    "    def work(self):\n",
    "        print(\"Developer writes code\")\n",
    "\n",
    "\n",
    "developer = Developer()\n",
    "\n",
    "developer.company()\n",
    "developer.work()"
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