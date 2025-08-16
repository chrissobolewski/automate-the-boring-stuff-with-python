# example of how end= works in print
import random
for i in range(100):  # Perform 100 coin flips.
    if random.randint(0, 1) == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
print()  # Print one newline at the end.

# example of how sep= works in print
print('cats', 'dogs', 'mice', sep=', ')