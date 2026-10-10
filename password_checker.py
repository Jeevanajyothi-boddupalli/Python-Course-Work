def check_password(password):
    if len(password) < 8:
        return "Weak"
    has_digit = False
    has_upper = False
    
    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
            
    if has_digit and has_upper:
        return "Strong"
    else:
        return "Weak"

s = input().strip()
if ":" in s:
    s = s.split(":")[-1].strip()

if " " in s and len(s.split()) > 1:
    s = s.split()[-1]

result = check_password(s)
print(f"Password is {result}")