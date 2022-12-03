from string import ascii_letters

with open("input.txt") as f:
    baggages = f.read().splitlines()

# Part 1
sum_priorities = 0
for baggage in baggages:
    first, second = set(baggage[:len(baggage)//2]), set(baggage[len(baggage)//2:])
    intersection = first & second
    sum_priorities += ascii_letters.index(intersection.pop()) + 1

print(sum_priorities)

# Part 2
sum_priorities = 0
groups = [baggages[i: i + 3] for i in range(0, len(baggages), 3)]
for group in groups:
    first, second, third = set(group[0]), set(group[1]), set(group[2])
    intersection = first & second & third
    sum_priorities += ascii_letters.index(intersection.pop()) + 1

print(sum_priorities)