import sys

if len(sys.argv) == 1:
    print("none")
else:
    num_params = len(sys.argv) - 1
    print(f"parameters: {num_params}")
    parameters = sys.argv[1:]
    for word in parameters:
        print(f"{word}: {len(word)}")