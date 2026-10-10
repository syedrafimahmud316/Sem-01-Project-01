'''
Write a program that reads a password, its confirmation, an age, and a parental consent answer (yes/no).
Check if the password and confirmation match.
If they don't match → print "Password not accepted" and stop.
If they match → print "Password accepted".
Check password strength: if the password contains any of !, @, or #, print "Strong password", otherwise "Weak password".
Determine access based on the rules:
age ≥ 18 → "Access granted"
age ≥ 14 and parental consent is "yes" → "Access granted"
otherwise → "Access denied"
Finally, print a greeting in the format: "Welcome, user with a N-character password!" where N is the password length (use len() and string concatenation).
'''


import math


password = input("Enter your password: ")
confirmation = input("Re-enter your password: ")

age = abs(int(input("Enter your age (0 - 120): ")))

if password != confirmation:
    print("Password not accepted.")
else: 
    print("Password accepted.")
    if ("!" in password) or ("@" in password) or ("#" in password):
        print("Strong password.")
    else:
        print("Weak password.")
    if age >= 18:
        print("Access granted.")
        print("Welcome, user with a " + str(len(password)) + "-character password!")
    elif age >= 14:
        consent = input("Do you have parential consent (yes/no): ")
        if (consent == "yes"):
            print("Access granted.")
            print("Welcome, user with a " + str(len(password)) + "-character password!")
        else:
            print("Access denied.")
    else:
        print("Access denied.")