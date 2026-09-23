import sys

if len(sys.argv) == 1:
    print("none")
else:
    parameters = sys.argv[1:]
    print("parameters:", len(parameters))

    for param in parameters:
        print(f"{param}: {len(param)}")