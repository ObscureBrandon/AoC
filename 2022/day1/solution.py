with open("input.txt") as f:
    elves_bags = f.read().splitlines()

# Part 1
calories_tracker: list[int] = []
current_calories = 0
for calories in elves_bags:
    if calories == '':
        calories_tracker.append(current_calories)
        current_calories = 0
        continue

    current_calories += int(calories)


#Part 2
calories_tracker: list[int] = []
current_calories = 0
for calories in elves_bags:
    if calories == '':
        calories_tracker.append(current_calories)
        current_calories = 0
        continue
    
    current_calories += int(calories)

print(sum(sorted(calories_tracker, reverse=True)[:3]))