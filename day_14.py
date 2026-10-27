{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f5075281",
   "metadata": {},
   "source": [
    "# NESTED LOOPS\n",
    "\n",
    "## NESTED LOOPS\n",
    "\n",
    "- A nested loop is a loop inside another loop.\n",
    "- The outer loop controls the execution of the inner loop.\n",
    "- The inner loop executes completely for every iteration of the outer loop.\n",
    "- Nested loops can be created using `for` and `while` loops.\n",
    "- They are mainly used for patterns, tables, matrices, and repeated combinations.\n",
    "\n",
    "## SYNTAX OF NESTED FOR LOOP\n",
    "\n",
    "for variable1 in sequence:\n",
    "    for variable2 in sequence:\n",
    "        statement\n",
    "\n",
    "## SYNTAX OF NESTED WHILE LOOP\n",
    "\n",
    "while condition1:\n",
    "    while condition2:\n",
    "        statement\n",
    "\n",
    "## IMPORTANT POINTS\n",
    "\n",
    "- The inner loop runs completely for each iteration of the outer loop.\n",
    "- Proper indentation is required.\n",
    "- `break` and `continue` can be used inside nested loops.\n",
    "- Nested loops can have more than two levels.\n",
    "- Nested loops are commonly used for rows and columns, patterns, and matrix operations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cca6aa26",
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
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "M=[[1,2,3],[4,5,6],[7,8,9]]\n",
    "for row in range(3):\n",
    "    for column in range(3):\n",
    "        print(M[row][column])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6cede34a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* * * * \n",
      "* * * * \n",
      "* * * * \n",
      "* * * * \n"
     ]
    }
   ],
   "source": [
    "for row in range(4):\n",
    "    for column in range(4):\n",
    "        print(\"*\", end=\" \")\n",
    "    print()  # Print a newline after each row\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cb784135",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*       * \n",
      "  *   *   \n",
      "    *     \n",
      "  *   *   \n",
      "*       * \n"
     ]
    }
   ],
   "source": [
    "n=5\n",
    "for r in range(n):\n",
    "    for c in range(n):\n",
    "        if r==c or (r+c)==n-1:\n",
    "            print(\"*\", end=\" \")\n",
    "        else:\n",
    "            print(\" \", end=\" \")\n",
    "    print()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19da7e74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    *     \n",
      "    *     \n",
      "* * * * * \n",
      "    *     \n",
      "    *     \n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "for r in range(n):\n",
    "    for c in range(n):\n",
    "        if r==(n//2) or c==(n//2):\n",
    "            print(\"*\", end=\" \")\n",
    "        else:\n",
    "            print(\" \", end=\" \")\n",
    "    print() #input:5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2fb6e395",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 \n",
      "4 5 6 \n",
      "7 8 9 \n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "num=1\n",
    "for r in range(n):\n",
    "    for c in range(n):\n",
    "        print(num, end=\" \")\n",
    "        num += 1\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f542a533",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 0 1 0 \n",
      "0 1 0 1 \n",
      "1 0 1 0 \n",
      "0 1 0 1 \n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "for r in range(n):\n",
    "    for c in range(n):\n",
    "        if (r+c)%2==0:\n",
    "            print(\"1\", end=\" \")\n",
    "        else:\n",
    "            print(\"0\", end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d0983e1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 4 6 8 \n",
      "1 3 5 7 \n",
      "10 12 14 16 \n",
      "9 11 13 15 \n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "num1=2\n",
    "num2=1\n",
    "for r in range(n):\n",
    "    for c in range(n):\n",
    "        if r%2==0:\n",
    "            print(num1, end=\" \")\n",
    "            num1+=2\n",
    "        else:\n",
    "            print(num2, end=\" \")\n",
    "            num2+=2\n",
    "    print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f539bfb7",
   "metadata": {},
   "outputs": [],
   "source": []
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