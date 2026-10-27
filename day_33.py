{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f30a72bd",
   "metadata": {},
   "source": [
    "# PANDAS IN PYTHON\n",
    "\n",
    "## ABOUT PANDAS\n",
    "- Pandas is a Python library used for data manipulation and analysis.\n",
    "- It helps us work with structured data such as tables, CSV files, and Excel files.\n",
    "- It is built on top of NumPy.\n",
    "- Pandas provides two main data structures:\n",
    "  - Series: A one-dimensional labeled array.\n",
    "  - DataFrame: A two-dimensional table with rows and columns.\n",
    "- It is commonly used for data cleaning, data analysis, filtering, sorting, and handling missing values.\n",
    "\n",
    "## INSTALLING AND IMPORTING PANDAS\n",
    "- Install Pandas using `pip install pandas`.\n",
    "- Import Pandas using `import pandas as pd`.\n",
    "\n",
    "## CREATING DATA\n",
    "- Create a Series using `pd.Series()`.\n",
    "- Create a DataFrame using `pd.DataFrame()`.\n",
    "\n",
    "## ACCESSING DATA\n",
    "- Use column names to access columns.\n",
    "- Use `loc[]` to access data using labels.\n",
    "- Use `iloc[]` to access data using integer positions.\n",
    "\n",
    "## DATA ANALYSIS FUNCTIONS\n",
    "- `head()` displays the first five rows by default.\n",
    "- `tail()` displays the last five rows by default.\n",
    "- `info()` provides information about the DataFrame.\n",
    "- `describe()` displays statistical summaries.\n",
    "- `shape` returns the number of rows and columns.\n",
    "- `columns` returns the column names.\n",
    "\n",
    "## DATA CLEANING\n",
    "- `isnull()` identifies missing values.\n",
    "- `dropna()` removes rows containing missing values.\n",
    "- `fillna()` replaces missing values.\n",
    "- `drop_duplicates()` removes duplicate rows.\n",
    "\n",
    "## DATA MANIPULATION\n",
    "- `sort_values()` sorts data.\n",
    "- `groupby()` groups data based on a column.\n",
    "- `filtering` selects rows based on conditions.\n",
    "- `rename()` changes column names.\n",
    "- `drop()` removes rows or columns.\n",
    "\n",
    "## FILE HANDLING\n",
    "- `read_csv()` reads data from a CSV file.\n",
    "- `to_csv()` saves data to a CSV file.\n",
    "- `read_excel()` reads data from an Excel file.\n",
    "- `to_excel()` saves data to an Excel file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c1ea65f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    10\n",
      "1    20\n",
      "2    30\n",
      "3    40\n",
      "4    50\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "s = pd.Series([10, 20, 30, 40, 50])\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c2796e2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name  Age       City\n",
      "0  Bhavana   22  Hyderabad\n",
      "1    Priya   21    Chennai\n",
      "2     Ravi   23  Bangalore\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Jeevana\", \"Priya\", \"Ravi\"],\n",
    "    \"Age\": [23, 21, 23],\n",
    "    \"City\": [\"Hyderabad\", \"Chennai\", \"Bangalore\"]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "763ae9ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     Asha\n",
      "1     Ravi\n",
      "2    Priya\n",
      "Name: Name, dtype: str\n",
      "0    85\n",
      "1    90\n",
      "2    78\n",
      "Name: Marks, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\", \"Priya\"],\n",
    "    \"Marks\": [85, 90, 78]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df[\"Name\"])\n",
    "print(df[\"Marks\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5ec39fd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Marks\n",
      "0   Asha     85\n",
      "1   Ravi     90\n",
      "2  Priya     78\n",
      "3   John     88\n",
      "4   Neha     92\n",
      "    Name  Marks\n",
      "1   Ravi     90\n",
      "2  Priya     78\n",
      "3   John     88\n",
      "4   Neha     92\n",
      "5  Kiran     80\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\", \"Priya\", \"John\", \"Neha\", \"Kiran\"],\n",
    "    \"Marks\": [85, 90, 78, 88, 92, 80]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df.head())\n",
    "print(df.tail())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3a6e84ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 2)\n",
      "Index(['Name', 'Marks'], dtype='str')\n",
      "<class 'pandas.DataFrame'>\n",
      "RangeIndex: 3 entries, 0 to 2\n",
      "Data columns (total 2 columns):\n",
      " #   Column  Non-Null Count  Dtype\n",
      "---  ------  --------------  -----\n",
      " 0   Name    3 non-null      str  \n",
      " 1   Marks   3 non-null      int64\n",
      "dtypes: int64(1), str(1)\n",
      "memory usage: 180.0 bytes\n",
      "None\n",
      "           Marks\n",
      "count   3.000000\n",
      "mean   84.333333\n",
      "std     6.027714\n",
      "min    78.000000\n",
      "25%    81.500000\n",
      "50%    85.000000\n",
      "75%    87.500000\n",
      "max    90.000000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\", \"Priya\"],\n",
    "    \"Marks\": [85, 90, 78]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df.shape)\n",
    "print(df.columns)\n",
    "print(df.info())\n",
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "17be6381",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Name  Marks\n",
      "0  Asha     85\n",
      "3  John     92\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\", \"Priya\", \"John\"],\n",
    "    \"Marks\": [85, 45, 78, 92]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df[df[\"Marks\"] > 80])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "570df5e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Marks\n",
      "2  Priya     78\n",
      "0   Asha     85\n",
      "1   Ravi     90\n",
      "    Name  Marks\n",
      "1   Ravi     90\n",
      "0   Asha     85\n",
      "2  Priya     78\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\", \"Priya\"],\n",
    "    \"Marks\": [85, 90, 78]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df.sort_values(by=\"Marks\"))\n",
    "print(df.sort_values(by=\"Marks\", ascending=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aacc710e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Marks\n",
      "0  False  False\n",
      "1  False   True\n",
      "2  False  False\n",
      "    Name  Marks\n",
      "0   Asha   85.0\n",
      "1   Ravi    0.0\n",
      "2  Priya   78.0\n",
      "    Name  Marks\n",
      "0   Asha   85.0\n",
      "2  Priya   78.0\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\", \"Asha\"],\n",
    "    \"Marks\": [85, 90, 85]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df.drop_duplicates())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "266bd164",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Marks Result\n",
      "0   Asha     85   Pass\n",
      "1   Ravi     90   Pass\n",
      "2  Priya     78   Pass\n",
      "    Name  Marks\n",
      "0   Asha     85\n",
      "1   Ravi     90\n",
      "2  Priya     78\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\", \"Priya\"],\n",
    "    \"Marks\": [85, 90, 78]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "df[\"Result\"] = [\"Pass\", \"Pass\", \"Pass\"]\n",
    "print(df)\n",
    "\n",
    "df = df.drop(columns=[\"Result\"])\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3b23e654",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Name  Score\n",
      "0  Asha     85\n",
      "1  Ravi     90\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Asha\", \"Ravi\"],\n",
    "    \"Marks\": [85, 90]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "df = df.rename(columns={\"Marks\": \"Score\"})\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e7f33a8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Department\n",
      "HR    30000.0\n",
      "IT    35000.0\n",
      "Name: Salary, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Department\": [\"IT\", \"HR\", \"IT\", \"HR\"],\n",
    "    \"Salary\": [30000, 25000, 40000, 35000]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df.groupby(\"Department\")[\"Salary\"].mean())"
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