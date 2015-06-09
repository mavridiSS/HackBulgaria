import sys


def file_data(filename):
    with open(filename) as f:
        data = f.read()
    return data


def main():
    if len(sys.argv[1:]) >= 1:
        result = [file_data(filename) for filename in sys.argv[1:]]
        print("\n".join(result))
    else:
        raise AttributeError("There are no arguments")

if __name__ == "__main__":
    main()
