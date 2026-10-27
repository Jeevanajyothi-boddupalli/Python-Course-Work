{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ded3b86e",
   "metadata": {},
   "source": [
    "## FUNCTIONS\n",
    "\n",
    "- A function is a block of reusable code that performs a specific task.\n",
    "- Functions help to divide a large program into smaller and manageable parts.\n",
    "- A function is executed when it is called.\n",
    "- Functions improve code reusability, readability, and maintainability.\n",
    "\n",
    "## WHY FUNCTIONS?\n",
    "\n",
    "- Code reusability\n",
    "- Reduces code repetition\n",
    "- Makes programs easier to understand\n",
    "- Makes debugging easier\n",
    "- Helps divide a large program into smaller modules\n",
    "- Makes code easier to maintain\n",
    "\n",
    "## TYPES OF FUNCTIONS\n",
    "\n",
    "### 1. BUILT-IN FUNCTIONS\n",
    "\n",
    "- Functions already provided by Python.\n",
    "- Examples: `print()`, `len()`, `max()`, `min()`, `sum()`, `type()`\n",
    "\n",
    "### 2. USER-DEFINED FUNCTIONS\n",
    "\n",
    "- Functions created by the programmer according to the requirement.\n",
    "- Defined using the `def` keyword.\n",
    "\n",
    "## USER-DEFINED FUNCTION SYNTAX\n",
    "\n",
    "def function_name(parameters):\n",
    "    statements\n",
    "    return value\n",
    "\n",
    "## TYPES OF USER-DEFINED FUNCTIONS\n",
    "\n",
    "### 1. WITHOUT ARGUMENTS AND WITHOUT RETURN VALUE\n",
    "\n",
    "- Function does not accept any arguments.\n",
    "- Function does not return a value.\n",
    "\n",
    "### 2. WITH ARGUMENTS AND WITHOUT RETURN VALUE\n",
    "\n",
    "- Function accepts arguments.\n",
    "- Function performs an operation but does not return a value.\n",
    "\n",
    "### 3. WITHOUT ARGUMENTS AND WITH RETURN VALUE\n",
    "\n",
    "- Function does not accept arguments.\n",
    "- Function returns a value using `return`.\n",
    "\n",
    "### 4. WITH ARGUMENTS AND WITH RETURN VALUE\n",
    "\n",
    "- Function accepts arguments.\n",
    "- Function performs an operation and returns a value.\n",
    "\n",
    "\n",
    "## TYPES OF ARGUMENTS\n",
    "\n",
    "Based on how arguments are passed to a function, functions can be classified into five types.\n",
    "\n",
    "### 1. POSITIONAL ARGUMENTS\n",
    "\n",
    "- Arguments are passed according to the position of the parameters.\n",
    "- The order of arguments is important.\n",
    "\n",
    "### 2. KEYWORD ARGUMENTS\n",
    "\n",
    "- Arguments are passed using parameter names.\n",
    "- The order of arguments is not important.\n",
    "\n",
    "### 3. DEFAULT ARGUMENTS\n",
    "\n",
    "- Parameters are assigned default values.\n",
    "- The default value is used when an argument is not provided.\n",
    "\n",
    "### 4. VARIABLE-LENGTH ARGUMENTS\n",
    "\n",
    "- Used when the number of positional arguments is not fixed.\n",
    "- Represented using `*args`.\n",
    "- Multiple positional arguments can be passed.\n",
    "\n",
    "### 5. VARIABLE-LENGTH KEYWORD ARGUMENTS\n",
    "\n",
    "- Used when the number of keyword arguments is not fixed.\n",
    "- Represented using `**kwargs`.\n",
    "- Multiple keyword arguments can be passed as key-value pairs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b4270731",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length: 5\n",
      "Maximum: 50\n",
      "Minimum: 10\n",
      "Sum: 150\n"
     ]
    }
   ],
   "source": [
    "# BUILT-IN FUNCTION\n",
    "\n",
    "numbers = [10, 20, 30, 40, 50]\n",
    "\n",
    "print(\"Length:\", len(numbers))\n",
    "print(\"Maximum:\", max(numbers))\n",
    "print(\"Minimum:\", min(numbers))\n",
    "print(\"Sum:\", sum(numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0f118e60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Welcome to Python\n"
     ]
    }
   ],
   "source": [
    "# USER-DEFINED FUNCTION - WITHOUT ARGUMENTS AND WITHOUT RETURN VALUE\n",
    "\n",
    "def greet():\n",
    "    print(\"Hello, Welcome to Python\")\n",
    "\n",
    "greet()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ff291dbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum = 30\n"
     ]
    }
   ],
   "source": [
    "# USER-DEFINED FUNCTION - WITH ARGUMENTS AND WITHOUT RETURN VALUE\n",
    "\n",
    "def addition(a, b):\n",
    "    print(\"Sum =\", a + b)\n",
    "\n",
    "addition(10, 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a59208a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number = 100\n"
     ]
    }
   ],
   "source": [
    "# USER-DEFINED FUNCTION - WITHOUT ARGUMENTS AND WITH RETURN VALUE\n",
    "\n",
    "def get_number():\n",
    "    return 100\n",
    "\n",
    "result = get_number()\n",
    "print(\"Number =\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6f1f0ead",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result = 20\n"
     ]
    }
   ],
   "source": [
    "# USER-DEFINED FUNCTION - WITH ARGUMENTS AND WITH RETURN VALUE\n",
    "\n",
    "def multiply(a, b):\n",
    "    return a * b\n",
    "\n",
    "result = multiply(5, 4)\n",
    "print(\"Result =\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "892d3562",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Bhavana\n",
      "Age: 21\n"
     ]
    }
   ],
   "source": [
    "# POSITIONAL ARGUMENTS\n",
    "\n",
    "def student(name, age):\n",
    "    print(\"Name:\", name)\n",
    "    print(\"Age:\", age)\n",
    "\n",
    "student(\"Bhavana\", 21)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d303d2be",
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
    "# KEYWORD ARGUMENTS\n",
    "\n",
    "def student(name, age):\n",
    "    print(\"Name:\", name)\n",
    "    print(\"Age:\", age)\n",
    "\n",
    "student(age=23, name=\"Jeevana\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f6b405fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Jeevana\n",
      "Company: TCS\n",
      "Name: Anu\n",
      "Company: Infosys\n"
     ]
    }
   ],
   "source": [
    "# DEFAULT ARGUMENTS\n",
    "\n",
    "def employee(name, company=\"TCS\"):\n",
    "    print(\"Name:\", name)\n",
    "    print(\"Company:\", company)\n",
    "\n",
    "employee(\"Jeevana\")\n",
    "employee(\"Anu\", \"Infosys\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dd50d891",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arguments: (10, 20)\n",
      "Sum = 30\n",
      "Arguments: (10, 20, 30, 40)\n",
      "Sum = 100\n"
     ]
    }
   ],
   "source": [
    "# VARIABLE-LENGTH ARGUMENTS\n",
    "\n",
    "def addition(*args):\n",
    "    print(\"Arguments:\", args)\n",
    "    print(\"Sum =\", sum(args))\n",
    "\n",
    "addition(10, 20)\n",
    "addition(10, 20, 30, 40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bd65f467",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name : Jeevana\n",
      "age : 23\n",
      "course : Python\n"
     ]
    }
   ],
   "source": [
    "# VARIABLE-LENGTH KEYWORD ARGUMENTS\n",
    "\n",
    "def student(**kwargs):\n",
    "    for key, value in kwargs.items():\n",
    "        print(key, \":\", value)\n",
    "\n",
    "student(name=\"Jeevana\", age=21, course=\"Python\")"
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