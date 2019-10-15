import sys


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


def main():
    try:
        print(first(["1st", "2nd", "3rd"]))
        print(first({"1st", "2nd", "3rd"}))
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Program execution continues normally here.")


if __name__ == '__main__':
    main()