# Python program to print all
# prime number in an interval

start = 59999
end = 25259999
limit = 100

for val in range(start, end + 1):

    # If num is divisible by any number
    # between 2 and val, it is not prime
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            mod = 25259999 % val
            if mod <= limit:
                print (val)
