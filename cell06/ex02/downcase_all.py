import sys

def downcase_it(text) :
    return text.lower()

if len(sys.argv) == 1 :
    print("none")
else :
    parameters = sys.argv[1:]
    for para in parameters:
        print(downcase_it(para))