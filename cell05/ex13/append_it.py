import sys

if len(sys.argv) == 1 :
    print("none")
else :
    para = sys.argv[1:]
    for word in para :
        if not word.endswith("ism") :
            print(f"{word}ism")