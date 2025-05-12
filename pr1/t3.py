import ast


def has_repeating_numbers(arr):
    for num_i in range(len(arr)):
        for inner_num_i in range(num_i + 1, len(arr)):
            if arr[num_i] == arr[inner_num_i]:
                return True
    return False


nums = ast.literal_eval(input("Enter numbers (in square brackets): "))
print(has_repeating_numbers(nums))