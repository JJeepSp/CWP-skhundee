import sys

if len(sys.argv) == 2 :
    original = sys.argv[1]
    user = input("What was the parameter? ")
    if user == original:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")