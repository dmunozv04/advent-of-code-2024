from collections import Counter


def main():
    part1()
    part2()

def part1():
    with open("day01/real_input.txt") as f:
        data = [line.rstrip() for line in f]
    data = [line.split() for line in data]
    left = sorted([int(x[0]) for x in data])
    right = sorted([int(x[1]) for x in data])
    diffs = [abs(x-y) for x,y in zip(left, right)]
    print(sum(diffs))

def part2():
    with open("day01/real_input.txt") as f:
        data = [line.rstrip() for line in f]
    data = [line.split() for line in data]
    left = [int(x[0]) for x in data]
    right = Counter(int(x[1]) for x in data)
    similarities = [x * right[x] for x in left]
    print(sum(similarities))

if __name__ == "__main__":
    main()