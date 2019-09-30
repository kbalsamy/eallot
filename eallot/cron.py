import time


with open('text.txt', 'w+') as f:

    f.write(f'started {time.strftime("%H:%M:%S", time.localtime())}')
