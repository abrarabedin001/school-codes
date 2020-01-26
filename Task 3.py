# Python program to reverse a string using recursion

# Function to print reverse of the passed string
def reverse(string):
    if len(string) == 0:
        return

    temp = string[0]
    print(temp)
    reverse(string[1:])



# Driver program to test above function
string = "Geeks for Geeks"
reverse(string)

# A single line statement to reverse string in python
# string[::-1]

# This code is contributed by Bhavya Jain
