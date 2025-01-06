# password strength checker 
# check if a password is "weak", "Medium", or "strong".
# criteria <6 character (weak), 6-10 chars (medium),>10 chars(strong)

password = "Secure3P@ss"

if len(password) < 6:
    strength ="Weak"
elif len(password) <= 10:
    strength= "Medium"
else:
    strength = "Strong"

print("Password strength is :", strength)