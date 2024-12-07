import re
def main():
    part1()
    part2()
    
def part1():
    with open("day03/real_input.txt", "r") as f:
        line = "".join(f)
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    matches = re.findall(pattern, line)
    numbers = [list(map(int, i.split("(")[1].split(")")[0].split(","))) for i in matches]    
    print(sum(x*y for (x,y) in numbers))

def part2():
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    with open("day03/real_input.txt", "r") as f:
        line = "".join(f)
    total_sum = 0
    for part in line.split("do()"):
        part = part.split("don't()")[0]
        matches = re.findall(pattern, part)
        numbers = [list(map(int, i.split("(")[1].split(")")[0].split(","))) for i in matches]    
        total_sum += sum(x*y for (x,y) in numbers)
    print(total_sum)

if __name__ == "__main__":
    main()