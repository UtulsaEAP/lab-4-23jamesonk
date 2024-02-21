"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Kai Jameson
Lab Time: Thursdays @ 2pm

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    binary_val = ''
    while user_num > 0:
        place = user_num % 2
        binary_val += str(place)
        user_num = user_num // 2
    print(binary_val)

if __name__ == "__main__":
    reverse_binary()