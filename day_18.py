{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ba9a8d34",
   "metadata": {},
   "source": [
    "# RECURSION, LAMBDA FUNCTIONS AND HIGHER ORDER FUNCTIONS\n",
    "\n",
    "## RECURSION\n",
    "\n",
    "- Recursion is a process in which a function calls itself.\n",
    "- A recursive function solves a problem by breaking it into smaller versions of the same problem.\n",
    "- Every recursive function must have a **base condition** to stop the recursion.\n",
    "\n",
    "## SYNTAX\n",
    "\n",
    "def function(parameters):\n",
    "    if base_condition:\n",
    "        return value\n",
    "    else:\n",
    "        return function(modified_parameters)\n",
    "\n",
    "## POINTS TO REMEMBER WHILE USING RECURSION\n",
    "\n",
    "- A base condition is compulsory.\n",
    "- The recursive call should move towards the base condition.\n",
    "- Without a proper base condition, infinite recursion may occur.\n",
    "- Each recursive call creates a new function call.\n",
    "- Recursion can be used as an alternative to loops for certain problems.\n",
    "- Excessive recursion can consume more memory.\n",
    "\n",
    "## TYPES OF RECURSIVE FUNCTIONS\n",
    "\n",
    "### 1. DIRECT RECURSION\n",
    "\n",
    "- A function directly calls itself.\n",
    "- Example: `function()` calls `function()`.\n",
    "\n",
    "### 2. INDIRECT RECURSION\n",
    "\n",
    "- Two or more functions call each other.\n",
    "- Example: `function1()` calls `function2()` and `function2()` calls `function1()`.\n",
    "\n",
    "## LAMBDA FUNCTIONS\n",
    "\n",
    "- A lambda function is a small anonymous function.\n",
    "- It is created using the `lambda` keyword.\n",
    "- It can take any number of arguments but contains only one expression.\n",
    "- Lambda functions are generally used for short and simple operations.\n",
    "\n",
    "## SYNTAX\n",
    "\n",
    "lambda arguments: expression\n",
    "\n",
    "## ANONYMOUS FUNCTION\n",
    "\n",
    "- A lambda function is called an anonymous function because it does not require a function name using `def`.\n",
    "- It can be assigned to a variable or directly passed to another function.\n",
    "\n",
    "## HIGHER ORDER FUNCTIONS\n",
    "\n",
    "- A higher order function is a function that accepts another function as an argument or returns a function as its result.\n",
    "- Higher order functions are commonly used with lambda functions.\n",
    "- Examples: `map()`, `filter()`, `reduce()`, and `sorted()` with a key function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cc067447",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# DIRECT RECURSION\n",
    "\n",
    "def countdown(n):\n",
    "    if n == 0:\n",
    "        return\n",
    "    print(n)\n",
    "    countdown(n - 1)\n",
    "\n",
    "countdown(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "533cdf2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial: 120\n"
     ]
    }
   ],
   "source": [
    "# FACTORIAL USING RECURSION\n",
    "\n",
    "def factorial(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return 1\n",
    "    return n * factorial(n - 1)\n",
    "\n",
    "print(\"Factorial:\", factorial(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "46963efe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum: 15\n"
     ]
    }
   ],
   "source": [
    "# SUM OF NUMBERS USING RECURSION\n",
    "\n",
    "def sum_numbers(n):\n",
    "    if n == 0:\n",
    "        return 0\n",
    "    return n + sum_numbers(n - 1)\n",
    "\n",
    "print(\"Sum:\", sum_numbers(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f17b91bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 "
     ]
    }
   ],
   "source": [
    "# FIBONACCI SERIES USING RECURSION\n",
    "\n",
    "def fibonacci(n):\n",
    "    if n <= 1:\n",
    "        return n\n",
    "    return fibonacci(n - 1) + fibonacci(n - 2)\n",
    "\n",
    "for i in range(7):\n",
    "    print(fibonacci(i), end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5f34ffdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# INDIRECT RECURSION\n",
    "\n",
    "def function1(n):\n",
    "    if n > 0:\n",
    "        print(n)\n",
    "        function2(n - 1)\n",
    "\n",
    "def function2(n):\n",
    "    if n > 0:\n",
    "        print(n)\n",
    "        function1(n - 1)\n",
    "\n",
    "function1(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6790fd17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "# LAMBDA FUNCTION\n",
    "\n",
    "square = lambda x: x * x\n",
    "\n",
    "print(square(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bd2d2d05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "# LAMBDA FUNCTION WITH MULTIPLE ARGUMENTS\n",
    "\n",
    "addition = lambda a, b: a + b\n",
    "\n",
    "print(addition(10, 20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "66370bef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "# HIGHER ORDER FUNCTION - FUNCTION AS AN ARGUMENT\n",
    "\n",
    "def calculate(operation, a, b):\n",
    "    return operation(a, b)\n",
    "\n",
    "addition = lambda x, y: x + y\n",
    "\n",
    "print(calculate(addition, 10, 20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0b5c3d40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "# MAP() - HIGHER ORDER FUNCTION\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "result = list(map(lambda x: x * 2, numbers))\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1704472b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6]\n"
     ]
    }
   ],
   "source": [
    "# FILTER() - HIGHER ORDER FUNCTION\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5, 6]\n",
    "\n",
    "result = list(filter(lambda x: x % 2 == 0, numbers))\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "073a2f01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "# REDUCE() - HIGHER ORDER FUNCTION\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "result = reduce(lambda x, y: x + y, numbers)\n",
    "\n",
    "print(result)"
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