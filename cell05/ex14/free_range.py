import sys

if len(sys.argv) == 3 :
    f_num = int(sys.argv[1])
    s_num = int(sys.argv[2])
    num_arr = list(range(f_num, s_num + 1))
    print(num_arr)
else :
    print("none")