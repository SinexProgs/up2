import ast


def find_sum_combos(candidates, target):
    candidates.sort()

    def rec(pool, target):
        if target == 0:
            return [[]]
        if target < 0:
            return []

        i = 0
        result = []
        while i < len(pool):
            cur_num = pool[i]
            for combo in rec(pool[i + 1:], target - cur_num):
                result.append([cur_num] + combo)
            while i < len(pool) and pool[i] == cur_num:
                i += 1
        return result

    return rec(candidates, target)


candidates = ast.literal_eval(input("Enter candicates (in square brackets): "))
target = int(input("Enter target: "))

print(find_sum_combos(candidates, target))