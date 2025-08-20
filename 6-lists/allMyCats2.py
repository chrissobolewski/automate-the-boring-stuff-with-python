import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
cat_names = []
logging.debug('Cat names len(' + str(len(cat_names)) + ')')
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]  # List concatenation
print('The cat names are:')
for name in cat_names:
    print('  ' + name)