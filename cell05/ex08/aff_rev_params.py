import sys
if len(sys.argv) > 2 :
    para = sys.argv[1:]
    for i in reversed(para) :
        print(i)
else :
    print("none")