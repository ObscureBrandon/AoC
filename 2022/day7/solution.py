from collections import defaultdict
from pathlib import Path

with open("input.txt") as f:
    lines = f.read().splitlines()

def resolve_file_system():
    cwd = Path("/")
    file_system = defaultdict(int)

    for line in lines:
        match line.split():
            case ["$", "cd", newdir]:
                cwd = cwd / newdir
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                size = int(size)
                for path in [cwd, *cwd.parents]:
                    file_system[path] += size

    return file_system

def part_1():
    return sum(x for x in resolve_file_system().values() if x <= 100_000)

def part_2():
    taken = resolve_file_system()[Path("/").resolve()]
    unused = 70_000_000 - taken
    to_free = 30_000_000 - unused
    return min(x for x in resolve_file_system().values() if x >= to_free)

