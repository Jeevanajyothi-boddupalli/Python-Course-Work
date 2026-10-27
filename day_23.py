{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a032b1dc",
   "metadata": {},
   "source": [
    "# EXCEPTION HANDLING AND FILE HANDLING\n",
    "\n",
    "## EXCEPTION HANDLING\n",
    "\n",
    "Exception handling is used to handle errors that occur during the\n",
    "execution of a Python program without stopping the entire program.\n",
    "\n",
    "### WHAT IS AN EXCEPTION?\n",
    "\n",
    "An exception is an error that occurs during the execution of a program.\n",
    "Python provides exception handling mechanisms to detect and handle\n",
    "these errors.\n",
    "\n",
    "### RUNTIME ERRORS\n",
    "\n",
    "Runtime errors occur while a program is running.\n",
    "\n",
    "### 1. ZeroDivisionError\n",
    "Occurs when a number is divided by zero.\n",
    "\n",
    "### 2. ValueError\n",
    "Occurs when a function receives an inappropriate value.\n",
    "\n",
    "### 3. KeyError\n",
    "Occurs when we try to access a dictionary key that does not exist.\n",
    "\n",
    "### 4. IndexError\n",
    "Occurs when we try to access an index that is outside the range\n",
    "of a sequence.\n",
    "\n",
    "### 5. FileNotFoundError\n",
    "Occurs when we try to open a file that does not exist.\n",
    "\n",
    "### 6. AttributeError\n",
    "Occurs when we try to access an attribute or method that an object\n",
    "does not have.\n",
    "\n",
    "### EXCEPTION HANDLING USING try AND except\n",
    "\n",
    "The try block contains code that may produce an exception.\n",
    "The except block is used to handle the exception.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "try:\n",
    "    # Code that may cause an exception\n",
    "except:\n",
    "    # Code to handle the exception\n",
    "\n",
    "\n",
    "## FILE HANDLING\n",
    "\n",
    "File handling is used to create, read, write, and modify files\n",
    "using Python.\n",
    "\n",
    "### FILE OPERATIONS\n",
    "\n",
    "### 1. Open\n",
    "The open() function is used to open a file.\n",
    "\n",
    "### 2. Read\n",
    "The read() function is used to read the contents of a file.\n",
    "\n",
    "### 3. Write\n",
    "The write() function is used to write data into a file.\n",
    "\n",
    "### 4. Close\n",
    "The close() function is used to close an opened file.\n",
    "\n",
    "### SYNTAX\n",
    "\n",
    "file = open(\"filename.txt\", \"mode\")\n",
    "\n",
    "### FILE MODES\n",
    "\n",
    "### r - Read Mode\n",
    "Opens a file for reading. The file must already exist.\n",
    "\n",
    "### w - Write Mode\n",
    "Opens a file for writing. Creates a new file if it does not exist.\n",
    "If the file already exists, its contents are overwritten.\n",
    "\n",
    "### a - Append Mode\n",
    "Opens a file for adding data at the end.\n",
    "Creates a new file if it does not exist.\n",
    "\n",
    "### r+ - Read and Write Mode\n",
    "Opens a file for both reading and writing.\n",
    "The file must already exist.\n",
    "\n",
    "### w+ - Write and Read Mode\n",
    "Opens a file for both writing and reading.\n",
    "Creates a new file if it does not exist and overwrites existing content.\n",
    "\n",
    "### a+ - Append and Read Mode\n",
    "Opens a file for both appending and reading.\n",
    "Creates a new file if it does not exist."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ec6fdab9",
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mZeroDivisionError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m a = \u001b[32m10\u001b[39m\n\u001b[32m      4\u001b[39m b = \u001b[32m0\u001b[39m\n\u001b[32m      5\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m print(a / b)\n",
      "\u001b[31mZeroDivisionError\u001b[39m: division by zero"
     ]
    }
   ],
   "source": [
    "# ZeroDivisionError\n",
    "\n",
    "a = 10\n",
    "b = 0\n",
    "\n",
    "print(a / b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "68e2848c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'hello'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# ValueError\u001b[39;00m\n\u001b[32m      2\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m num = int(\u001b[33m\"hello\"\u001b[39m)\n\u001b[32m      4\u001b[39m \n\u001b[32m      5\u001b[39m print(num)\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: 'hello'"
     ]
    }
   ],
   "source": [
    "# ValueError\n",
    "\n",
    "num = int(\"hello\")\n",
    "\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "80ae77e8",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'marks'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[32m      4\u001b[39m     \u001b[33m\"name\"\u001b[39m: \u001b[33m\"Bhavana\"\u001b[39m,\n\u001b[32m      5\u001b[39m     \u001b[33m\"age\"\u001b[39m: \u001b[32m22\u001b[39m\n\u001b[32m      6\u001b[39m }\n\u001b[32m      7\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m print(student[\u001b[33m\"marks\"\u001b[39m])\n",
      "\u001b[31mKeyError\u001b[39m: 'marks'"
     ]
    }
   ],
   "source": [
    "# KeyError\n",
    "\n",
    "student = {\n",
    "    \"name\": \"Bhavana\",\n",
    "    \"age\": 22\n",
    "}\n",
    "\n",
    "print(student[\"marks\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "312a7398",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mIndexError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# IndexError\u001b[39;00m\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m numbers = [\u001b[32m10\u001b[39m, \u001b[32m20\u001b[39m, \u001b[32m30\u001b[39m]\n\u001b[32m      4\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m print(numbers[\u001b[32m5\u001b[39m])\n",
      "\u001b[31mIndexError\u001b[39m: list index out of range"
     ]
    }
   ],
   "source": [
    "# IndexError\n",
    "\n",
    "numbers = [10, 20, 30]\n",
    "\n",
    "print(numbers[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "56ac15f6",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'abc.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# FileNotFoundError\u001b[39;00m\n\u001b[32m      2\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m file = open(\u001b[33m\"abc.txt\"\u001b[39m, \u001b[33m\"r\"\u001b[39m)\n\u001b[32m      4\u001b[39m \n\u001b[32m      5\u001b[39m print(file.read())\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'abc.txt'"
     ]
    }
   ],
   "source": [
    "# FileNotFoundError\n",
    "\n",
    "file = open(\"abc.txt\", \"r\")\n",
    "\n",
    "print(file.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "41fc8977",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'upper'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# AttributeError\u001b[39;00m\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m numbers = [\u001b[32m10\u001b[39m, \u001b[32m20\u001b[39m, \u001b[32m30\u001b[39m]\n\u001b[32m      4\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m numbers.upper()\n",
      "\u001b[31mAttributeError\u001b[39m: 'list' object has no attribute 'upper'"
     ]
    }
   ],
   "source": [
    "# AttributeError\n",
    "\n",
    "numbers = [10, 20, 30]\n",
    "\n",
    "numbers.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a400e82c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cannot divide by zero.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    num1 = int(input(\"Enter first number: \"))\n",
    "    num2 = int(input(\"Enter second number: \"))\n",
    "\n",
    "    print(\"Result:\", num1 / num2)\n",
    "\n",
    "except ZeroDivisionError:\n",
    "    print(\"Cannot divide by zero.\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Please enter valid numbers.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b31f03e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Python File Handling.\n"
     ]
    }
   ],
   "source": [
    "# Write and read a file\n",
    "\n",
    "file = open(\"sample.txt\", \"w\")\n",
    "\n",
    "file.write(\"Welcome to Python File Handling.\")\n",
    "\n",
    "file.close()\n",
    "\n",
    "file = open(\"sample.txt\", \"r\")\n",
    "\n",
    "data = file.read()\n",
    "\n",
    "print(data)\n",
    "\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "551ece44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Python File Handling.\n",
      "This is an additional line.\n"
     ]
    }
   ],
   "source": [
    "# Append data to a file\n",
    "\n",
    "file = open(\"sample.txt\", \"a\")\n",
    "\n",
    "file.write(\"\\nThis is an additional line.\")\n",
    "\n",
    "file.close()\n",
    "\n",
    "file = open(\"sample.txt\", \"r\")\n",
    "\n",
    "print(file.read())\n",
    "\n",
    "file.close()"
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