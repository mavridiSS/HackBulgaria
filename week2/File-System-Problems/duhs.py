import sys
import os


def main():
    f = os.popen('du -hs ' + sys.argv[1])
    size = f.read()
    print(sys.argv[1], size)

if __name__ == '__main__':
    main()
