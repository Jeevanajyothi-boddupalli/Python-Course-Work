{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c485207a",
   "metadata": {},
   "source": [
    "## MODULES\n",
    "\n",
    "- A module is a Python file containing functions, classes, variables, and statements.\n",
    "- A module is saved with the `.py` extension.\n",
    "- Modules help to organize Python programs into separate files.\n",
    "- Python provides many built-in modules, and we can also create our own modules.\n",
    "\n",
    "## WHY MODULES?\n",
    "\n",
    "- Code reusability\n",
    "- Reduces code duplication\n",
    "- Organizes large programs\n",
    "- Makes code easier to maintain\n",
    "- Provides ready-to-use functions and classes\n",
    "- Helps divide a large program into smaller files\n",
    "\n",
    "## TYPES OF MODULES\n",
    "\n",
    "### 1. BUILT-IN MODULES\n",
    "\n",
    "- Modules provided by Python.\n",
    "- Examples: `math`, `random`, `datetime`, `os`\n",
    "\n",
    "### 2. USER-DEFINED MODULES\n",
    "\n",
    "- Modules created by the programmer.\n",
    "- Any Python file can be used as a module.\n",
    "\n",
    "### 3. THIRD-PARTY MODULES\n",
    "\n",
    "- Modules developed by external developers or organizations.\n",
    "- They are usually installed using `pip`.\n",
    "- Examples: `numpy`, `pandas`, `requests`\n",
    "\n",
    "## DIFFERENT WAYS OF IMPORTING MODULES\n",
    "\n",
    "### 1. IMPORT ENTIRE MODULE\n",
    "\n",
    "import module_name\n",
    "\n",
    "### 2. IMPORT WITH ALIAS\n",
    "\n",
    "import module_name as alias\n",
    "\n",
    "### 3. IMPORT SPECIFIC FUNCTION\n",
    "\n",
    "from module_name import function_name\n",
    "\n",
    "### 4. IMPORT MULTIPLE FUNCTIONS\n",
    "\n",
    "from module_name import function1, function2\n",
    "\n",
    "### 5. IMPORT ALL\n",
    "\n",
    "from module_name import *\n",
    "\n",
    "## USING FUNCTIONS FROM A MODULE\n",
    "\n",
    "- When an entire module is imported, the module name is used with the dot operator.\n",
    "- Example: `math.sqrt(25)`\n",
    "\n",
    "## SIMPLE CALCULATOR USING MODULES\n",
    "\n",
    "- A calculator can be created by defining arithmetic operations in a separate Python file.\n",
    "- The calculator module can then be imported into another Python program.\n",
    "- This demonstrates code reusability and user-defined modules."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ce213d66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square root: 5.0\n",
      "Power: 8.0\n",
      "Factorial: 120\n"
     ]
    }
   ],
   "source": [
    "# BUILT-IN MODULE\n",
    "\n",
    "import math\n",
    "\n",
    "print(\"Square root:\", math.sqrt(25))\n",
    "print(\"Power:\", math.pow(2, 3))\n",
    "print(\"Factorial:\", math.factorial(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c7e9b223",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square root: 6.0\n",
      "Value of pi: 3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "# IMPORT MODULE WITH ALIAS\n",
    "\n",
    "import math as m\n",
    "\n",
    "print(\"Square root:\", m.sqrt(36))\n",
    "print(\"Value of pi:\", m.pi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bb7cf5e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square root: 7.0\n"
     ]
    }
   ],
   "source": [
    "# IMPORT SPECIFIC FUNCTION\n",
    "\n",
    "from math import sqrt\n",
    "\n",
    "print(\"Square root:\", sqrt(49))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0ad9dac4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square root: 8.0\n",
      "Factorial: 120\n"
     ]
    }
   ],
   "source": [
    "# IMPORT MULTIPLE FUNCTIONS\n",
    "\n",
    "from math import sqrt, factorial\n",
    "\n",
    "print(\"Square root:\", sqrt(64))\n",
    "print(\"Factorial:\", factorial(5))"
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