# Password Strength Checker in Python

A Python program which evaluates the strength of passwords based on their length, character variety, digit inclusion, and whether the password is commonly used.

This was my first independent project after taking COMPSCI 101 and is based off a tutorial from https://dev.to/immah/building-a-password-strength-checker-in-python-47om with added input ability and the ability to check multiple passwords at once.

---

## Features

- Checks password strength based on:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters

- Detects common passwords using a large dataset (100k most used passwords)

- Provides:
  - Strength rating (Weak, Okay, Good, Strong)
  - Numerical score
  - Suggestions for improvement

- Supports checking:
  - Single password input
  - Multiple passwords at once

---

## How It Works

The program assigns a score based on:

- Password length thresholds
- Variety of character types
- Penalty adjustment for low diversity
- Bonus deduction for missing character variety

It then categorizes the password into:

- Weak
- Okay
- Good
- Strong

---

## Files

- `PasswordStrengthChecker.py`: main program
- `100k-most-used-passwords-NCSC.txt`: dataset of common passwords

---




