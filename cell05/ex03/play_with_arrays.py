original = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for num in original:
    if num > 5 :
        new_arr.append(num + 2)
print(original)
print(set(new_arr))