import sys


def main():
    with open(sys.argv[1]) as f:
        data = f.read()
        print(sum([int(ch) for ch in data.split(" ")]))

if __name__ == '__main__':
    main()
