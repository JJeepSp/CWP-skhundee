import sys

def cut(text) :
    print(text[:8])

def enlarge(text) :
    missing = 8 - len(text)
    print(text + ("Z" * missing))

parameters = sys.argv[1:]
for word in parameters :
    if len(word) > 8 :
        cut(word)
    elif len(word) < 8 :
        enlarge(word)
    else :
        print(word)