with open("input.txt") as f:
    stream = f.read().strip()

def part_1() -> int:
    for i in range(len(stream)):
        repeated = False
        for char in stream[i:i + 4]:
            if stream[i:i + 4].count(char) > 1:
                repeated = True
                continue

        if not repeated:
            return i + 4

    return 0

def part_2() -> int:
    for i in range(len(stream)):
        repeated = False
        for char in stream[i:i+14]:
            if stream[i:i+14].count(char) > 1:
                repeated = True
                continue

        if not repeated:
            return i + 14

    return 0
