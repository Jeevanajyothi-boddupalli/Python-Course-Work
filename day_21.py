{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d76c3842",
   "metadata": {},
   "source": [
    "# BUILT-IN MODULES\n",
    "\n",
    "Built-in modules are modules that are already available in Python.\n",
    "They provide useful functions and features for performing common tasks.\n",
    "\n",
    "## IMPORTANT BUILT-IN MODULES\n",
    "\n",
    "### 1. math\n",
    "The math module provides mathematical functions such as square root,\n",
    "factorial, power, floor, and ceiling.\n",
    "\n",
    "### 2. random\n",
    "The random module is used to generate random numbers and select\n",
    "random elements from sequences.\n",
    "\n",
    "### 3. sys\n",
    "The sys module provides functions and variables related to the\n",
    "Python interpreter and system environment.\n",
    "\n",
    "### 4. platform\n",
    "The platform module provides information about the operating system,\n",
    "machine, processor, and Python version.\n",
    "\n",
    "### 5. collections\n",
    "The collections module provides specialized container datatypes\n",
    "such as Counter, defaultdict, and deque.\n",
    "\n",
    "### 6. itertools\n",
    "The itertools module provides functions for creating and working\n",
    "with iterators efficiently.\n",
    "\n",
    "### 7. datetime\n",
    "The datetime module is used to work with dates and times."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d564c7de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square root: 5.0\n",
      "Power: 8.0\n",
      "Factorial: 120\n",
      "Ceiling: 5\n",
      "Floor: 4\n"
     ]
    }
   ],
   "source": [
    "# Math module\n",
    "\n",
    "import math\n",
    "\n",
    "num = 25\n",
    "\n",
    "print(\"Square root:\", math.sqrt(num))\n",
    "print(\"Power:\", math.pow(2, 3))\n",
    "print(\"Factorial:\", math.factorial(5))\n",
    "print(\"Ceiling:\", math.ceil(4.3))\n",
    "print(\"Floor:\", math.floor(4.8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4549b72f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random integer: 89\n",
      "Random choice: 20\n",
      "Random choices: [50, 20, 50]\n",
      "Random sample: [50, 40, 10]\n",
      "Shuffled list: [20, 40, 10, 50, 30]\n"
     ]
    }
   ],
   "source": [
    "# Random module\n",
    "\n",
    "import random\n",
    "\n",
    "numbers = [10, 20, 30, 40, 50]\n",
    "\n",
    "# randint() - generates a random integer within a range\n",
    "print(\"Random integer:\", random.randint(1, 100))\n",
    "\n",
    "# choice() - selects one random element\n",
    "print(\"Random choice:\", random.choice(numbers))\n",
    "\n",
    "# choices() - selects multiple random elements\n",
    "print(\"Random choices:\", random.choices(numbers, k=3))\n",
    "\n",
    "# sample() - selects multiple unique random elements\n",
    "print(\"Random sample:\", random.sample(numbers, k=3))\n",
    "\n",
    "# shuffle() - randomly rearranges the elements\n",
    "random.shuffle(numbers)\n",
    "print(\"Shuffled list:\", numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92be1792",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sys module\n",
    "\n",
    "import sys\n",
    "\n",
    "print(\"Python version:\", sys.version)\n",
    "print(\"Platform:\", sys.platform)\n",
    "print(\"Python executable:\", sys.executable)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1f10243b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Frequency of elements: Counter({4: 4, 3: 3, 2: 2, 1: 1})\n"
     ]
    }
   ],
   "source": [
    "# Collections module\n",
    "\n",
    "from collections import Counter\n",
    "\n",
    "numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]\n",
    "\n",
    "count = Counter(numbers)\n",
    "\n",
    "print(\"Frequency of elements:\", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59da9c7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Datetime module\n",
    "\n",
    "import datetime\n",
    "\n",
    "current = datetime.datetime.now()\n",
    "\n",
    "print(\"Current date and time:\", current)\n",
    "print(\"Date:\", current.date())\n",
    "print(\"Time:\", current.time())"
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