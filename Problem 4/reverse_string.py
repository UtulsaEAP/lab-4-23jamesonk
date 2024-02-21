"""
Complete the following python code to reverse the string entered by the user.

Name: Kai Jameson
Lab Time: Thursday @ 2pm
"""

def reverse_string():
    # YOUR CODE HERE
    userWord = input()
    while userWord != "done" and userWord != "Done" and userWord !="d":
        revString = ""
        for char in userWord:
            revString = char + revString
        print(revString)
        userWord = str(input())
        

    
if __name__ == "__main__":
    reverse_string()