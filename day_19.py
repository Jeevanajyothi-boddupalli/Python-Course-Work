{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "af0dd540",
   "metadata": {},
   "source": [
    "# COMPREHENSIONS AND GENERATOR\n",
    "\n",
    "## LIST COMPREHENSION\n",
    "\n",
    "- List comprehension is a short and simple way to create a list.\n",
    "- It is used to generate a new list from an existing iterable.\n",
    "- It can contain an expression, `for` loop, and optional condition.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "[expression for item in iterable]\n",
    "\n",
    "## LIST COMPREHENSION WITH IF CONDITION\n",
    "\n",
    "- The `if` condition is used to filter elements.\n",
    "- Only elements satisfying the condition are included in the list.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "[expression for item in iterable if condition]\n",
    "\n",
    "## LIST COMPREHENSION WITH IF-ELSE CONDITION\n",
    "\n",
    "- `if-else` can be used to choose between two expressions.\n",
    "- The `if-else` condition is written before the `for` loop.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "[expression_if_true if condition else expression_if_false for item in iterable]\n",
    "\n",
    "## LIST COMPREHENSION WITH MATRIX\n",
    "\n",
    "- List comprehension can be used to create and process matrices.\n",
    "- Nested list comprehensions are used to work with rows and columns.\n",
    "\n",
    "## DICTIONARY COMPREHENSION\n",
    "\n",
    "- Dictionary comprehension is a short way to create a dictionary.\n",
    "- It creates key-value pairs using an iterable.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "{key: value for item in iterable}\n",
    "\n",
    "## SET COMPREHENSION\n",
    "\n",
    "- Set comprehension is used to create a set in a concise way.\n",
    "- It automatically removes duplicate values.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "{expression for item in iterable}\n",
    "\n",
    "## GENERATOR\n",
    "\n",
    "- A generator is a special type of iterator used to generate values one at a time.\n",
    "- Generators are memory efficient because they do not store all values at once.\n",
    "- The `yield` keyword is used to produce values from a generator.\n",
    "- A generator function returns a generator object.\n",
    "- Values are generated only when they are requested.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "def generator_function():\n",
    "    yield value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f4487cfb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25]\n"
     ]
    }
   ],
   "source": [
    "# LIST COMPREHENSION\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "squares = [x * x for x in numbers]\n",
    "\n",
    "print(squares)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3a210287",
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
    "# LIST COMPREHENSION WITH IF CONDITION\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5, 6]\n",
    "\n",
    "even = [x for x in numbers if x % 2 == 0]\n",
    "\n",
    "print(even)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "92a39436",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Odd', 'Even', 'Odd', 'Even', 'Odd']\n"
     ]
    }
   ],
   "source": [
    "# LIST COMPREHENSION WITH IF-ELSE CONDITION\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "result = [\"Even\" if x % 2 == 0 else \"Odd\" for x in numbers]\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8e4c18e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2, 4], [6, 8], [10, 12]]\n"
     ]
    }
   ],
   "source": [
    "# LIST COMPREHENSION WITH MATRIX\n",
    "\n",
    "matrix = [[1, 2], [3, 4], [5, 6]]\n",
    "\n",
    "result = [[x * 2 for x in row] for row in matrix]\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ac20d411",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n"
     ]
    }
   ],
   "source": [
    "# DICTIONARY COMPREHENSION\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "squares = {x: x * x for x in numbers}\n",
    "\n",
    "print(squares)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d7f81f57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 4, 9, 16, 25}\n"
     ]
    }
   ],
   "source": [
    "# SET COMPREHENSION\n",
    "\n",
    "numbers = [1, 2, 2, 3, 4, 4, 5]\n",
    "\n",
    "squares = {x * x for x in numbers}\n",
    "\n",
    "print(squares)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "51083cf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "# GENERATOR\n",
    "\n",
    "def numbers():\n",
    "    for i in range(1, 6):\n",
    "        yield i\n",
    "\n",
    "result = numbers()\n",
    "\n",
    "for value in result:\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6d9c7566",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n",
      "9\n",
      "16\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "# GENERATOR FOR SQUARES\n",
    "\n",
    "def squares(n):\n",
    "    for i in range(1, n + 1):\n",
    "        yield i * i\n",
    "\n",
    "for value in squares(5):\n",
    "    print(value)"
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