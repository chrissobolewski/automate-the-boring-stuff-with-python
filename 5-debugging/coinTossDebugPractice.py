import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().strip().lower()
toss = random.randint(0, 1) 
logging.debug('Toss value(' + str(toss) + ')')
logging.debug('Guess value(' + str(guess) + ')')

if toss == 0:
    coin = 'tails'
elif toss == 1:
    coin = 'heads' # 0 is tails, 1 is heads

logging.debug('Coin value(' + str(coin) + ')')

if coin == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input().strip().lower()
    if coin == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')