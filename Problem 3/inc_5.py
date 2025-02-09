"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Kai Jameson
Lab Time: Thursday @ 2pm
"""

def inc_5():
    # Write your code here
    first = int(input())
    last = int(input())
    if first > last:
        print('Second integer can\'t be less than the first.')
    else:
        while first <= last:
            print(first, end=" ")
            first += 5

if __name__ == '__main__':
    inc_5()