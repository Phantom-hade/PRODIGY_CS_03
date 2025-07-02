"""
Title       : Password Complexity Checker
Author      : Larona B. Kwae
Date        : June 2025
PRODIGY_CS  : 03
Description : A python tool that checks the strength of a password. 
""" 
import re # Imports the 're' module to use regular expressions for pattern matching in the password


def check_password_strength(password):
    strength = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append(" Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append(" Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append(" Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append(" Include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Use at least one special character (e.g., !@#$).")

    # Evaluate strength
    if strength == 5:
        status = "Strong Password"
    elif 3 <= strength < 5:
        status = "Medium Password"
    else:
        status = " Weak Password"

    return status, feedback

# Main Program
print("\n Password Strength Checker")
password = input("Enter your password: ")

status, feedback = check_password_strength(password)

print(f"\nPassword Status: {status}")
if feedback:
    print("\nSuggestions:")
    for tip in feedback:
        print(tip)
