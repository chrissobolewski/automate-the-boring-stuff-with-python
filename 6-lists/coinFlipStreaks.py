import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    flips = []
    for flip in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row
    streak = 0
    for i in range(len(flips)):
        if i == 0 or flips[i] == flips[i - 1]:
            streak += 1
        else:
            streak = 1
        if streak == 6:
            number_of_streaks += 1
            break
print('Chance of streak: %s%%' % (number_of_streaks / 100))