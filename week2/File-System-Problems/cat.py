import sys


def main():
    for arg in sys.argv[1:]:
        with open(arg) as f:
            data = f.read()
            print(data)

if __name__ == '__main__':
    main()
