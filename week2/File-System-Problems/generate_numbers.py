import sys
from random import randint


def main():
        with open(sys.argv[1], 'w') as f:
            f.write(" ".join([str(randint(1, 100))
                    for i in range(int(sys.argv[2]))]))

if __name__ == '__main__':
    main()
