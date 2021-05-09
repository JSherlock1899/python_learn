import os
import time


def marquee():
    content = "通通五十块通通五十块"

    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)

        content = content[1:] + content[0]

if __name__ == '__main__':
    marquee()
