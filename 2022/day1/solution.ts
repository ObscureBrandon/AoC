const input = await Deno.readTextFile("input.txt");
const elves_bags = input.split("\n");

const calories_tracker = [];
let current_calories = 0;

for (let i = 0; i < elves_bags.length; i++) {
    const calories = elves_bags[i];
    if (calories == "") {
        calories_tracker.push(current_calories);
        current_calories = 0;
        continue;
    }

    current_calories += parseInt(calories);
}

calories_tracker.sort((a, b) => b - a);

// Part 1
console.log(calories_tracker[0]);

// Part 2
console.log(calories_tracker.slice(0, 3).reduce((a, b) => a + b, 0));
