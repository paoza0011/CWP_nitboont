import sys

if len(sys.argv) != 3:
    print("none")
else:
    first = int(sys.argv[1])
    second = int(sys.argv[2])

    numbers = list(range(first, second + 1))
    print(numbers)