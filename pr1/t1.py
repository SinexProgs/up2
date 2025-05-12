str_j = input("Enter J: ")
str_s = input("Enter S: ")

j_in_s_count = 0
for cur_char in str_s:
    if cur_char in str_j:
        j_in_s_count += 1

print(j_in_s_count)