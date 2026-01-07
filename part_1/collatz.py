import logging
logging.basicConfig(
    filename='logs/collatz_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)
# logging.disable(logging.CRITICAL) # Comment to toggle logging
# ----------------------------------------

def collatz(number):
    logging.debug('collatz() successfully called')
    if number % 2 == 0:
        print(f"{number // 2}", end=' | ')
        return number // 2
    else:
        print(f"{number * 3 + 1}", end=' | ')
        return number * 3 + 1
# ----------------------------------------

logging.debug('Start of program')

active = True
while active:
    try:
        num = int(input("Enter a number: "))
        while num > 1:
            num = collatz(num)
        active = False
    except ValueError:
        print("Please enter a number.")
        continue
logging.debug('Program end.')
