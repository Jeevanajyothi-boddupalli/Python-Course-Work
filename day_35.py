{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d5f2a171",
   "metadata": {},
   "source": [
    "# WEB SCRAPING IN PYTHON\n",
    "\n",
    "## ABOUT WEB SCRAPING\n",
    "- Web scraping is the process of extracting data from websites automatically.\n",
    "- Python provides libraries such as Requests and BeautifulSoup for web scraping.\n",
    "- Requests is used to send HTTP requests and retrieve webpage content.\n",
    "- BeautifulSoup is used to parse HTML and extract required information.\n",
    "- Web scraping can be used to collect product details, headlines, links, and other publicly available information.\n",
    "\n",
    "## LIBRARIES USED\n",
    "- Requests: Fetches webpage content.\n",
    "- BeautifulSoup: Parses HTML and extracts data.\n",
    "- CSV: Stores extracted data in a CSV file.\n",
    "\n",
    "## BASIC STEPS\n",
    "1. Import the required libraries.\n",
    "2. Send a request to the website.\n",
    "3. Check the response status.\n",
    "4. Parse the HTML content using BeautifulSoup.\n",
    "5. Extract the required elements.\n",
    "6. Display or save the extracted data.\n",
    "\n",
    "## IMPORTANT FUNCTIONS\n",
    "- `requests.get()`: Sends a GET request.\n",
    "- `BeautifulSoup()`: Parses HTML content.\n",
    "- `find()`: Finds the first matching element.\n",
    "- `find_all()`: Finds all matching elements.\n",
    "- `get_text()`: Extracts text from an HTML element.\n",
    "- `get()`: Retrieves an HTML attribute, such as a link.\n",
    "- `select()`: Finds elements using CSS selectors.\n",
    "\n",
    "## IMPORTANT POINTS\n",
    "- Install the libraries using `pip install requests beautifulsoup4`.\n",
    "- Check website terms and scraping permissions before collecting data.\n",
    "- Respect robots.txt, rate limits, and privacy restrictions.\n",
    "- Some websites load content using JavaScript and may require other tools."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acccfd41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!doctype html><html lang=en><head><meta charset=utf-8><link rel=icon href=data:,><meta name=viewport content=\"width=device-width,initial-scale=1\"><title>Example Domain</title><style>html{color-scheme:light dark;background:light-dark(#eee,#222)}body{font:16px/1.6 system-ui,sans-serif;max-width:26em;margin:auto;padding:25vh 2em 2em;text-align:center}</style></head><body><p>This domain is for use in documentation examples without needing permission. This is not a service; avoid relying on it for testing and monitoring purposes.</p><script src=/s.js></script></body></html>\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"https://example.com\"\n",
    "\n",
    "response = requests.get(url, timeout=10)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    print(response.text)\n",
    "else:\n",
    "    print(\"Failed to fetch webpage\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e41ab604",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Example Domain\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "url = \"https://example.com\"\n",
    "response = requests.get(url, timeout=10)\n",
    "\n",
    "soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "title = soup.find(\"title\")\n",
    "print(title.get_text(strip=True) if title else \"Title not found\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "82f76a04",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "from urllib.parse import urljoin\n",
    "\n",
    "url = \"https://example.com\"\n",
    "response = requests.get(url, timeout=10)\n",
    "\n",
    "soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "for link in soup.find_all(\"a\", href=True):\n",
    "    text = link.get_text(strip=True)\n",
    "    href = urljoin(url, link[\"href\"])\n",
    "    print(text, href)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fe6b2d1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data saved to headings.csv\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import csv\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "url = \"https://example.com\"\n",
    "response = requests.get(url, timeout=10)\n",
    "\n",
    "soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "headings = soup.find_all([\"h1\", \"h2\", \"h3\"])\n",
    "\n",
    "with open(\"headings.csv\", \"w\", newline=\"\", encoding=\"utf-8\") as file:\n",
    "    writer = csv.writer(file)\n",
    "    writer.writerow([\"Heading\"])\n",
    "\n",
    "    for heading in headings:\n",
    "        writer.writerow([heading.get_text(strip=True)])\n",
    "\n",
    "print(\"Data saved to headings.csv\")"
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