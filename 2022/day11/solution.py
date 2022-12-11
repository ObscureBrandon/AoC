from io import TextIOWrapper
from math import prod
from typing import Callable, TypedDict


class Monkey(TypedDict):
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], bool]
    testnum: int
    inspections: int
    throw: dict[bool, int]


def parse_monkey(lines) -> Monkey:
    print(lines)
    return {
        "items": [int(x) for x in lines[1][18:].split(",")],
        "operation": lambda old: eval(lines[2][19:]),
        "test": lambda x: x % int(lines[3][21:]) == 0,
        "testnum": int(lines[3][21:]),
        "inspections": 0,
        "throw": {
            True: int(lines[4][29:]),
            False: int(lines[5][30:]),
        },
    }


def part_1(f: TextIOWrapper) -> int:
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().strip().split("\n\n")]

    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                monkeys[i]["inspections"] += 1
                worry = monkey["operation"](item) // 3
                test = monkey["test"](worry)
                throw_to = monkey["throw"][test]
                monkeys[throw_to]["items"].append(worry)

            monkey["items"] = []

    desc = sorted([x["inspections"] for x in monkeys], reverse=True)
    return desc[0] * desc[1]


def part_2(f: TextIOWrapper) -> int:
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().strip().split("\n\n")]
    mod = prod(m["testnum"] for m in monkeys)

    for _ in range(10_000):
        for _, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                monkey["inspections"] += 1
                new = monkey["operation"](item) % mod
                test = monkey["test"](new)
                throw = monkey["throw"][test]
                monkeys[throw]["items"].append(new)

            monkey["items"] = []

    desc = sorted([x["inspections"] for x in monkeys], reverse=True)
    return desc[0] * desc[1]
