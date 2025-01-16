import re

def check_password_strength(password):
    """Assess the strength of a given password based on various criteria."""
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Evaluate password strength
    strength = sum([
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    # Feedback based on strength
    if strength == 5:
        return "Strong", "Your password meets all the criteria!"
    elif strength >= 3:
        return "Moderate", "Your password is decent but can be improved."
    else:
        return "Weak", "Your password is too weak. Consider adding more complexity."

print("*** PASSWORD COMPLEXITY CHECKER ***")
print()

print("Enter your password to check its strength:")
password = input("Password: ")

strength, feedback = check_password_strength(password)
print()
print(f"PASSWORD STRENGTH: {strength.upper()}")
print(f"FEEDBACK: {feedback}")
