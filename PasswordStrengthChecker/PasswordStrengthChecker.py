import string

def checkCommonPassword(password):
    '''
    uses a large file to check if the password is considered a common password
    '''
    with open("100k-most-used-passwords-NCSC.txt", "r", encoding="utf-8") as file:
        words = [word.strip() for word in file.readlines()]

    if password in words:
        return True
    else:
        return False

def passwordStrength(password):
    '''
    determines the strength of a password by its length, uppercase letters, lowercase letters,
    digits, and special characters. determines a score based off of these factors.
    '''

    score = 0
    lengthPassword = len(password)

    upperCase = any(c.isupper() for c in password)
    lowerCase = any(c.islower() for c in password)
    digits = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    characters = [upperCase, lowerCase, digits, special]

    if lengthPassword > 8:
        score += 1
    if lengthPassword > 12:
        score += 1
    if lengthPassword > 17:
        score += 1
    if lengthPassword > 20:
        score += 1

    score += max(sum(characters) - 1, 0)

    if score < 4:
        return "Weak", score
    if score == 4:
        return "Okay", score
    if 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score

def feedback(password):
    '''
    returns the appropriate feedback based on if the password is common or based off of the
    score of the password
    '''

    isCommon = checkCommonPassword(password)
    if isCommon:
        return "Password is common, score is 0"

    strength, score = passwordStrength(password)

    response = "Password strength is " + strength + ", score is " + str(score)

    if score < 4:

        response += "\nSuggestions to improve your password:\n"

        if len(password) < 8:
            response += "Your password is too short, it must contain at least 8 characters. "
        if not any(c.isupper() for c in password):
            response += "You must have at least one uppercase letter. "
        if not any(c.islower() for c in password):
            response += "You must have at least one lowercase letter. "
        if not any(c.isdigit() for c in password):
            response += "You must have at least one digit. "
        if not any(c in string.punctuation for c in password):
            response += "You must have at least one special character. "

    return response

def isMultiple():
    '''
    determines if the user is going to be inputing one password or multiple passwords
    '''

    while True:

        print("Input Y if you are checking multiple passwords or N if you are only checking one password.")
        answer = input()

        if answer == "Y" or answer == "y":
            return True
        elif answer == "N" or answer == "n":
            return False
        else:
            print("Please enter Y or N.")

def multiplePasswords(passwordList):
    '''
    in the case of multiple passwords, returns the feedback of all of the inputed passwords
    '''

    response = ""

    for password in passwordList:
        r = feedback(password)
        if password == passwordList[0]:
            response += password + ": " + r
        else:
            response += "\n\n" + password + ": " + r

    return response

def fullPasswordStrengthChecker():
    '''
    asks the user for a password or passwords and prints the appropriate feedback
    '''

    multiple = isMultiple()

    if multiple:
        print("Enter your passwords seperated by a single space. For example: 'Password1 Password2 Password3'.")
        passwordList = input().split()
        response = multiplePasswords(passwordList)
        print(response)

    if not multiple:
        print("Enter your password.")
        password = input()
        response = feedback(password)
        print(response)



if __name__ == "__main__":
    fullPasswordStrengthChecker()

