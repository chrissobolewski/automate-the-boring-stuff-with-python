# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
# Then, write a program that lets the user enter an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer; sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value. To make the output more compact, the print() calls that print the numbers should have a sep=' ' named parameter to print all values on one line.

print('Input number to test: ')
while True:
    try:
        number = int(input('> '))
        if number <= 0:
            print('Please enter a positive integer.')
            continue
        break
    except ValueError:
        print('Please enter a valid integer.')

def collatz(n):
    # Returns the next number in the Collatz sequence
    if n % 2 == 0:
        print (n // 2, end =' ')
        return n // 2
    else:
        print (3 * n + 1, end =' ')
        return 3 * n + 1
    
while number != 1:
    number = collatz(number)
print()
print('Reached 1!')  # Print when the sequence ends
