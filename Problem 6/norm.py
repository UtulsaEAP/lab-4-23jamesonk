"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Kai Jameson
Lab Time: Thursday @ 2pm
"""

def norm():
    # Write your code here
    numAmount = int(input())
    numArr = {}
    highNum = float(0)
    for x in range(0,numAmount):
        numArr[x] = float(input())
    
    highNum = numArr[0]
    for x in range(1,numAmount):
        if highNum < numArr[x]:
            highNum = numArr[x]
    for x in range(0,numAmount):
        numArr[x] /= highNum
        print(f'{numArr[x]:.2f}')

if __name__ == "__main__":
    norm()