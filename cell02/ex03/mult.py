f_num = int(input("Enter the first number:\n"))
S_num = int(input("Enter the second number:\n"))
mul = f_num * S_num
print(f_num, "x", S_num, "=", mul)
if mul > 0 :
    print("The result is positive.")
elif mul < 0 :
    print("The result is negative.")
else :
    print("The result is positive and negative.")