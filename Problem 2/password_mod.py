"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Kai Jameson
Lab Time: Thursday @ 2pm
"""

def password_mod():
    word = input()
    password = ''
    for char in word:
        if char == 'i':
            password = password + "1"
        elif char == 'a':
            password = password + "@"
        elif char == 'm':
            password += "M"
        elif char == 'B':
            password += "8"
        elif char == 's':
            password += "$"
        else:
            password = password + char

    print(password + '!')


if __name__ == "__main__":
    password_mod()