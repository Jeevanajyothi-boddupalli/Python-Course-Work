import re
s = input()
prices = re.findall(r"\$\d+\.\d{2}",s)
print(prices)
