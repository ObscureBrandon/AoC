const input = await Deno.readTextFile("input.txt");
const strategy = input
    .trim()
    .split("\n")
    .map((line) => line.trim().split(" "));

const mod = (m: number, n: number) => {
    return ((m % n) + n) % n;
};

const part1 = () => {
    let ans = 0;
    strategy.forEach((item) => {
        const [opp, me] = item;

        const a = "ABC".indexOf(opp);
        const b = "XYZ".indexOf(me);

        ans += b + 1;

        switch (mod(b - a, 3)) {
            case 1:
                ans += 6;
                break;
            case 0:
                ans += 3;
                break;
        }
    });
    return ans;
};

const part2 = () => {
    let ans = 0;
    strategy.forEach((item) => {
        const [opp, me] = item;
        const a = "ABC".indexOf(opp);

        switch (me) {
            case "X":
                ans += mod(a - 1, 3) + 1;
                break;
            case "Y":
                ans += 3;
                ans += a + 1;
                break;
            case "Z":
                ans += 6;
                ans += mod(a + 1, 3) + 1;
        }
    });

    return ans;
};
