import sys
import time

f = None
try:
    f = open("F:\\Github\\Python\\Practice\\Files\\data\\poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line),
        sys.stdout.flush()
        print("Press CTRL+C now")
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print("Couldn't find your poem")
except KeyboardInterrupt:
    print("You cancelled the reading from file")
finally:
    if f:
        f.close()
    print("[Cleaning up: Closed the file]")