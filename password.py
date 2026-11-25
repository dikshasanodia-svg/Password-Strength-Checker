
# Password Strength Checker
# Project No. 12

import re

print("=" * 45)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 45)

# Function to check password strength
def check_password(password):

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    # Check special characters
    if re.search(r"[@#$!%&*?]", password):
        score += 1
    else:
        suggestions.append("Add a special character (@, #, $, !, etc.).")

    # Decide password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, suggestions


# Main program
while True:

    password = input("\nEnter your password: ")

    strength, score, suggestions = check_password(password)

    print("\n" + "-" * 45)
    print("           PASSWORD REPORT")
    print("-" * 45)

    print("Password Strength :", strength)
    print("Security Score    :", str(score) + "/5")

    # Display suggestions if needed
    if suggestions:
        print("\nSuggestions to improve your password:")

        for suggestion in suggestions:
            print("-", suggestion)

    else:
        print("\nExcellent! Your password meets all the checks.")

    print("-" * 45)

    # Ask whether the user wants to check another password
    choice = input("\nDo you want to check another password? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using Password Strength Checker!")
        break
