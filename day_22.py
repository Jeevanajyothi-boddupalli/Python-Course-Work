{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3a533667",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "n8tF^bfL\n"
     ]
    }
   ],
   "source": [
    "#random password generator\n",
    "import random\n",
    "characters=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "characters+=\"abcdefghijklmnopqrstuvwxyz\"\n",
    "characters+=\"0123456789\"\n",
    "characters+=\"!@#$%^&*\"\n",
    "length=int(input())\n",
    "password=\"\"\n",
    "for i in range(length):\n",
    "    ch=random.choice(characters)\n",
    "    password+=ch\n",
    "print(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "367749ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "@5vT#bNY\n"
     ]
    }
   ],
   "source": [
    "#Strong password generator\n",
    "import random\n",
    "Uppercase=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "Lowercase=\"abcdefghijklmnopqrstuvwxyz\"\n",
    "Numbers=\"0123456789\"\n",
    "Special=\"!@#$%^&*\"\n",
    "length=int(input())\n",
    "password=[]\n",
    "if length<4:\n",
    "    print(\"Password length should be at least 4\")\n",
    "else:\n",
    "    password.append(random.choice(Uppercase))\n",
    "    password.append(random.choice(Lowercase))\n",
    "    password.append(random.choice(Numbers))\n",
    "    password.append(random.choice(Special))\n",
    "    for i in range(length-4):\n",
    "        password.append(random.choice(Uppercase+Lowercase+Numbers+Special))\n",
    "    random.shuffle(password)\n",
    "    print(\"\".join(password))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "61799be9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0:0:59\n",
      " Your 1 minute completed\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "from IPython.display import clear_output\n",
    "seconds=0\n",
    "minutes=0\n",
    "hours=0\n",
    "while True:\n",
    "    print(f\"{hours}:{minutes}:{seconds}\")\n",
    "    time.sleep(1)\n",
    "    seconds+=1\n",
    "    if seconds==60:\n",
    "        minutes+=1\n",
    "        seconds=0\n",
    "        if minutes==1:\n",
    "            print(f\" Your {minutes} minute completed\")\n",
    "            break\n",
    "            hours+=1\n",
    "            minutes=0\n",
    "    clear_output(wait=True)"
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