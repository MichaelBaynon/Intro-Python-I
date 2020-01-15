# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard

x = int(input())

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(is_even(x))



# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

x = int(input())

def is_even(x):
    if x % 2 == 0:
        print('Even!')
    else:
        print('Odd!')

print(is_even(x))

