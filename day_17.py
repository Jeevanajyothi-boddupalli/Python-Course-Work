{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5c770ebb",
   "metadata": {},
   "source": [
    "## SCOPE\n",
    "\n",
    "- Scope refers to the region of a program where a variable or name can be accessed.\n",
    "- The scope of a variable determines where it can be used.\n",
    "- In Python, variables can have different scopes depending on where they are created.\n",
    "\n",
    "## TYPES OF SCOPE\n",
    "\n",
    "### 1. LOCAL SCOPE\n",
    "\n",
    "- A variable created inside a function has local scope.\n",
    "- It can be accessed only within that function.\n",
    "- It cannot be directly accessed outside the function.\n",
    "\n",
    "### 2. GLOBAL SCOPE\n",
    "\n",
    "- A variable created outside all functions has global scope.\n",
    "- It can be accessed throughout the program.\n",
    "- A global variable can be accessed inside functions.\n",
    "\n",
    "### 3. ENCLOSING SCOPE\n",
    "\n",
    "- Occurs when a function is defined inside another function.\n",
    "- A variable in the outer function has enclosing scope for the inner function.\n",
    "- The inner function can access variables of the outer function.\n",
    "\n",
    "### 4. BUILT-IN SCOPE\n",
    "\n",
    "- Contains names already provided by Python.\n",
    "- These names can be used anywhere in the program.\n",
    "- Examples: `print()`, `len()`, `sum()`, `type()`, `range()`\n",
    "\n",
    "## LEGB RULE\n",
    "\n",
    "Python searches for a variable in the following order:\n",
    "\n",
    "- **L - Local:** Inside the current function\n",
    "- **E - Enclosing:** Inside the enclosing/outer function\n",
    "- **G - Global:** At the program level\n",
    "- **B - Built-in:** Names provided by Python\n",
    "\n",
    "## GLOBAL KEYWORD\n",
    "\n",
    "- The `global` keyword is used to modify a global variable inside a function.\n",
    "- Without the `global` keyword, assigning a value to a variable inside a function creates a local variable.\n",
    "\n",
    "## NONLOCAL KEYWORD\n",
    "\n",
    "- The `nonlocal` keyword is used inside a nested function.\n",
    "- It allows the inner function to modify a variable belonging to the enclosing function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8365dd95",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bhavana\n"
     ]
    }
   ],
   "source": [
    "# LOCAL SCOPE\n",
    "\n",
    "def display():\n",
    "    name = \"Jeevana\"\n",
    "    print(name)\n",
    "\n",
    "display()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "301ffd0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jeevana\n",
      "Jeevana\n"
     ]
    }
   ],
   "source": [
    "# GLOBAL SCOPE\n",
    "\n",
    "name = \"Jeevana\"\n",
    "\n",
    "def display():\n",
    "    print(name)\n",
    "\n",
    "display()\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4b183173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Local: Roopa\n",
      "Global: Jeevana\n"
     ]
    }
   ],
   "source": [
    "# LOCAL AND GLOBAL SCOPE\n",
    "\n",
    "name = \"Jeevana\"\n",
    "\n",
    "def display():\n",
    "    name = \"Anu\"\n",
    "    print(\"Local:\", name)\n",
    "\n",
    "display()\n",
    "print(\"Global:\", name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b0801ee0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bhavana\n"
     ]
    }
   ],
   "source": [
    "# ENCLOSING SCOPE\n",
    "\n",
    "def outer():\n",
    "    name = \"Bhavana\"\n",
    "\n",
    "    def inner():\n",
    "        print(name)\n",
    "\n",
    "    inner()\n",
    "\n",
    "outer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "47a79872",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "40\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "# BUILT-IN SCOPE\n",
    "\n",
    "numbers = [10, 20, 30, 40]\n",
    "\n",
    "print(len(numbers))\n",
    "print(max(numbers))\n",
    "print(sum(numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8075913b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "# GLOBAL KEYWORD\n",
    "\n",
    "count = 10\n",
    "\n",
    "def update():\n",
    "    global count\n",
    "    count = 20\n",
    "\n",
    "update()\n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "05bb52d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "# NONLOCAL KEYWORD\n",
    "\n",
    "def outer():\n",
    "    count = 10\n",
    "\n",
    "    def inner():\n",
    "        nonlocal count\n",
    "        count = 20\n",
    "\n",
    "    inner()\n",
    "    print(count)\n",
    "\n",
    "outer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fcc0b32b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inside function: 50\n",
      "Outside function: 100\n"
     ]
    }
   ],
   "source": [
    "# PROGRAM TO UNDERSTAND LOCAL AND GLOBAL VARIABLES\n",
    "\n",
    "x = 100\n",
    "\n",
    "def test():\n",
    "    x = 50\n",
    "    print(\"Inside function:\", x)\n",
    "\n",
    "test()\n",
    "print(\"Outside function:\", x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "baeb377a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Marks: 90\n"
     ]
    }
   ],
   "source": [
    "# PROGRAM TO MODIFY A GLOBAL VARIABLE\n",
    "\n",
    "marks = 50\n",
    "\n",
    "def update_marks():\n",
    "    global marks\n",
    "    marks = 90\n",
    "\n",
    "update_marks()\n",
    "print(\"Marks:\", marks)"
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