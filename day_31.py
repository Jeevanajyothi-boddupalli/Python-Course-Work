{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "41900cf8",
   "metadata": {},
   "source": [
    "# REGULAR EXPRESSIONS\n",
    "\n",
    "Regular Expressions, also called Regex, are patterns used to search,\n",
    "match, and manipulate text.\n",
    "\n",
    "Python provides the `re` module for working with regular expressions.\n",
    "\n",
    "## IMPORTANT FUNCTIONS\n",
    "\n",
    "### 1. re.match()\n",
    "Checks whether a pattern matches at the beginning of a string.\n",
    "\n",
    "### 2. re.search()\n",
    "Searches for a pattern anywhere in a string.\n",
    "\n",
    "### 3. re.findall()\n",
    "Returns all occurrences of a pattern as a list.\n",
    "\n",
    "### 4. re.finditer()\n",
    "Returns an iterator containing match objects for all occurrences.\n",
    "\n",
    "### 5. re.sub()\n",
    "Replaces the matched pattern with another string.\n",
    "\n",
    "### 6. re.split()\n",
    "Splits a string based on a specified pattern.\n",
    "\n",
    "## IMPORTANT REGEX PATTERNS\n",
    "\n",
    "### . \n",
    "Matches any character except a newline.\n",
    "\n",
    "### ^\n",
    "Matches the beginning of a string.\n",
    "\n",
    "### $\n",
    "Matches the end of a string.\n",
    "\n",
    "### *\n",
    "Matches zero or more occurrences.\n",
    "\n",
    "### +\n",
    "Matches one or more occurrences.\n",
    "\n",
    "### ?\n",
    "Matches zero or one occurrence.\n",
    "\n",
    "### \\d\n",
    "Matches a digit.\n",
    "\n",
    "### \\D\n",
    "Matches a non-digit character.\n",
    "\n",
    "### \\w\n",
    "Matches a word character.\n",
    "\n",
    "### \\W\n",
    "Matches a non-word character.\n",
    "\n",
    "### \\s\n",
    "Matches whitespace.\n",
    "\n",
    "### \\S\n",
    "Matches non-whitespace characters.\n",
    "\n",
    "### [abc]\n",
    "Matches any one character from a, b, or c.\n",
    "\n",
    "### [0-9]\n",
    "Matches any digit from 0 to 9.\n",
    "\n",
    "### [a-z]\n",
    "Matches lowercase letters from a to z.\n",
    "\n",
    "### [A-Z]\n",
    "Matches uppercase letters from A to Z."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa9631ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pattern matched\n"
     ]
    }
   ],
   "source": [
    "# re.match()\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"Python is easy to learn\"\n",
    "\n",
    "result = re.match(\"Python\", text)\n",
    "\n",
    "if result:\n",
    "    print(\"Pattern matched\")\n",
    "else:\n",
    "    print(\"Pattern not matched\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9faa09ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pattern found\n"
     ]
    }
   ],
   "source": [
    "# re.search()\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"I am learning Python\"\n",
    "\n",
    "result = re.search(\"Python\", text)\n",
    "\n",
    "if result:\n",
    "    print(\"Pattern found\")\n",
    "else:\n",
    "    print(\"Pattern not found\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9d957dfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python', 'Python']\n"
     ]
    }
   ],
   "source": [
    "# re.findall()\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"Python is easy and Python is powerful\"\n",
    "\n",
    "result = re.findall(\"Python\", text)\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8b676c54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Match: Python\n",
      "Position: 0\n",
      "Match: Python\n",
      "Position: 19\n"
     ]
    }
   ],
   "source": [
    "# re.finditer()\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"Python is easy and Python is powerful\"\n",
    "\n",
    "result = re.finditer(\"Python\", text)\n",
    "\n",
    "for match in result:\n",
    "    print(\"Match:\", match.group())\n",
    "    print(\"Position:\", match.start())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3f44f95b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I like Python\n"
     ]
    }
   ],
   "source": [
    "# re.sub()\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"I like Java\"\n",
    "\n",
    "result = re.sub(\"Java\", \"Python\", text)\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "093bb6db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python', 'Java', 'C++']\n"
     ]
    }
   ],
   "source": [
    "# re.split()\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"Python,Java,C++\"\n",
    "\n",
    "result = re.split(\",\", text)\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fd13d67e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']\n"
     ]
    }
   ],
   "source": [
    "# \\d - digits\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"My phone number is 9876543210\"\n",
    "\n",
    "result = re.findall(r\"\\d\", text)\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "477ac99d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python', '123', 'Programming']\n"
     ]
    }
   ],
   "source": [
    "# \\w - word characters\n",
    "\n",
    "import re\n",
    "\n",
    "text = \"Python 123 Programming\"\n",
    "\n",
    "result = re.findall(r\"\\w+\", text)\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f748eb10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valid phone number\n"
     ]
    }
   ],
   "source": [
    "# Phone number validation\n",
    "\n",
    "import re\n",
    "\n",
    "phone = \"9876543210\"\n",
    "\n",
    "pattern = r\"^[0-9]{10}$\"\n",
    "\n",
    "if re.match(pattern, phone):\n",
    "    print(\"Valid phone number\")\n",
    "else:\n",
    "    print(\"Invalid phone number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fb259aaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valid email\n"
     ]
    }
   ],
   "source": [
    "# Email validation\n",
    "\n",
    "import re\n",
    "\n",
    "email = \"bhavana@gmail.com\"\n",
    "\n",
    "pattern = r\"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$\"\n",
    "\n",
    "if re.match(pattern, email):\n",
    "    print(\"Valid email\")\n",
    "else:\n",
    "    print(\"Invalid email\")"
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