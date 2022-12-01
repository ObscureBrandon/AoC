with open("input.txt") as f:
    elves_bags = f.read().splitlines()

calories_tracker: list[int] = []
current_calories = 0
for calories in elves_bags:
    if calories == '':
        calories_tracker.append(current_calories)
        current_calories = 0
        continue

    current_calories += int(calories)

# Part 1
print(max(calories_tracker))

#Part 2
print(sum(sorted(calories_tracker, reverse=True)[:3]))
