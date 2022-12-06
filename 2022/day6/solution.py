with open("input.txt") as f:
    stream = f.read().strip()

def part_1() -> int:
    for i in range(len(stream)):
        if len(set(stream[i:i + 4])) == 4:
            return i + 4

    return 0

def part_2() -> int:
    for i in range(len(stream)):
        if len(set(stream[i:i+14])) == 14:
            return i + 14

    return 0

print(part_1())
print(part_2())