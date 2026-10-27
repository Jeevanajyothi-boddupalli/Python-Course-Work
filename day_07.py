{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "57149a89",
   "metadata": {},
   "source": [
    "LISTS AND TUPLES\n",
    "\n",
    "## LISTS\n",
    "- Ordered collection\n",
    "- Mutable\n",
    "- Allows duplicate values\n",
    "- Different data types can be stored\n",
    "- Indexing and slicing\n",
    "\n",
    "## LIST OPERATIONS\n",
    "- Concatenation (+)\n",
    "- Repetition (*)\n",
    "- Membership (in, not in)\n",
    "- Comparison\n",
    "- Indexing\n",
    "- Slicing\n",
    "\n",
    "## LIST METHODS\n",
    "- append()\n",
    "- extend()\n",
    "- insert()\n",
    "- remove()\n",
    "- pop()\n",
    "- clear()\n",
    "- index()\n",
    "- count()\n",
    "- sort()\n",
    "- reverse()\n",
    "- copy()\n",
    "\n",
    "## BUILT-IN FUNCTIONS\n",
    "- len()\n",
    "- max()\n",
    "- min()\n",
    "- sum()\n",
    "- sorted()\n",
    "- any()\n",
    "- all()\n",
    "\n",
    "## TUPLES\n",
    "- Ordered collection\n",
    "- Immutable\n",
    "- Allows duplicate values\n",
    "- Different data types can be stored\n",
    "- Indexing and slicing\n",
    "\n",
    "## TUPLE METHODS\n",
    "- count()\n",
    "- index()\n",
    "\n",
    "## TUPLE OPERATIONS\n",
    "- Concatenation (+)\n",
    "- Repetition (*)\n",
    "- Membership (in, not in)\n",
    "- Indexing\n",
    "- Slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "42b2f59d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 20, 30, 40, 50]\n",
      "10\n",
      "50\n",
      "[20, 30, 40]\n",
      "[50, 40, 30, 20, 10]\n",
      "[10, 'Python', 20.5, True, 10]\n"
     ]
    }
   ],
   "source": [
    "# Creating a list\n",
    "my_list = [10, 20, 30, 40, 50]\n",
    "\n",
    "print(my_list)\n",
    "print(my_list[0])\n",
    "print(my_list[-1])\n",
    "\n",
    "# Slicing\n",
    "print(my_list[1:4])\n",
    "print(my_list[::-1])\n",
    "\n",
    "# Different data types and duplicates\n",
    "data = [10, \"Python\", 20.5, True, 10]\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6508d796",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6]\n",
      "[1, 2, 3, 1, 2, 3]\n",
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "l1 = [1, 2, 3]\n",
    "l2 = [4, 5, 6]\n",
    "\n",
    "# Concatenation\n",
    "print(l1 + l2)\n",
    "\n",
    "# Repetition\n",
    "print(l1 * 2)\n",
    "\n",
    "# Membership\n",
    "print(2 in l1)\n",
    "print(10 not in l1)\n",
    "\n",
    "# Comparison\n",
    "print(l1 == [1, 2, 3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2b3e6a94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30, 10, 20, 40, 50]\n",
      "[30, 10, 20, 40, 50, 60, 70]\n",
      "[30, 15, 10, 20, 40, 50, 60, 70]\n",
      "[30, 10, 20, 40, 50, 60, 70]\n",
      "70\n",
      "[30, 10, 20, 40, 50, 60]\n",
      "2\n",
      "1\n",
      "[10, 20, 30, 40, 50, 60]\n",
      "[60, 50, 40, 30, 20, 10]\n",
      "[60, 50, 40, 30, 20, 10]\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "numbers = [30, 10, 20, 40]\n",
    "\n",
    "numbers.append(50)\n",
    "print(numbers)\n",
    "\n",
    "numbers.extend([60, 70])\n",
    "print(numbers)\n",
    "\n",
    "numbers.insert(1, 15)\n",
    "print(numbers)\n",
    "\n",
    "numbers.remove(15)\n",
    "print(numbers)\n",
    "\n",
    "print(numbers.pop())\n",
    "print(numbers)\n",
    "\n",
    "print(numbers.index(20))\n",
    "print(numbers.count(20))\n",
    "\n",
    "numbers.sort()\n",
    "print(numbers)\n",
    "\n",
    "numbers.reverse()\n",
    "print(numbers)\n",
    "\n",
    "copy_list = numbers.copy()\n",
    "print(copy_list)\n",
    "\n",
    "numbers.clear()\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a7b0dbd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "50\n",
      "10\n",
      "150\n",
      "[10, 20, 30, 40, 50]\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "numbers = [10, 20, 30, 40, 50]\n",
    "\n",
    "print(len(numbers))\n",
    "print(max(numbers))\n",
    "print(min(numbers))\n",
    "print(sum(numbers))\n",
    "print(sorted(numbers))\n",
    "\n",
    "print(any([False, True, False]))\n",
    "print(all([True, True, True]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fcb710d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(10, 20, 30, 20, 40)\n",
      "10\n",
      "40\n",
      "(20, 30, 20)\n",
      "(40, 20, 30, 20, 10)\n",
      "(1, 2, 3, 4, 5, 6)\n",
      "(1, 2, 3, 1, 2, 3)\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Creating a tuple\n",
    "t = (10, 20, 30, 20, 40)\n",
    "\n",
    "print(t)\n",
    "\n",
    "# Indexing\n",
    "print(t[0])\n",
    "print(t[-1])\n",
    "\n",
    "# Slicing\n",
    "print(t[1:4])\n",
    "print(t[::-1])\n",
    "\n",
    "# Operations\n",
    "t1 = (1, 2, 3)\n",
    "t2 = (4, 5, 6)\n",
    "\n",
    "print(t1 + t2)       # Concatenation\n",
    "print(t1 * 2)        # Repetition\n",
    "print(2 in t1)       # Membership"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1960bd90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "2\n",
      "6\n",
      "40\n",
      "10\n",
      "140\n"
     ]
    }
   ],
   "source": [
    "t = (10, 20, 30, 20, 40, 20)\n",
    "\n",
    "print(t.count(20))\n",
    "print(t.index(30))\n",
    "\n",
    "print(len(t))\n",
    "print(max(t))\n",
    "print(min(t))\n",
    "print(sum(t))"
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