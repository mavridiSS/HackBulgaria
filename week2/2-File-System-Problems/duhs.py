import sys
import os


def bytes_to_gb(b):
    return b * (10 ** -9)


def main():
    if len(sys.argv[1:]) >= 1:
        path = sys.argv[1]
        total_size = 0

        for root, subsirs, files in os.walk(path):
            for data in files:
                try:
                    total_size += os.path.getsize(os.path.join(root, data))
                except IOError as error:
                    print(error)

        print(bytes_to_gb(total_size), "GB")
    else:
        raise AttributeError("No arguments were given.")


if __name__ == "__main__":
    main()
