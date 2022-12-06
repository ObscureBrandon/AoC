import re
from collections import deque

with open("input.txt") as f:
    crates, instructions = f.read().split("\n\n")

def part_1():
    stacks: list[deque] = []
    for line in crates.splitlines():
        for i, idx in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())

            if line[idx] != " ":
                stacks[i].append(line[idx])
    print(stacks)
    for instruction in instructions.splitlines():
        a, b, c = map(int, re.findall(r"\d+", instruction))
        for _ in range(a):
            print(f"Moving {a} from {b} to {c}")
            stacks[c - 1].appendleft(stacks[b - 1].popleft())
            print(stacks)

    return "".join(stack.popleft() for stack in stacks)

def part_2():
    stacks: list[deque] = []
    for line in crates.splitlines():
        for i, idx in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            
            if line[idx] != " ":
                stacks[i].append(line[idx])

    print(stacks)
    for instruction in instructions.splitlines():
        a, b, c = map(int, re.findall(r"\d+", instruction))
        temp = deque()
        for _ in range(a):
            temp.appendleft(stacks[b - 1].popleft())

        stacks[c - 1].extendleft(temp)

    return "".join(stack.popleft() for stack in stacks)
