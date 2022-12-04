with open("input.txt") as f:
    pairs = [line.split(",") for line in f.read().splitlines()]

def p1():
    ans = 0
    for pair in pairs:
        pair_1, pair_2 = pair[0].split("-"), pair[1].split("-")
        if (int(pair_1[0]) <= int(pair_2[0])) and (int(pair_2[1]) <= int(pair_1[1])) \
            or (int(pair_2[0]) <= int(pair_1[0]) and (int(pair_1[1]) <= int(pair_2[1]))):
            ans += 1

    return ans

def p2(): 
    ans = 0
    for pair in pairs:
        pair_1, pair_2 = pair[0].split("-"), pair[1].split("-")

        pair_1, pair_2 = range(int(pair_1[0]), int(pair_1[1]) + 1), range(int(pair_2[0]), int(pair_2[1]) + 1)
        ans += bool(set(pair_1).intersection(pair_2))

    return ans
