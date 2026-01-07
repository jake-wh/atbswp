import time, sys

indent = 0

indent_increasing = True

try:
    while True:
        if indent_increasing:
            print(' ' * indent, end='')
            print('**********')
            time.sleep(0.1)
            indent += 1
            if indent == 10:
                indent_increasing = False
        else:
            print(' ' * indent, end='')
            print('**********')
            time.sleep(0.1)
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
