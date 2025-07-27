import re

def check_password_strength(password):
    length = len(password)
    strength = 0
    remarks = []

    if length >= 8:
        strength += 1
    else:
        remarks.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Include numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Include special characters")

    return strength, remarks
